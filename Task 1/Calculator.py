def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot Divide By Zero"

while True:
    print("-" * 50)
    print("WELCOME TO SIMPLE CALCULATOR".center(50, "-"))
    print("-" * 50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-" * 50)
    
    choice = input("Enter Your Choice (1-5): ")

    if choice == '5':
        print("Thank you for using the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            first_num = float(input("Please Enter Your First Number: "))
            second_num = float(input("Please Enter Your Second Number: "))

            if choice == '1':
                print(f"{first_num} + {second_num} = {add(first_num, second_num)}")
            elif choice == '2':
                print(f"{first_num} - {second_num} = {subtract(first_num, second_num)}")
            elif choice == '3':
                print(f"{first_num} x {second_num} = {multiply(first_num, second_num)}")
            elif choice == '4':
                result = division(first_num, second_num)
                if isinstance(result, str):
                    print(f"{first_num} / {second_num} = {result}")
                else:
                    print(f"{first_num} / {second_num} = {result}")

            input("<-- Press Enter to continue -->")
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    else:
        print("Invalid Choice. Please Try Again\n")
        input("<-- Press Enter to continue -->")
