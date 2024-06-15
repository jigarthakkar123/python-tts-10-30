class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",str(self.acno)," Is Opened With ",str(self.balance)," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Insufficient Balance")
    def checkBalance(self):
        print("Your Current Balance Is : ",self.balance)

        
b1=Bank()
print("*"*60)
acno=int(input("Enter Account Number : "))
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial Balance : "))
print("*"*60)
b1.openAccount(acno,cname,balance)
print("*"*60)
while True:

    print("*"*60)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*60)
    choice=int(input("Enter Your Choice : "))
    print("*"*60)
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*60)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*60)
    elif choice==3:
        b1.checkBalance()
        print("*"*60)
    elif choice==4:
        print("Thank You For Using Our Services.")
        print("*"*60)
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*"*60)
        
