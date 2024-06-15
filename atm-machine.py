# Task-1 create atm card like atm machine or bank where we go and withdraw and deposite and ceck transition 
# this tere method do in thi program

import time
print("Enter your Card Number..")

history = []
username= ['Misbah',"Maadeha"]
user_paword ={
    'Misbah':123,
    'Maadeha':456

}
amount=5000

def deposite():
    deposit_amount = int(input("Enter a Amount That you Deposit in your Account: "))
    global amount
    amount = amount +deposit_amount
    print("Know your curent blace is: ",amount)
    history.append({'Deposite':deposit_amount})



    
def withdraw():
    withdraw_amount = int(input("Enter a Withdraw amount: "))
    global amount
    if withdraw_amount < amount:
        amount -=withdraw_amount
    else:
        print("Enter a valid amount..")
        withdraw()
    history.append({'withdraw':withdraw_amount})

    
def transition():
    for i ,hist in enumerate(history):
        if "Deposite" in hist:
            print(f"Transiction-{i+1} : deposite -> {hist['Deposite']}")
        elif 'withdraw' in hist:
            print(f"Transiction-{i+1} : withdraw -> {hist['withdraw']}")
        else:
            print("You Have Not Any Transiction :)")


def menu_mean():
    choose = int(input("""1.Deposite
2.withdraw
3.Transiction
4.exit
Please Enter Your Choice: 
"""))
    if choose == 1:
        deposite()
    elif choose ==2:
        withdraw()
    elif choose == 3:
        transition()
    elif choose == 4:
        exit()



num =0
while num<3:
    pas = 123
    user = input("Enter ypur user Name: ")
    password =int(input("Enter your password of your acount: "))
    if user in username and user_paword[user]==password:
        while True:
            menu_mean()
    else:
        print(f"Sorry your password is incorrect :(  please try Again \nYou have only {num} chance")
    num+=1
else:
    print("You Try 3 time Your Acount Know block..")


    