username=input("Enter Username: ")
password=input("Enter Password: ")
balance=5000
i=0
j=True
while(i<4):
    if (username=='niha') and (password=='1234'):
        while True:
            choose=input("Type 1 for adding money, type 2 for debiting money: ")
            if (choose=='1'):
                add=int(input("Enter the amount to be added: "))
                availbal=(balance+add)
                print("Available balance : ",availbal)
                balance=balance+add
                continue1=input("Do you wish to continue (y/n)? ")
                if(continue1=='y'):
                    continue
                if(continue1=='n'):
                    end1=input("Thanks, have a nice day")       
            if(choose=='2'):
                withdraw=int(input("Enter withdrawal amount "))
                if (withdraw>balance):
                    print("Insufficient Funds")
                    break
                if(withdraw<=balance):
                    balance=balance-withdraw
                    print("Available Balance: ",balance)
                    continue1=input("Do you wish to continue (y/n)? ")
                    if(continue1=='y'):
                        continue
                    if(continue1=='n'):
                        end1=input("Thanks, have a nice day")
    else:
        print("Incorrect Password, try again")
        username=input("Enter Username: ")
        password=input("Enter Password: ")
        i+=1
print("Number of attempts completed, invalid user")
