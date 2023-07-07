import os
name = ["Comin","momo\t", "Samosa", "Chicken", "Pizza"]
rate = [70,120,20, 250, 320]
vat = 13
discount = 10
myList = []
itemList = []
itemAmount = []
itemRate = []
itemQuantity = []

def error():
    print("!!! ERROR !!!")
    exit()

def welcome():
    os.system('cls')
    print('''
            -------Welcome-------
          Get the best food in town
        
             Today's special :-)
    ''')


def ThankYou():
    print('''\n\n\n\n
Thank you :)
-Visit us again
    ''')


def checkLenght(i, j):
    if len(i) != len(j):
        error()


def printList():
    for i in range(len(name)):
        print(f"{i+1}: {name[i]}\tRs.{rate[i]}")
    print("\n\n")



def takeOrder(ItemNo):
    if ItemNo == 0:
        ItemNo = int(input("Enter order num: "))
    ItemNo = ItemNo - 1
    if ItemNo in range(len(name)):
        Quantity = int(input("Quantity: "))
        orderList(ItemNo, Quantity)
        bill(ItemNo, Quantity)
    else:
       os.system('cls')
       print("\nEnter the item number, Sn. numberof item you want to order.\neg: enter 2 if you want samosa\n")
       printList()
       takeOrder(0)

def orderList(ItemNo,Quantity):
    if name[ItemNo] != "momo\t":
        tempOrderList = f"{name[ItemNo]}"
    else:
        tempOrderList = f"{name[ItemNo][:-1]}"
    # myList.append(f"")
    tempOrderList = f"{tempOrderList}" + " => "+ f"{Quantity}"
    myList.append(tempOrderList)
    # print(myList)     //not printig here to make the ui more clean


def orderMore():
    os.system('cls')
    print("\n"+ f"{myList}"+"\n")
    printList()
    check = input("\nMore Order ?( n = No or Enter order Num): ")
    if check == 'n' or check == '' or check == "N":
        printBill(itemList, itemAmount)
        
    else:
        takeOrder(int(check))


def bill(item, Quantity):
    if item not in itemList:
        itemList.append(name[item])
        itemQuantity.append(Quantity)
        itemRate.append(rate[item])
        itemAmount.append(rate[item]*Quantity)
        orderMore()
    


def printBill(itemList,itemAmount):
    print("\n\nYour total bill is:")
    print("\nSn. Items\t\tRate\tQuantity\tCost")
    for i in range(len(itemAmount)):
        print(f"{i+1}: {itemList[i]}\t\t{itemRate[i]}\t{itemQuantity[i]}\t\tRs.{itemAmount[i]}")

checkLenght(name, rate)  #this check the if all item has rate or not
welcome()
print("Sn. Item \tRate")
printList()
takeOrder(0)
#inside takeorder() myList() is call which include the list of orders
#after bill() is call inside takeOrder()
#this function is also called in orderMore function // printBill(itemList, itemAmount)
ThankYou()