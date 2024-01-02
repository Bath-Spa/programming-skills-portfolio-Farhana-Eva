def display_menu():
    print("Welcome to the Vending Machine!")
    print("1.7Up-AED 2")
    print("2.Pepsi-AED 2.50")
    print("3.Sprite-AED 2")
    print("4.Mirinda-AED 2")
    print("5.Mr.Krisps-AED 1.50")
    print("6.Super Ring-AED 1")
    print("7.Salad-AED 2")
    print("8.Bugles-AED 17")
    print("9.Exit")

def make_selection():
    choice = int(input("Enter Your Selection(1-9):"))
    if choice==1:
        return"7Up"
    elif choice==2:
        return"Pepsi"
    elif choice==3:
        return"Sprite"
    elif choice==4:
        return"Mirinda"
    elif choice==5:
        return"Mr.Krisps"
    elif choice==6:
        return"Super Ring"
    elif choice==7:
        return"Salad"
    elif choice==8:
        return"Bugles"
    elif choice==9:
        return"Exit"
    else:
        print("Invalid selection.please try again")
        return make_selection()

def process_payment(item):
    print("selected item:",item)
    payment=float(input("Enter payment amount:"))
    price=0.0
    if item=="7Up"or item=="Salad"or item=="Sprite" or item=="Mirinda":
        price=2
    elif item=="Pepsi":
        price=2.50
    elif item=="Mr.Krisps":
        price=1.50
    elif item=="Super Ring":
        price=1
    elif item=="Bugles":
        price=17
    if payment>=price:
        change=payment-price
        print("payment successful!here's your change:AED",change)
    else:
        print("Insufficient payment.please try again.")
        process_payment(item)

def run_vending_machine():
    while True:
        display_menu()
        item = make_selection()
        if item == "Exit":
            print("Thank you for using the Vending Machine!")
            break
        else:
            process_payment(item)

run_vending_machine()


