#GTIN-8 TEST
#Import csv module
import csv
#Initialise variables
border = "-------------------------------------------------------------------------"
borderlong = "--------------------------------------------------------------------------------------------------------------------------------"
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
        print("| {0:^10} | {1:^5} | {2:^50}".format("GTIN-8","Price","Description"))
        print(border)
        for i in range(len(products)):
                print("| {0:^10} | {1:^5} | {2:^50}" .format(products[i][0], "£" + str("%.2f" % float(products[i][2])), products[i][1]))
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
                                        break
                                except ValueError:
                                        print("Quantity must be an integer.")
                        #Calculate price of that quantity of product
                        price = float(quantity) * float(products[product][2])
                        #Print price of that quantity of product
                        print()
                        print(str(quantity) + " x " + products[product][1] + " = £" + str("%.2f" % price))
                        #Add product code and quantity to order
                        order.append([product,quantity,price])
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
        print("| {0:^10} | {1:^50} | {2:^20} | {3:^10} | {4:^20}".format("GTIN-8","Description","Price (each)","Quantity","Price (all)"))
        print(borderlong)
        for i in range(len(order)):
                #Use variables to make printing less complicated
                gtin = products[order[i][0]][0]
                desc = products[order[i][0]][1]
                pricepp = "£" + str("%.2f" % float(products[order[i][0]][2]))
                quantity = str(order[i][1])
                priceall = "£" + str("%.2f" % float(order[i][2]))

                #Print product row
                print("| {0:^10} | {1:^50} | {2:^20} | {3:^10} | {4:^20}".format(gtin,desc,pricepp,quantity,priceall))
                print(borderlong)
                total += order[i][2]

        #print price total row
        total = "£" + str("%.2f" % float(total))
        print("| {0:^10} | {1:^50} | {2:^20} | {3:^10} | {4:^20}".format("Total","","","",total))
        print(borderlong)
        print()        

#Function to restock any understocked products


#Main program
#Import products from file to list
with open("products.csv", 'rU') as f:
    reader = csv.reader(f)
    products = list(list(rec) for rec in csv.reader(f, delimiter=','))

#Options
while True:
        #Print options
        print(" 1. Check the validity of a GTIN-8 barcode.")
        print(" 2. Calculate the check digit from the first 7 digits of a GTIN-8 barcode.")
        print(" 3. Order products from our inventory.")
        print(" 4. Restock any under-stocked products.")
        print(" 5. Exit.")
        #Input the option
        num = input("Enter a number: ")
        if num == '1':
                print('\n' + checkDigitCorrect(inputBarcode(8)) + '\n')
        elif num == '2':
                print("\nThe check digit is " + calcCheckDigit(inputBarcode(7)) + ".\n")
        elif num == '3':
                orderProducts()
        elif num == '4':
                restockProducts()
        elif num == '5':
                exit()
