#define the menu of Restaurant
menu={
'Pizza':60,
'black coffee':50,
'cold coffee':50,
'Momoz':70,
'Pasta':50,
'Burger':45,
'Salad':40,
'Simple Coffee':30,
'Sandwhich':35,
'Choumin':55,
}

#greet
print("Welcome to DHAKAD Cafe")
print("Pizza: Rs60\nblack coffee: Rs50\nblack coffee: Rs50\ncold coffee: Rs50\nMomoz: Rs70\nPasta: Rs50\nBurger: Rs45\nSalad: Rs40\nSimple Coffee: Rs30\nSandwhich: Rs35\nChoumin: Rs55")
# add next item in same order
order_total = 0
item_1=input("Enter the name of itemyou want to order = ")
if item_1 in menu: #membership opreter
    order_total+= menu[item_1]  #0+70
    print (f"your item {item_1} has been add to your order")#f =formating strig
else:
    print(f"ordered item{item_1}is not aviallable yet!")
another_order = input("do you want to add another item? (yes/no) =")
if another_order == "yes":
     item_2 = input("enter the name of second item =")
     if item_2 in menu:
        order_total+= menu[item_2]
        print(f"item {item_2} has been added to order")
else:
     print(f"ordered item{item_2}is not aviallable!")

print(f"the total amount of item to pay is {order_total}")
