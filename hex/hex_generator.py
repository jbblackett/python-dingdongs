import random as r
import time as t

codes = []
hexd = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
t0 = t.time()
extra = 0
# f = open("C:\\Users\\admin\\Documents\\GitHub\\python-dingdongs\\hex\\codes.txt", "w")
f = open("C:\\Users\\admin\\Documents\\GitHub\\python-dingdongs\\hex\\pattern.txt", "w")
for i in range(70000):
    code = ""
    for i in range(10):
        char = r.randint(0,15)
        if char > 9:
            char = hexd[char]
        code += str(char)
    if not(code in codes):
        # f.write(code + "\n")
        codes.append(code)
        extra += 1

    t1 = t.time() - t0
    if t1 > 2:
        f.write(str(extra) + "\n")
        print("Done " + str(extra) + " more. " + str(len(codes)) + " total.")
        t0 = t.time()
        extra = 0
f.close()
