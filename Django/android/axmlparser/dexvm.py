import bytecode 
from struct import pack, unpack

CONF = {
    "BIN_DED": "ded.sh",
    "PATH_DED": "./decompiler/ded/",
    "PATH_DEX2JAR": "./decompiler/dex2jar/",
    "BIN_DEX2JAR": "dex2jar.sh",
    "PATH_JAD": "./decompiler/jad/",
    "BIN_JAD": "jad",
    "BIN_WINEJAD": "jad.exe",
    "PATH_FERNFLOWER": "./decompiler/fernflower/",
    "BIN_FERNFLOWER": "fernflower.jar",
    "OPTIONS_FERNFLOWER": {"dgs": '1',
                           "asc": '1'},
    "PRETTY_SHOW": 1,
    "TMP_DIRECTORY": "/tmp/",
    # Full python or mix python/c++ (native)
    #"ENGINE" : "automatic",
    "ENGINE": "python",
    "RECODE_ASCII_STRING": False,
    "RECODE_ASCII_STRING_METH": None,
    "DEOBFUSCATED_STRING": True,
    #    "DEOBFUSCATED_STRING_METH" : get_deobfuscated_string,
    "PATH_JARSIGNER": "jarsigner",
    "LAZY_ANALYSIS": False,
    "MAGIC_PATH_FILE": None,
    "DEFAULT_API": 19,
    "SESSION": None,
}

class ClassManager(object):
    """
    This class is used to access to all elements (strings, type, proto ...) of the dex format
    """

    def __init__(self, vm, config):
        self.vm = vm
        self.buff = vm

        self.decompiler_ob = None
        self.vmanalysis_ob = None
        self.gvmanalysis_ob = None

        self.__manage_item = {}
        self.__manage_item_off = []

        self.__strings_off = {}

        self.__obj_offset = {}
        self.__item_offset = {}

        self.__cached_proto = {}

        self.recode_ascii_string = config["RECODE_ASCII_STRING"]
        self.recode_ascii_string_meth = None
        if config["RECODE_ASCII_STRING_METH"]:
            self.recode_ascii_string_meth = config["RECODE_ASCII_STRING_METH"]

        self.lazy_analysis = config["LAZY_ANALYSIS"]

        self.hook_strings = {}

        self.engine = []
        self.engine.append("python")

        if self.vm is not None:
            self.odex_format = self.vm.get_format_type() == "ODEX"

class HeaderItem(object):
    def __init__(self, size, buff, cm):
        self.CM = cm
        #buff = bytecode.BuffHandle(buff)
        self.offset = 0

        self.magic, = unpack("=Q", buff.read(8))
        self.checksum, = unpack("=i", buff.read(4))
        self.signature, = unpack("=20s", buff.read(20))
        self.file_size, = unpack("=I", buff.read(4))
        self.header_size, = unpack("=I", buff.read(4))
        self.endian_tag, = unpack("=I", buff.read(4))
        self.link_size, = unpack("=I", buff.read(4))
        self.link_off, = unpack("=I", buff.read(4))
        self.map_off, = unpack("=I", buff.read(4))
        self.string_ids_size, = unpack("=I", buff.read(4))
        self.string_ids_off, = unpack("=I", buff.read(4))
        self.type_ids_size, = unpack("=I", buff.read(4))
        self.type_ids_off, = unpack("=I", buff.read(4))
        self.proto_ids_size, = unpack("=I", buff.read(4))
        self.proto_ids_off, = unpack("=I", buff.read(4))
        self.field_ids_size, = unpack("=I", buff.read(4))
        self.field_ids_off, = unpack("=I", buff.read(4))
        self.method_ids_size, = unpack("=I", buff.read(4))
        self.method_ids_off, = unpack("=I", buff.read(4))
        self.class_defs_size, = unpack("=I", buff.read(4))
        self.class_defs_off, = unpack("=I", buff.read(4))
        self.data_size, = unpack("=I", buff.read(4))
        self.data_off, = unpack("=I", buff.read(4))

        self.map_off_obj = None
        self.string_off_obj = None
        self.type_off_obj = None
        self.proto_off_obj = None
        self.field_off_obj = None
        self.method_off_obj = None
        self.class_off_obj = None
        self.data_off_obj = None

class MapList(object):
    """
    This class can parse the "map_list" of the dex format
    """

    def __init__(self, cm, off, buff):
        self.CM = cm

        buff.set_idx(off)

        self.offset = off

        self.size = unpack("=I", buff.read(4))[0]

        self.map_item = []
        for i in range(0, self.size):
            idx = buff.get_idx()

            mi = MapItem(buff, self.CM)
            self.map_item.append(mi)

            buff.set_idx(idx + mi.get_length())

            c_item = mi.get_item()
            if c_item is None:
                mi.set_item(self)
                c_item = mi.get_item()

            self.CM.add_type_item(TYPE_MAP_ITEM[mi.get_type()], mi, c_item)

        for i in self.map_item:
            androconf.debug("Reloading %s" % TYPE_MAP_ITEM[i.get_type()])
            started_at = time.time()
            i.reload()
            diff = time.time() - started_at
            minutes, seconds = float(diff // 60), float(diff % 60)
            androconf.debug(
                "End of reloading %s = %s:%s" % (TYPE_MAP_ITEM[i.get_type()], str(minutes), str(round(seconds, 2))))

class DalvikVM(object):
	def __init__(self, buff):
		self.magic = buff[:3]
		self.api_version = 19
		self.config = {'RECODE_ASCII_STRING': False, 'RECODE_ASCII_STRING_METH': None, 'LAZY_ANALYSIS': False}
		self.CM = ClassManager(self, self.config)
		self._load(buff)

	def _load(self, buff):
		self.__header = HeaderItem(0, self, ClassManager(None, self.config))
		if self.__header.map_off == 0:
			print "no map list ..."
		else:
			self.map_list = MapList(self.CM, self.__header.map_off, self)
			self.classes = self.map_list.get_item_type("TYPE_CLASS_DEF_ITEM")
			self.methods = self.map_list.get_item_type("TYPE_METHOD_ID_ITEM")
			self.fields = self.map_list.get_item_type("TYPE_FIELD_ID_ITEM")
			self.codes = self.map_list.get_item_type("TYPE_CODE_ITEM")
			self.strings = self.map_list.get_item_type("TYPE_STRING_DATA_ITEM")
			self.debug = self.map_list.get_item_type("TYPE_DEBUG_INFO_ITEM")
			self.header = self.map_list.get_item_type("TYPE_HEADER_ITEM")
		self._flush()
	
	def _flush(self):
		self.classes_names = None
		self.__cache_methods = None
		self.__cached_methods_idx = None
		self.__cache_fields = None
		self.__cache_all_methods = None
		self.__cache_all_fields = None

	def get_format_type(self):
		if self.magic is 'dex':
			return 'DEX'
		elif self.magic is 'dey':
			return 'ODEX'
		else:
			return 'Unknown Format'
	