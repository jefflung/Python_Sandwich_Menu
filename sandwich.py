import string

def orderSandwich():
    ask_order = input("Which sandwich would you like? ")
    cap_ask = string.capwords(ask_order)
    
    with open("menu.txt", mode="r") as menu:
        found = False
        for line in menu:
            #remove space between words to compare
            if cap_ask.strip() == line.strip():
                print("Yes, we have",cap_ask,"sandwich in our menu.")
                #only matched item in menu showing Yes answer
                found = True
        if not found:
            print("Sorry, we don't have",cap_ask,"sandwich in our menu.")
                
orderSandwich()
