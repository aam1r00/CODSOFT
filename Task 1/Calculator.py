def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y!= 0:
        return x/y
    else:
        return "Cannot Divide By Zero"
while True:
    a = "WELCOME TO SIMPLE CALCULATOR"
    b = a.center(50,"-")
    print(b,"\n")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice = int(input("Enter Your Choice(1-4) : "))
    if choice==1:
        first_num = float(input("Please Enter Your First Number : "))
        second_num = float(input("Please Enter Your Second Number : "))
        print(first_num,"+",second_num,"=",add(first_num,second_num),"\n")
        q = input("<--Press Enter-->")
        continue
    elif choice==2:
        first_num = float(input("Please Enter Your First Number : "))
        second_num = float(input("Please Enter Your Second Number : "))
        print(first_num,"-",second_num,"=",subtract(first_num,second_num),"\n")
        q = input("<--Press Enter-->")
        continue
    elif choice==3:
        first_num = float(input("Please Enter Your First Number : "))
        second_num = float(input("Please Enter Your Second Number : "))
        print(first_num,"x",second_num,"=",multiply(first_num,second_num),"\n")
        q = input("<--Press Enter-->")
        continue
    elif choice==4:
        first_num = float(input("Please Enter Your First Number : "))
        second_num = float(input("Please Enter Your Second Number : "))
        print(first_num,"/",second_num,"=",division(first_num,second_num),"\n")
        q = input("<--Press Enter-->")
        continue
    elif choice==5:
        break
    else:
        print("Invalid Choice. Please Try Again\n")
        q = input("<--Press Enter-->")
        continue
