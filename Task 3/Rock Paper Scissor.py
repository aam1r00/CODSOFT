print('Welcome to Rock-Paper-Scissors Game!!')
while True:
    user_choice = input('Choose your option(rock, paper, scissor): ').lower()
    choices = ['rock','paper','scissor']
    x = 'You lose'
    y = 'You win'
    import random
    comp_choice = random.choice(choices)
    print(f"Computer choose: {comp_choice}")
    if user_choice not in choices:
        print('Invalid choice.')
    elif (user_choice == 'rock' and comp_choice == 'paper'):
        print('Result:',x)
    elif (user_choice == 'paper' and comp_choice == 'scissor'):
        print('Result:',x)
    elif (user_choice == 'scissor' and comp_choice == 'paper'):
        print('Result:',x)
    elif (user_choice == comp_choice):
        print('Result:',"It's a Tie")
    else:
        print('Result:',y)
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        continue
    elif play_again == 'no':
        break
    else:
        print('Invalid choice.')
        break
print('Thank You for playing')
