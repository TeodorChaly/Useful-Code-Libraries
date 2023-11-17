import time


def Ciphar(user_text):
    try:
        text = user_text.replace(" ", "_")  # Max - 25 Char

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
            results = res4 + res1 + res2 + res3


        else:
            res3 = te2[:r]
            res4 = te2[r:]
            results = res4 + res1 + res2 + res3
        # print(len(res4 + res1 + res2 + res3), len(res4 + res3), res3 + res4)
        return results
    except Exception as e:
        return "There was an error. Try again (use only English letters)."
#
# user_text = str(
#     input("Input cipher here (without spaces):"))  # For example "I like bananas"
# result = Ciphar('Some text')
# print("\nYour result:")
# print(result)
# time.sleep(60)
