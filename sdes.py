
class SDES:

    def permute(self, bit, num):
        num = 'x' + num
        res = ''
        move = []
        if bit == 10:
            move = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        elif bit == 8:
            move = [6, 3, 7, 4, 8, 5, 10, 9]
        else:
            move = [2, 4, 3, 1]
        for i in move:
            res += num[i]
        return res

    def divide_half(self, num):
        return num[0: int(len(num)/2)], num[int(len(num)/2):  len(num)]

    def shift_left(self, bit, left_num, right_num):
        for i in range(bit):
            left_res = left_num[1: len(left_num)] + left_num[0]
            left_num = left_res

        for i in range(bit):
            right_res = right_num[1: len(right_num)] + right_num[0]
            right_num = right_res
        return left_res, right_res

    def ip(self, bit, num):
        num = 'x' + num
        res = ''
        move = []
        if bit == 8:
            move = [2, 6, 3, 1, 4, 8, 5, 7]

        for i in move:
            res += num[i]

        return res

    def ip_inverse(self, bit, num):
        num = 'x' + num
        res = ''
        move = []
        if bit == 8:
            move = [4, 1, 3, 5, 7, 2, 8, 6]

        for i in move:
            res += num[i]

        return res

    def ep(self, bit, num):
        num = 'x' + num
        res = ''
        expand = [4, 1, 2, 3, 2, 3, 4, 1]
        for i in expand:
            res += num[i]
        return res

    def xor(self, key, num):
        res = ''
        for i in range(len(num)):
            if num[i] == key[i]:
                res += '0'
            else:
                res += '1'
        return res

    def sbox(self, numl, numr):
        s0 = [['01', '00', '11', '10'], ['11', '10', '01', '00'],
              ['00', '10', '01', '11'], ['11', '01', '11', '10'], ]

        s1 = [['00', '01', '10', '11'], ['10', '00', '01', '11'],
              ['11', '00', '01', '00'], ['10', '01', '00', '11'], ]

        rl = int(numl[0] + numl[3], 2)
        cl = int(numl[1] + numl[2], 2)

        rr = int(numr[0] + numr[3], 2)
        cr = int(numr[1] + numr[2], 2)

        return s0[rl][cl] + s1[rr][cr]

    def sw(self, num):
        return self.divide_half(num)[1] + self.divide_half(num)[0]

    def gen_key(self, key):
        k = self.permute(10, key)
        lh, rh = self.divide_half(k)
        lh, rh = self.shift_left(1, lh, rh)
        k1 = self.permute(8, lh + rh)

        lh, rh = self.shift_left(2, lh, rh)
        k2 = self.permute(8, lh + rh)

        return k1, k2

    def encrypt(self, key, plain):

        k1, k2 = self.gen_key(key)

        p = self.ip(8, plain)
        lh, rh = self.divide_half(p)
        op = self.ep(4, rh)
        op = self.xor(k1, op)
        sr = self.sbox(self.divide_half(op)[0], self.divide_half(op)[1])
        op = self.permute(4, sr)
        op = self.xor(lh, op)
        op = op + rh

        op = self.sw(op)

        lh, rh = self.divide_half(op)
        op = self.ep(4, rh)
        op = self.xor(k2, op)
        sr = self.sbox(self.divide_half(op)[0], self.divide_half(op)[1])
        op = self.permute(4, sr)
        op = self.xor(lh, op)
        op = op + rh
        cipher = self.ip_inverse(8, op)
        return cipher

    def decrypt(self, key, cipher):

        k1, k2 = self.gen_key(key)

        p = self.ip(8, cipher)
        lh, rh = self.divide_half(p)
        op = self.ep(4, rh)
        op = self.xor(k2, op)
        sr = self.sbox(self.divide_half(op)[0], self.divide_half(op)[1])
        op = self.permute(4, sr)
        op = self.xor(lh, op)
        op = op + rh

        op = self.sw(op)

        lh, rh = self.divide_half(op)
        op = self.ep(4, rh)
        op = self.xor(k1, op)
        sr = self.sbox(self.divide_half(op)[0], self.divide_half(op)[1])
        op = self.permute(4, sr)
        op = self.xor(lh, op)
        op = op + rh
        plain = self.ip_inverse(8, op)
        return plain
