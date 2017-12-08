# This file is part of Androguard.
#
# Copyright (C) 2010, Anthony Desnos <desnos at t0t0.fr>
# All rights reserved.
#
# Androguard is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Androguard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Androguard.  If not, see <http://www.gnu.org/licenses/>.

import bytecode

from bytecode import SV

from io import StringIO
from struct import pack, unpack
from xml.dom import minidom

class StringBlock:
    """
    axml format translated from:
    http://code.google.com/p/android4me/source/browse/src/android/content/res/AXmlResourceParser.java
    """
    def __init__(self, buff, header):
        self._cache = {}
        self.header = header

        self.stringCount, = unpack('<i', buff.read(4))
        self.styleOffsetCount, = unpack('<i', buff.read(4)) 
        self.flags, = unpack('<i', buff.read(4))
        self.m_isUTF8 = (self.flags & (1 << 8) != 0)

        self.stringsOffset, = unpack('<i', buff.read(4)) 
        self.stylesOffset, = unpack('<i', buff.read(4)) 

        if self.styleOffsetCount == 0 and self.stylesOffset > 0:
            print "Styles Offset given, but styleCount is zero."

        self.m_stringOffsets = []
        self.m_styleOffsets = []
        self.m_strings = ""
        self.m_styles = []

        for i in range(0, self.stringCount):
            self.m_stringOffsets.append(SV('<i', buff.read(4)))

        for i in range(0, self.styleOffsetCount):
            self.m_styleOffsets.append(SV('<i', buff.read(4)))

        size = self.header.size - self.stringsOffset

        if self.stylesOffset != 0 and self.styleOffsetCount != 0:
            size = self.stylesOffset - self.stringsOffset

        if (size % 4) != 0:
            pass

        self.m_strings = buff.read(size)

        if self.stylesOffset!= 0 and self.styleOffsetCount != 0:
            size = self.header.size - self.stylesOffset
            if (size % 4) != 0:
                pass

            for i in range(0, size // 4):
                self.m_styles.append(SV('<i', buff.read(4)))

    def getRaw(self, idx):
        if idx in self._cache:
            return self._cache[idx]
        if idx < 0 or not self.m_stringOffsets or idx >= len(self.m_stringOffsets):
            return ""
        offset = self.m_stringOffsets[idx].get_value()

        if self.m_isUTF8:
            self._cache[idx] = self.decode8(offset)
        else:
            self._cache[idx] = self.decode16(offset)

        return self._cache[idx]

    def decode8(self, offset):
        str_len, skip = self.decodeLength(offset, 1)
        offset += skip

        encoded_bytes, skip = self.decodeLength(offset, 1)
        offset += skip

        data = self.m_strings[offset: offset + encoded_bytes]

        return self.decode_bytes(data, 'utf-8', str_len)

    def decode16(self, offset):
        str_len, skip = self.decodeLength(offset, 2)
        offset += skip

        encoded_bytes = str_len * 2

        data = self.m_strings[offset: offset + encoded_bytes]

        return self.decode_bytes(data, 'utf-16', str_len)

    def decode_bytes(self, data, encoding, str_len):
        string = data.decode(encoding, 'replace')
        if len(string) != str_len:
            androconf.warning("invalid decoded string length")
        return string

    def decodeLength(self, offset, sizeof_char):
        length = self.m_strings[offset]
        sizeof_2chars = sizeof_char << 1
        fmt_chr = 'B' if sizeof_char == 1 else 'H'
        fmt = "<2" + fmt_chr
        length1, length2 = unpack(fmt, self.m_strings[offset:(offset + sizeof_2chars)])
        highbit = 0x80 << (8 * (sizeof_char - 1))
        if (length1 & highbit) != 0:
            return ((length1 & ~highbit) << (8 * sizeof_char)) | length2, sizeof_2chars
        else:
            return length1, sizeof_char
