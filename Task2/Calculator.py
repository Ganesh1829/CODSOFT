def add():
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    print("The sum is")
    c=a+b
    return c

def sub():
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    print("The difference is")
    c=a-b
    return c
def mul():
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    print("The product is")
    c=a*b
    return c
def div():
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    print("the quotient is")
    c=a/b
    return c
while(1):
    print("Enter 1.Addition 2.Subtraction 3.Multiplication 4.Division")
    choice=int(input("enter choice"))
    if choice == 1:
            res =add()
            print(res)
    elif choice == 2:
            res = sub()
            print(res)
    elif choice == 3:
            res = mul()
            print(res)
    elif choice == 4:
            res = div()
            print(res)
    else:
        print("INvalid!!!")



