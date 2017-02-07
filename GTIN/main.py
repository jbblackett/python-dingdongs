#GTIN-8 TEST
#Import csv module
import csv
#Initialise variables
border = "—"*65
borderlong = "—"*126
#Function to input and validates given digit GTIN-8 code
def inputBarcode(digits):
        valid = False
        while valid == False:
                barcode = input("\nEnter a GTIN-8 code (" + str(digits) + " digits): ")
                if len(barcode) == digits:
                        if barcode.isdigit():
                                valid = True
                        else:
                                print("The GTIN-8 code must be numerical.")
                else:
                        print("The GTIN-8 code must be " + str(digits) + " digits long.")
        return(barcode)


#Function to calculate and compare the check digit to the given check digit returning true or false
def checkDigitCorrect(barcode):
        check = calcCheckDigit(barcode[:7])
        #Compare calculated check digit to the given one and return
        if str(check) == barcode[7]:
                return("The GTIN-8 code is valid.")
        else:
                return("The GTIN-8 code is invalid. The check digit should be " + str(check) + ".")

#Function to calculate the check digit from the first 7 digits
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

#Function to order products
def orderProducts():
        #Initialise variables
        order = []
        global border
        #Print products list
        print()
        print("Products:")
        print(border)
        print("| {0:^10} | {1:^5} | {2:^40} |".format("GTIN-8","Price","Description"))
        print(border)
        for i in range(len(products)):
                print("| {0:^10} | {1:^5} | {2:40} |" .format(products[i][0], "£" + str("%.2f" % float(products[i][2])), products[i][1]))
        print(border)
        #Loop to get list of wanted products and their quantities
        done = False
        while not done:
                #Input code
                code = input("Enter GTIN-8 product code: ")
                found = False
                for i in range(len(products)):
                        if products[i][0] == code:
                                found = True
                                product = i
                #If code not in products list then print error message
                if not found:
                        print("Product not found.")
                #Otherwise (product found)
                else:
                        #Display selected product
                        print()
                        print("Product found:")
                        print(products[product][1] + " at " + "£" + str("%.2f" % float(products[product][2]) + " each."))
                        print()
                        #Loop to get and validate quantity of product
                        while True:
                                quantity = input("Quantity: ")
                                try:
                                        v = int(quantity)
                                        if v < 1:
                                                print("Quantity must be positive.")
                                                continue
                                        if v > 100000:
                                                print("Cannot order more than 100,000 items.")
                                                continue
                                        break
                                except ValueError:
                                        print("Quantity must be an integer.")
                        #Calculate price of that quantity of product
                        price = float(quantity) * float(products[product][2])
                        #Print price of that quantity of product
                        print()
                        print(str(quantity) + " x " + products[product][1] + " = £" + str("%.2f" % price))
                        #Add product code and quantity to order
                        order.append([products[product][0],quantity])
                        print("Added to basket.")
                        print()
                        #Loop to find if another product wanted
                        again = ""
                        while not(again == "yes" or again == "no"):
                                again = input("Another product? ")
                        if again == "yes":
                                done = False
                        else:
                                done = True
                                
        #Print reciept and find total
        total = 0
        print()
        print("Thank you, here is your recipt:")
        print(borderlong)
        print("| {0:^10} | {1:^50} | {2:^20} | {3:^10} | {4:^20} |".format("GTIN-8","Description","Price (each)","Quantity","Price (total)"))
        print(borderlong)
        for i in range(len(order)):
                #Use variables to make printing less complicated
                gtin = order[i][0]
                count = 0
                for j in range(len(products)):
                        try:
                                products[j].index(gtin)
                                productind = j
                                continue
                        except ValueError:
                                pass
                desc = products[productind][1]
                price = float(products[productind][2])
                pricepp = "£" + str("%.2f" % price)
                
                quantity = order[i][1]
                
                subtotal = float(products[productind][2]) * float(quantity)
                priceall = "£" + str("%.2f" % subtotal)

                #Print product row
                print("| {0:^10} | {1:50} | {2:^20} | {3:^10} | {4:^20} |".format(gtin,desc,pricepp,quantity,priceall))
                print(borderlong)
                total += subtotal

        #print price total row
        total = "£" + str("%.2f" % float(total))
        print("| {0:^10} | {1:^50} | {2:^20} | {3:^10} | {4:^20} |".format("Total ","","","",total))
        print(borderlong)
        print()
        restockProducts(order)


#Function to restock any understocked products
def restockProducts(order):
        print(stock)
        #Reduce all current stock by the quantity in order
        for i in range(len(order)):
                quantity = int(order[i][1])
                gtin = order[i][0]
                #Find stock list index for current product
                for j in range(len(stock)):
                        try:
                                stock[j].index(gtin)
                                stockind = j
                                continue
                        except ValueError:
                                pass
                #Change current stock value
                stock[stockind][1] = str(int(stock[stockind][1]) - quantity)
        print("\n")
        print(stock)


        
#Main program
#Import products from file to list
try:
        with open("products.csv", 'rU') as f:
            reader = csv.reader(f)
            products = list(list(rec) for rec in csv.reader(f, delimiter=','))
        productsCsv = True
except:
        productsCsv = False

#Import stock levels from file to two-dimensional list
try:
        with open("stock.csv", "rU") as f:
            reader = csv.reader(f)
            stock = list(list(rec) for rec in csv.reader(f, delimiter=","))
        stockCsv = True
except:
        stockCsv = False

#Print welcome message
print("Welcome! Please use this program in IDLE in full screen (Python 3.0.0+).\n")


#Options
while True:
        #Print options
        print(" 1. Check the validity of a GTIN-8 barcode.")
        print(" 2. Calculate the check digit from the first 7 digits of a GTIN-8 barcode.")
        print(" 3. Order products from our inventory.")
        print(" 4. Exit.")
        #Input the option
        num = input("Enter a number: ")
        if num == '1':
                print('\n' + checkDigitCorrect(inputBarcode(8)) + '\n')
        elif num == '2':
                print("\nThe check digit is " + calcCheckDigit(inputBarcode(7)) + ".\n")
        elif num == '3':
                if productsCsv:
                        if stockCsv:
                                orderProducts()
                        else:
                                print("\nCound not find stock levels list (stock.csv).\n")
                else:
                        print("\nCould not find products list (products.csv).\n")
        elif num == '4':
                exit()
