class Crypto:
    """Requires key"""
    def __init__(self, key: bytes):
        self.key = key


class Plaintext:
    """plaintext type for Crypto"""

    def __init__(self, dat):
        """str, list of ints, bytes, bytearray supported"""

        typ = type(dat)
        if typ == str:
            temp_dat = list(dat.encode())
        elif typ == list:
            self.dat= dat
            return
        elif typ == bytes or typ == bytes:
            temp_dat = list(dat)
        else:
            raise TypeError(f"Invalid type: {typ}. Try str, list of ints, bytes, or bytearray.")

        self.dat = []
        for i in range(0, len(temp_dat), 2):
            self.dat.append((temp_dat[i] * 256) + temp_dat[i+1])

    def in_hex(self):
        tmp = []
        for item in self.dat:
            tmp.append(item // 256)
            tmp.append(item % 256)
        return tmp

    def large_blocks(self):
        tmp = []
        for i in range(0, len(self.dat), 16):
            tmp2 = []
            for j in range(16):
                tmp2.append(self.dat[i+j])
            tmp.append(tmp2)
        return tmp

    def __str__(self):
        return str(bytes(self))

    def __iter__(self):
        return iter(self.dat)

    def __len__(self):
        return len(self.dat)

    def __bytes__(self):
        return bytes(self.in_hex())

    def __add__(self, other):
        return Plaintext(self.dat + other.dat)


class Ciphertext(Plaintext):
    def __add__(self, other):
        return Ciphertext(self.dat + other.dat)
    """ciphertext type for Crypto"""


if __name__ == "__main__":
    ooo = Plaintext("abcdabcdabcdabcdabcdabcdabcdabcd")
    print(ooo.large_blocks())
