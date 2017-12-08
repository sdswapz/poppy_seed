from .axmlparser import ARSCHeader
from struct import pack, unpack
import bytecode
from stringblock import StringBlock
import collections

class ARSCResTablePackage(object):
    def __init__(self, buff, header):
        self.header = header
        self.start = buff.get_idx()
        self.id, = unpack('<I', buff.read(4))
        self.name = buff.readNullString(256)
        self.typeStrings, = unpack('<I', buff.read(4))
        self.lastPublicType, = unpack('<I', buff.read(4))
        self.keyStrings, = unpack('<I', buff.read(4))
        self.lastPublicKey, = unpack('<I', buff.read(4))
        self.mResId = self.id << 24

    def get_name(self):
        name = self.name.decode("utf-16", 'replace')
        name = name[:name.find("\x00")]
        return name

class PackageContext(object):
    def __init__(self, current_package, stringpool_main, mTableStrings,
                 mKeyStrings):
        self.stringpool_main = stringpool_main
        self.mTableStrings = mTableStrings
        self.mKeyStrings = mKeyStrings
        self.current_package = current_package

    def get_mResId(self):
        return self.current_package.mResId

    def set_mResId(self, mResId):
        self.current_package.mResId = mResId

    def get_package_name(self):
        return self.current_package.get_name()

class ARSCParser(object):
    def __init__(self, raw_buff):
        self.analyzed = False
        self._resolved_strings = None
        self.buff = bytecode.BuffHandle(raw_buff)

        self.header = ARSCHeader(self.buff)
        self.packageCount = unpack('<i', self.buff.read(4))[0]

        self.packages = {}
        self.values = {}
        self.resource_values = collections.defaultdict(collections.defaultdict)
        self.resource_configs = collections.defaultdict(lambda: collections.defaultdict(set))
        self.resource_keys = collections.defaultdict(
            lambda: collections.defaultdict(collections.defaultdict))
        self.stringpool_main = None

        self.buff.set_idx(self.header.start + self.header.header_size)

        data_end = self.header.start + self.header.size

        while self.buff.get_idx() <= data_end - ARSCHeader.SIZE:
            res_header = ARSCHeader(self.buff)

            if res_header.start + res_header.size > data_end:
                # this inner chunk crosses the boundary of the table chunk
                break

            if res_header.type == 0x0001 and not self.stringpool_main:
                self.stringpool_main = StringBlock(self.buff, res_header)

            elif res_header.type == 0x0200:
                print len(self.packages) < self.packageCount, "Got more packages than expected"

                current_package = ARSCResTablePackage(self.buff, res_header)
                package_name = current_package.get_name()
                package_data_end = res_header.start + res_header.size

                self.packages[package_name] = []

                self.buff.set_idx(current_package.header.start + current_package.typeStrings)
                type_sp_header = ARSCHeader(self.buff)
                assert type_sp_header.type == 0x0001, \
                    "Expected String Pool header, got %x" % type_sp_header.type
                mTableStrings = StringBlock(self.buff, type_sp_header)

                self.buff.set_idx(current_package.header.start + current_package.keyStrings)
                key_sp_header = ARSCHeader(self.buff)
                assert key_sp_header.type == 0x0001, \
                    "Expected String Pool header, got %x" % key_sp_header.type
                mKeyStrings = StringBlock(self.buff, key_sp_header)

                self.packages[package_name].append(current_package)
                self.packages[package_name].append(mTableStrings)
                self.packages[package_name].append(mKeyStrings)

                pc = PackageContext(current_package, self.stringpool_main,
                                    mTableStrings, mKeyStrings)

                # skip to the first header in this table package chunk
                self.buff.set_idx(res_header.start + res_header.header_size)

                while self.buff.get_idx() <= package_data_end - ARSCHeader.SIZE:

                    pkg_chunk_header = ARSCHeader(self.buff)
                    if pkg_chunk_header.start + pkg_chunk_header.size > package_data_end:
                        # we are way off the package chunk; bail out
                        break

                    self.packages[package_name].append(pkg_chunk_header)

                    if pkg_chunk_header.type == RES_TABLE_TYPE_SPEC_TYPE:
                        self.packages[package_name].append(ARSCResTypeSpec(
                            self.buff, pc))

                    elif pkg_chunk_header.type == RES_TABLE_TYPE_TYPE:
                        a_res_type = ARSCResType(self.buff, pc)
                        self.packages[package_name].append(a_res_type)
                        self.resource_configs[package_name][a_res_type].add(
                            a_res_type.config)

                        entries = []
                        for i in range(0, a_res_type.entryCount):
                            current_package.mResId = current_package.mResId & 0xffff0000 | i
                            entries.append((unpack('<i', self.buff.read(4))[0],
                                            current_package.mResId))

                        self.packages[package_name].append(entries)

                        for entry, res_id in entries:
                            if self.buff.end():
                                break

                            if entry != -1:
                                ate = ARSCResTableEntry(self.buff, res_id, pc)
                                self.packages[package_name].append(ate)
                    elif pkg_chunk_header.type == RES_TABLE_LIBRARY_TYPE:
                        print "RES_TABLE_LIBRARY_TYPE chunk is not supported"
                    else:
                        # silently skip other chunk types
                        pass

                    # skip to the next chunk
                    self.buff.set_idx(pkg_chunk_header.start + pkg_chunk_header.size)

            # move to the next resource chunk
            self.buff.set_idx(res_header.start + res_header.size)