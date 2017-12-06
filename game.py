''' This is a text based game that effect a user's character based upon user input. '''

import random
import sys

#Title sequence
print('')
print('')
print('              ============== Magical Journey Quest ==============')
print('')
print('')

#Dictionary of Character Traits
characterTraits = {
'name': '',
'characterType': '',
'HP': 100,
'magicPoints': '',
'attackPoints': ''}

#Game over function
def gameOver():
    print('      ------ GAME OVER ------',
    characterTraits['name'],
    'You fought bravely, but now you\'re dead.')
    return sys.exit()

#Confirm if the user wants to play
def start():
    print('Greetings warrior.  Are you ready to battle in Space Dungeon?')
    print()
    choice = input('Answer yes or no, warrior!                           ')
    if(choice == 'no'):
        print('Then flee coward!')
        sys.exit()
    else:
        print('Let\'s begin')

start()

#Beginning to define the character traits.
characterTraits['name'] = input('Welcome, please create your character\'s name.        ')
characterTraits['characterType'] = input('Alright warrior, ' + characterTraits['name'] + ', what is your character type?  ')

#Function to instruct user about the Magic Point and Attack Point value system.
def startInfo():
    print()
    print('The total amount of your Magic points will determine your attack points.')
    print('Magic Points plus Attack points will equal 100.')

startInfo()

#Magic Points requested
characterTraits['magicPoints'] = int(input('Now choose how many Magic points you would like.     '))

#Determining Attack Points
while(characterTraits['magicPoints'] >= 100):
    characterTraits['magicPoints'] = int(input('Please choose a valid amount, imbecile!'))

while(characterTraits['magicPoints'] <= 0):
    characterTraits['magicPoints'] = int(input('You can\'t be seriously condsidering a value less than 0!'))
else:
    print()
    print('Your magic points are ' + str(characterTraits['magicPoints']) + '.')
    characterTraits['attackPoints'] = 100 - characterTraits['magicPoints']

#Checking to see if the Profile is accurate
def accuracyOfProfile():
    print(characterTraits['name'] + ', you have chosen to be a ' + characterTraits['characterType'] + ' with ' + str(characterTraits['magicPoints']) + ' magic points, and ' + str(characterTraits['attackPoints']) + ' attack points.')
    accuracy = input('Does this information look accurate?                 ')
    if(accuracy == 'no'):
        print('Then you must master the computer before proceeding.')
        sys.exit()
    else:
        print()
        print('Let us begin your quest ' + characterTraits['name'] + '!')
        print()
        print('============================================================================')

accuracyOfProfile()

#Wise Man Character Introduced
def wiseMan():
    print()
    print('A wise man approaches and gives you some well-timed, wise advice.')
    print()
    print('Greetings warrior ' + characterTraits['name'] + '!')
    print('I know your name because I am wise.')
    print('On your quest you will meet many obstacles.')
    print('As you fight, your magic and attack points will diminish.')
    print('Your total health points equals 100 & this will decrease in battle as well.')
    print('Now go and do what you set out to do!')

wiseMan()

#Character Reaction
print()
print('You walk in a hurry, he was creeping you out anyway.')
print()

#List of Enemies
randomEnemiesList = ['Demagorgan', 'Trogladite', 'Mindflayer', 'Demadog', 'Ogre', 'Troll', 'Dragon']

#Lis of Possible Goody Values
randomGoodies = [int(characterTraits.update(['HP'] + 10),
int(characterTraits.update(['magicPoints'] + 10),
int(characterTraits.update(['attackPoints'] + 10)]

#Enemy function
def randomEnemy(randomEnemiesList):
    randomNumber = int(random.randint(0,6))
    return randomEnemiesList[randomNumber]
enemy = randomEnemy(randomEnemiesList)


#Goody bag functions
def randomSelection(randomGoodies):
    randomNumber2 = int(random.randint(0,2))
    randomGoodies[randomNumber2]
    print('Your HP is now ' + str(characterTraits['HP']) + '.',
    'Your magic is now ' + str(characterTraits['magicPoints']) + '.',
    'Your attack is now ' + str(characterTraits['attackPoints']) + '.')


#Initial HP
characterTraits['HP'] = int(100)

#Calculating points used in battle and determining HP based upon those values

def newHealth():
    return random.randint(characterTraits['HP'] - (200 - int(characterTraits['magicPoints'] + characterTraits['attackPoints'])), characterTraits['HP'])


fightingStyle = ['magic', 'attack']

#Defining different fighting styles
def offensiveManeuvers():
    fightingStyle = input('Will you use magic or attack?')
    if(fightingStyle == 'attack'):
        while(characterTraits['attackPoints'] > 20):
            print('You have used 10 attck points. You now have  ' + str(characterTraits['attackPoints']) + ' attack points.')
            characterTraits['attackPoints'] -=10
            return newHealth()
            if characterTraits['HP'] > 0:
                print('Your total health is now' + str(characterTraits['HP']) + '.')
            elif characterTraits['HP'] <= 0:
                return gameOver()
        else:
            print('You have defeated the' + enemy + '. Well done, warrior!')
    elif(fightingStyle == 'magic'):
        while(characterTraits['magicPoints'] > 20):
            print('You have used 10 magic points. You now have '+ str(characterTraits['magicPoints']) + ' magic points.')
            characterTraits['magicPoints'] -=10
            return newHealth()
            if characterTraits['HP'] > 0:
                print('Your total health is now' + str(characterTraits['HP']) + '.')
            elif characterTraits['HP'] <= 0:
                return gameOver()
        else:
            print('You have defeated the ', enemy, '. Well done, warrior!')
            print('Your total health is now' + str(characterTraits['HP']) + '.')
    else:
        print('Please input a valid fighting style.')




#Introducing simple left and right choice option for the user.


def direction():
    randomNumber3 = random.randint(0,100)
    if choice == 'left':
        if(randomNumber3) <= 50:
            return randomSelection(randomGoodies)
        else:
            print('As you are walking briskly, a ', enemy,' approaches.')
            return offensiveManeuvers()
            return newHealth()
    elif choice == 'right':
        if(randomNumber3) <= 50:
            return randomSelection(randomGoodies)
        else:
            print('As you are walking briskly, a ', enemy,' approaches.')
            return offensiveManeuvers()
            return newHealth()
    else:
        print('Seriously? Do you even want to play?')


choice = input('You come to a forked path, would you like to go left or right?')

direction()

choice = input('You come to a forked path, would you like to go left or right?')

direction()

choice = input('You come to a forked path, would you like to go left or right?')

direction()
