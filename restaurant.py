import os
name = ["Chomin", "momo\t","Noodles", "Samosa", "Chicken", "Pizza","Mushroom","Mix Veg","Sandwich","Burger"]
rate = [70, 120, 20,130, 250, 320,410,280,250,340]
vat = 13
discount = 10
myList = []
itemList = []
itemAmount = []
itemRate = []
itemQuantity = []


def error():  # display when ther is erron on the code
    print("!!! ERROR !!!")
    exit()


def welcome():  # the welcome message
    os.system('cls')
    print('''
            -------BIPOs FOOD-------
          Get the best food in town
        
             Today's special :-)
    ''')


def ThankYou():  # thankyou message
    print('''
                                   Thank you :)
                                -Visit us again
    ''')


def checkLenght(i, j):  # check the length of menu item and price for the efficent running of programe
    if len(i) != len(j):
        error()
def checkTheRepeat(itemNo,Quantity):
    indexOfRepeat = -1
    r = -1
    for repeatElement in itemList:
        indexOfRepeat = indexOfRepeat + 1
        if repeatElement == name[itemNo]:
            r = indexOfRepeat
    if r == -1:
        return -1
    else:
        return r



def printList():  # this will print the list of product available
    for i in range(len(name)):
        print(f"{i+1}: {name[i]}\tRs.{rate[i]}")
    print("\n\n")


def takeOrder(ItemNo):  # this will take input form user and call different function
    if ItemNo == 0:  # take input for the first time
        ItemNo = int(input("Enter order num: "))
    ItemNo = ItemNo - 1     # to work with 0 index
    if ItemNo in range(len(name)):  # check if the input item is available or not
        Quantity = int(input("Quantity: "))
        isRepeat=checkTheRepeat(ItemNo,Quantity)
        if isRepeat == -1:  #the order is not repeat
            orderListNoRepeat(ItemNo,Quantity)
        else:
            orderListRepeat(ItemNo,Quantity,isRepeat)

        bill(ItemNo, Quantity,isRepeat)  # calculate the bill
    else:
        os.system('cls')
        print("\nEnter the item number, Sn. number of item you want to order.\neg: enter 1 if you want Chomin \n")
        printList()
        takeOrder(0)


def orderListNoRepeat(ItemNo, Quantity):    #for order list if there is no repert
    if name[ItemNo] != "momo\t":
        tempOrderList = f"{name[ItemNo]}"
    else:
        tempOrderList = f"{name[ItemNo][:-1]}"      #remover \n form momo 
    tempOrderList = f"{tempOrderList}" + " => " + f"{Quantity}"
    myList.append(tempOrderList)

    # print(myList)     //not printig here to make the ui more clean

def orderListRepeat(ItemNo, Quantity,isRepeat):    #for order list if there is repert
    if name[ItemNo] != "momo\t":
        tempOrderList = f"{name[ItemNo]}"
    else:
        tempOrderList = f"{name[ItemNo][:-1]}"      #remover \n form momo 

    myList[isRepeat] = f"{tempOrderList}" + " => " + f"{Quantity}"

    # print(myList)     //not printig here to make the ui more clean


def orderMore():            #for multiple orders
    os.system('cls')
    print("\n" + f"{myList}"+"\n")         #format and store order information 
    printList()
    check = input("\nMore Order ?( n = No or Enter order Num): ")   
    if check == 'n' or check == '' or check == "N":  #check if user want to orde or not
        printBill(itemList, itemAmount)     

    else:
        takeOrder(int(check))


def bill(item, Quantity,isRepeat):
    if isRepeat == -1:          #check if the order item is repeted or not
        itemList.append(name[item])
        itemQuantity.append(Quantity)
        itemRate.append(rate[item])
        itemAmount.append(rate[item]*Quantity)
        orderMore()
    else:
        itemQuantity[isRepeat] = Quantity
        orderMore()

        


def printBill(itemList, itemAmount):
    totalAmount = 0
    os.system('cls')
    print('''
        -------BIPOs FOOD-------
      Get the best food in town
        Tilottama -9, Manigram
    
          
          -----Bill-----


''')
    print("\nSn. Items\tRate\tQuantity\tCost")
    for i in range(len(itemAmount)):
        print(
            f"{i+1}: {itemList[i]}\t{itemRate[i]}\t{itemQuantity[i]}\t\tRs.{itemAmount[i]}")
        totalAmount = totalAmount + itemAmount[i]
    print(f"""


---------------------------------------------
                              Total: Rs.{totalAmount}
""")


checkLenght(name, rate)  # this check the if all item has rate or not
welcome()
print("Sn. Item \tRate")
printList()
takeOrder(0)
# inside takeorder() myList() is call which include the list of orders
# after bill() is call inside takeOrder()
# this function is also called in orderMore function // printBill(itemList, itemAmount)
ThankYou()
