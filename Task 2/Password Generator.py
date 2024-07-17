print("-------------Password Generator--------------")
import random
import string
weak_password = string.ascii_lowercase
moderate_password = string.ascii_letters + string.digits
strong_password = string.ascii_letters + string.digits + string.punctuation
while True:
    password_length = int(input("Enter the length  of the password: "))
    user_choice = input("Enter your choice(weak,moderate,strong): ").lower()
    if user_choice == 'weak':
        password = ''.join(random.choices(weak_password,k=password_length))
        print("Password Generated:",password)
    elif user_choice == 'moderate':
        password = ''.join(random.choices(moderate_password,k=password_length))
        print("Password Generated:",password)
    elif user_choice == 'strong':
        password = ''.join(random.choices(strong_password,k=password_length))
        print("Password Generated:",password)
    else:
        print("Invalid choice. Please try again")
    new_password = input('Do you want to generate new password? (yes/no): ').lower()
    if new_password == 'yes':
        continue
    elif new_password == 'no':
        break
    else:
        print('Invalid choice')
        break
print("Thank You for using")
