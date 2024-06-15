import UDF

while True:
    print("*"*50)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Pattern")
    print("7. Exit")
    print("*"*50)

    choice=int(input("Enter Your Choice : "))

    if choice==1:
        a=int(input("Enter Value : "))
        UDF.oddeven(a)
        print("*"*50)
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.maxoftwo(a,b)
        print("*"*50)
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.maxofthree(a,b,c)
        print("*"*50)
    elif choice==4:
        a=int(input("Enter Value : "))
        UDF.fibonacci(a)
        print("*"*50)
    elif choice==5:
        a=int(input("Enter Value : "))
        UDF.prime(a)
        print("*"*50)
    elif choice==6:
        a=int(input("Enter Value : "))
        UDF.pattern(a)
        print("*"*50)
    elif choice==7:
        print("Thank You For Using Our Services.")
        print("*"*50)
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*"*50)
        
        
        
