print('Hello, and Welcome to "QuestGame"!')
playername = input('What is your name?: ')
print('Your name is', playername,'\n')
print('Do you choose a Sword or a Shield? Press 1 for a Sword and 2 for a Shield.')

choice = input('Which will it be: ')

if choice == '1':
    print('\nYou chose a Sword.')

elif choice == '2':
    print('\nYou chose a Shield.')

else:
    print('Invalid.')

direction = input('\nYou set out on your adventure. You come accross a fork in the path. Do you go left or right? 1 for left, 2 for right: ')

if direction == '1':
    print('\nYou come accross a bowman!')
    if choice == '1':
        print('\nUnfortunately, your sword cannot stop his arrows, and you are slain.')
        win = '0'
    elif choice == '2':
        print('\nYour shield stops his arrows, and you raid his fortress. You retire comfortably with pounds and pounds of gold.')
        win = '1'
if direction == '2':
    print('\nYou come accross an Ogre!')
    if choice == '1':
        print('\nYou sink your sword into the Ogre and defeat him. You take all the gold from his lair and spend the rest of your days in luxury.')
        win = '1'
    elif choice == '2':
        print('\nUnfortunately, the Ogre smashes through your shield and you are slain.')
        win = '0'
if win == '1':
    print('\nCongratulations! You won,', playername)
elif win == '0':
    print('\nRest in Peace,', playername)
