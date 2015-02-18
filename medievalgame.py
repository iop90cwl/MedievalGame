print('Hello, and Welcome to "Quest for Gold"!')
playername = input('What is your name?: ')
print('',playername,'!' ' You are known through the land as a valiant and noble warrior, and you begin your quest for riches!\n')
print('Do you choose a Sword or a Shield? Enter 1 for a Sword and 2 for a Shield.')

#Choice Input
choice = input('Which will it be? ')

if choice == '1':
    print('\nYou chose a Sword.')

elif choice == '2':
    print('\nYou chose a Shield.')

else:
    print('Invalid. Restart the game.')

#Story Branch
direction = input('\nYou set out on your adventure. You come accross a fork in the path. Do you go left or right? 1 for left, 2 for right: ')

#First Path
if direction == '1':
    print('\nYou come accross a bowman!')
    fight = input('\nDo you run away(enter 1) or stay and fight?(enter 2).')
    if choice == '1' and fight == '2':
        print('\nUnfortunately, your sword cannot stop his arrows, and you are slain.')
        win = '0'
        halfwin = '0'
    elif choice == '1' and fight == '1':
        print('\nYou narrowly escape with your life and live to tell the tale to your malnourished children.')
        win = '0'
        halfwin = '1'
    elif choice == '2' and fight == '2':
        print('\nYour shield stops his arrows, and you raid his fortress. You retire comfortably with pounds and pounds of gold.')
        win = '0'
        halfwin = '0'
    elif choice == '2' and fight == '1':
        print('\nYou run away, but you always wonder what would\'ve happened if you\'d\'ve stayed and fought.')
        win = '1'
        halfwin = '1'
    else:
        print('\nYou messed up. Restart the game.')
        
#Second Path
if direction == '2':
    print('\nYou come accross an Ogre!')
    defend = input('Do you fight(enter 1) or defend yourself?(enter 2).')
    if choice == '1' and defend == '1':
        print('\nYou sink your sword into the Ogre and defeat him. You take all the gold from his lair and spend the rest of your days in luxury.')
        win = '1'
        halfwin = '0'
    elif choice == '1' and defend == '2':
        print('\nYou escape, but for the rest of your life you ponder what might have happened if you had fought and won.')
        win = '0'
        halfwin = '1'
    elif choice == '2' and defend == '1':
        print('\nYour shield is no match for the Ogre, and he bashes your head in.')
        win = '0'
        halfwn = '0'
    elif choice == '2' and defend == '2':
        print('\nYou barely escape, and come home emptyhanded, but alive.')
        win = '1'
        halfwin = '1'
    else:
        print('\nYou dun\' goofed! Restart the game.')

#Win/Lose
if win == '1' and halfwin != '1':
    print('\nCongratulations! You won,', playername)
    input('\nPress ENTER to quit.')
elif win == '0' and halfwin != '1':
    print('\nRest in Peace,', playername)
    input('\nPress ENTER to quit.')
elif halfwin == '1':
    print('Congrats,', playername,', you won, kind of.')
    input('\nPress ENTER to quit.')
