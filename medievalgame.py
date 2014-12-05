print('Hello, and Welcome to "QuestGame"!')
playername = input('What is your name?: ')
print('Your name is', playername,'\n')
print('Do you choose a Sword or a Shield? Press 1 for a Sword and 2 for a Shield.')

choice = input('Which will it be: ')

if choice == '1':
    print('\nYou chose a Sword.')

elif choice == '2':
    print('You chose a Shield.')

else:
    print('Invalid.')
        
print('\nMore to come soon!')
