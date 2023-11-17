import time


def ves1():
    def UnicCiphar():
        text = "R85dzert!".replace(" ", "_")  # Enter Cipher

        res1 = ""
        res2 = ""

        te = text[::2]
        te1 = text[1::2]
        te2 = text[::3]
        j = 0

        print("Ciphering process started:")
        for i in range(len(te)):
            if j == len(te2):
                j = 0
            te_re = te2[j]
            j += 1
            te_re1 = (ord(te_re) - 96) + ord(te[i])
            print(te_re, (ord(te_re) - 96), te[i], chr(te_re1))

            res1 += chr(te_re1)
        for i in range(len(te1)):
            if j == len(te2):
                j = 0
            te_re = te2[j]
            j += 1
            te_re1 = (ord(te_re) - 96) + ord(te1[i])
            print(te_re, (ord(te_re) - 96), te1[i], chr(te_re1))

            res2 += chr(te_re1)

        # print(res1, res2)
        r = len(te2) // 2
        if len(te2) % 2 == 0:
            res3 = te2[:r]
            res4 = te2[r:]
            return res4 + res1 + res2 + res3


        else:
            res3 = te2[:r]
            res4 = te2[r:]
            return res4 + res1 + res2 + res3
        # print(len(res4 + res1 + res2 + res3), len(res4+res3), res3+res4)

    def UnUnicCiphar(user_cipher):
        encrypted = user_cipher

        i1 = 0
        i2 = 0

        for i in range(len(encrypted)):

            if i2 % 4 == 0:
                i1 += 1
            i2 += 1

        key = i1

        print("Deciphering process started:")
        if len(encrypted) % 2 == 0 and key % 2 != 0:  # Если четное число, но не ключ
            t1 = len(encrypted) - key
            t = t1 // 2
            rekey = key - (key // 2)

            te = encrypted[rekey:rekey + t + 1]
            te1 = encrypted[rekey + t + 1:-(key // 2)]
            te2 = encrypted[-(key // 2):] + encrypted[:rekey]
        elif len(encrypted) % 2 == 0 and key % 2 == 0:  # Если четное число и ключ
            t1 = len(encrypted) - key
            t = t1 // 2

            half = key // 2
            te = encrypted[half:half + t]
            te1 = encrypted[half + t:-half]
            te2 = encrypted[-half:] + encrypted[:half]

        elif len(encrypted) % 2 != 0 and key % 2 != 0:  # Если не четное и ключ не четный
            t1 = len(encrypted) - key
            t = t1 // 2
            rekey = key - (key // 2)
            te = encrypted[rekey:rekey + t]
            te1 = encrypted[rekey + t:-(key - (rekey))]
            te2 = encrypted[-(key - (rekey)):] + encrypted[:rekey]

        elif len(encrypted) % 2 != 0 and key % 2 == 0:  # Если не четное и ключ четный

            t1 = len(encrypted) - key
            t = t1 // 2
            half = key // 2

            te = encrypted[half:half + t + 1]
            te1 = encrypted[half + 1 + t:-half]
            te2 = encrypted[-half:] + encrypted[:half]

        print(te, te1, te2)

        res1 = ''
        res2 = ''
        final_res = ''
        j = 0
        for i in range(len(te)):
            if j == len(te2):
                j = 0
            te_re = te2[j]
            j += 1
            te_re1 = ord(te[i]) - (ord(te_re) - 96)

            res1 += chr(te_re1)
            print(te_re, (ord(te_re) - 96), te[i], chr(te_re1))
        print("++++++")
        for i in range(len(te1)):
            if j == len(te2):
                j = 0
            te_re = te2[j]
            j += 1
            te_re1 = ord(te1[i]) - (ord(te_re) - 96)

            res2 += chr(te_re1)
            print(te_re, (ord(te_re) - 96), te1[i], chr(te_re1))
        # print(res1, res2)

        for i in range(len(res1)):
            if (len(te + te1) % 2 == 1):
                res2 += " "
            res = res1[i] + res2[i]
            final_res += res

        return final_res

    user_cipher = UnicCiphar()

    print(user_cipher)
    print("---------")
    user_decipher = UnUnicCiphar(user_cipher)
    print(user_decipher)


ves1()
time.sleep(60)
