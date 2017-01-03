import random as r


def calcCheckDigit(barcode):
        #Initialise variables
        MULTI = [3,1,3,1,3,1,3]
        check = 0
        multen = None
        #Multiply and sum the digits
        for i in range(7):
                check += int(barcode[i]) * MULTI[i]
        #Find the nearest multiple of 10
        if str(check)[len(str(check))-1] != '0':
                multen = str(((int((str(check))[0]))+1))+'0'
        else:
                multen = check
        #Subtract from nearest multiple of 10
        check = int(multen) - check
        if len(str(check)) > 1:
                check = str(check)[1]
        #Return check digit
        return str(check)
f = open("C:\\Users\\admin\\Documents\\GitHub\\python-dingdongs\\GTIN\\products.csv", "w")
for i in range(10):
    code = ""
    for i in range(7):
        code += str(r.randint(0,9))
    code += calcCheckDigit(code)
    print(code)
    f.write(code + "\n")
