import io
from .axmlprinter import AXMLPrinter
from .arscparser import ARSCParser
from .dexvm import DalvikVM
from xml.dom import minidom

class APK(object):
	def __init__(self):
		self.xml = {}
		self.axml = {}
		self.arsc = {}

	def scan_arsc(self, raw):
		arsc = ARSCParser(raw)
		print arsc.__dict__
		#buff = minidom.parseString(axml.getBuff()).toxml()
		return arsc

	def scan_dex(self, raw):
		import binascii
		print (binascii.hexlify(raw))
		#dexvm = DalvikVM(raw)
		#print dexvm.__dict__
		#buff = minidom.parseString(axml.getBuff()).toxml()
		return "TODO"

	def scan_axml(self, raw):
		axml = AXMLPrinter(raw)
		buff = minidom.parseString(axml.getBuff()).toxml()
		return buff

	def scan_apk(self, raw):
		self.raw = raw
		import zipfile
		zip1 = zipfile.ZipFile(io.BytesIO(raw), mode='r')
		packer = rules()
		test = zip1.testzip()
		axml = []
		if test is not None:
			print 'APK is broken'
		pack = []
		filenames = zip1.namelist()
		for i in zip1.namelist():
			if i in 'AndroidManifest.xml':		
				buff = self.scan_axml(zip1.read(i))
			if i in "resources.arsc" :
				arscobj = self.scan_arsc(zip1.read(i))
			if i in 'classes.dex':
				dex_report = self.scan_dex(zip1.read(i))
				print dex_report.__dict__
			for key in packer.keys():
				if any(value in i for value in packer[key]):
					print key
					if key not in pack:
						pack.append(key)
		return pack, buff, filenames

class CheckMagic(object):
	def __init__(self):
		pass

	def magic_info(self):
		m_zip = ['PK\x03\x04', 'PK\x05\x06', 'PK\x07\x08']
		m_dex = ['dex\n']
		m_odex = ['dey\n']
		m_elf = ['\x7fELF']
		m_axml = ['\x03\x00\x08\x00']
		m_arsc = ['\x02\x00\x0C\x00']
		self.magic = {'apk': m_zip, 'dex': m_dex, 'odex': m_odex ,'elf': m_elf, 'axml': m_axml, 'arsc':m_arsc}
		return self.magic

def rules():
	jsb = ['jsb', 'jshlLib.so']
	appguard = ['assets/appguard/', 'assets/classes.sox']
	dexshield = ['libdxbase.so', 'assets/DXINFO.XML']
	secneo = ['libDexHelper.so', 'libDexHelper-x86.so', 'assets/classes0.jar']
	dexprotector = ['assets/dp.arm.so.dat', 'assets/dp.arm-v7.so.dat', 'assets/dp.x86.so.dat','assets/dp.x86.so.dat', 'assets/dp.mp3', 'assets/dp.arm-v8.so.dat']
	apkprotector = ['apkprotect.com/key.dat', 'apkprotect.com/', 'libAPKProtect.so']
	vkey = ['libhook.so', 'libchecks.so', 'assets/firmware']
	arxan = ['libarxsse.so', 'libarxsse1.so', 'assets/testkeys.dat', 'assets/userkey.dat']
	bangcle = ['libsecexe.so', 'libsecmain.so', 'assets/bangcleplugin/container.dex', 'bangcleclasses.jar', 'bangcle_classes.jar']
	kiro = ['libkiroro.so', 'assets/sbox']
	jiagu = ['assets/ssspbahk.so','jiagu', 'libjiagu.so', 'libjiagu_art.so']
	insidesecure = ['libwb_textfile.so','libtvmbk.so']
	qbdh = ['assets/qdbh']
	liapp = ['/LIAPPEgg','LIAPPClient.sc']
	unicom = ['libunicomsdk.jar','libdecrypt.jar','classes.jar']
	appfortify = ['libNSaferOnly.so']
	nqshield = ['libnqshield.so','nqshield','nqshell']
	tencent =['libshell.so', 'libmobisecy.so', 'com/tencent/StubShell', '/mix.dex']
	ijiami = ['assets/ijiami.dat','ijiami.ajm','assets/ijm_lib/']
	naga = ['libddog.so']
	alibaba = ['libmobisec.so']
	pangxie = ['libnsecure.so']
	medusah = ['libmd.so']
	medusah_appsolid = ['libmd.so','assets/high_resolution.png']
	baidu = ['liblocSDK4b.so', 'libbaiduprotect.so','baiduprotect.jar','baiduprotect1.jar']
	kony = ['libkonyjsvm.so','assets/application.properties','assets/js/startup.js']
	approov = ['libapproov.so', 'assets/cbconfig.JSON']
	packer = {'JSB': jsb, 'AppGuard': appguard, 'DexShield': dexshield, 'SecNeo': secneo, 'DexProtector':dexprotector, 'ApkProtector':apkprotector,'VKey': vkey, 'Arxan GuardIT': arxan, 'Bangcle': bangcle, 'Kiro': kiro, 'Jiagu': jiagu, 'Inside Secure': insidesecure, 'QBDH': qbdh, 'LIAPP' : liapp, 'Unicom': unicom, 'AppFortify': appfortify, 'NQShield': nqshield, 'Tencent': tencent, 'IJIAMI':ijiami, 'NAGA':naga, 'Alibaba': alibaba, 'Pangxie': pangxie, 'Medusah': medusah, 'Medusah AppSolid': medusah_appsolid,'Baidu': baidu, 'Kony': kony, 'Approv': approov}
	return packer
		
	
