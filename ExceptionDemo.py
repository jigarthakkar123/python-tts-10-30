print("Start Code")

try:
    a=int(input("Enter Value : "))
    b=int(input("Enter Value : "))

    c=a/b
    print("Division : ",c)
except Exception as e:
    print("Exception Caught : ",e)
print("End Code")
