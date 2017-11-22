''' This is a game that defines values based upon user input. '''

import random

print('')
print('')
print('              ==============Space Dungeon==============')
print('')
print('')


print('Greetings warrior.  Are you ready to battle in Space Dungeon?')
print()
choice = input('Answer yes or no, warrior!                           ')
if(choice == 'no'):
    print('Then flee coward!')
else:
    name = input('Welcome, please create your character\'s name.        ')
    characterType = input('Alright warrior, ' + str(name) + ', what is your character type?  ')

print()
print('The total amount of your Magic points will determine your attack points.')
print('Magic Points plus Attack points will equal 100.')
magicPoints = int(input('Now choose how many Magic points you would like.     '))

while(magicPoints >= 100):
    magicPoints = int(input('Please choose a valid amount, imbecile!'))

while(magicPoints <= 0):
    magicPoints = int(input('You can\'t be seriously condsidering a value less than 0!'))
else:
    print()
    print('Your magic points are ' + str(magicPoints) + '.')
    attackPoints = 100 - magicPoints

def accuracyOfProfile():
    print(name + ', you have chosen to be a ' + characterType + ' with ' + str(magicPoints) + ' magic points, and ' + str(attackPoints) + ' attack points.')
    accuracy = input('Does this information look accurate?                 ')
    if(accuracy == 'no'):
        print('Then you must master the computer before proceeding.')
    else:
        print()
        print('Let us begin your quest ' + name + '!')
        print()
        print('==========================================')
accuracyOfProfile()

print()
print('A wise man approaches and gives you some well-timed, wise advice.')
print()
print('Greetings warrior ' + name + '!')
print('I know your name because I am wise.')
print('On your quest you will meet many obstacles.')
print('As you fight the evils of this universe your magic and attack points will diminish.')
print('Your total health points equals 100 and this will diminish in battle as well.')
print('Now go and do what you set out to do!')

print()
print('You walk in a hurry, he was creeping you out anyway.')
print()

totalHealth = int(100)

pointsUsed = int(attackPoints + magicPoints)
newHealth = random.randint((totalHealth - (200 - pointsUsed)), totalHealth)




randomEnemiesList = ['Demagorgan', 'Trogladite', 'Mindflayer', 'Demadog', 'Ogre', 'Troll', 'Dragon']

def randomEnemy(randomEnemiesList):
    randomNumber = random.randint(0,6)
    return randomEnemiesList[randomNumber]

enemy1 = randomEnemy(randomEnemiesList)

print('As you are walking briskly, a ', enemy1,' approaches. You must decide to use your magic or your attack skills.')

fightingStyle = input('Would you like to use magic or attack?                     ')

if(fightingStyle == 'attack'):
    while(attackPoints > 20):
        print('You have used 10 attck points. You now have  ', attackPoints, ' attack points.')
        attackPoints -=10
    else:
        print('You have defeated the demagorgan. Well done, warrior!')


elif(fightingStyle == 'magic'):
    while(magicPoints > 20):
        print('You have used 10 magic points. You now have ', magicPoints, ' magic points.')
        magicPoints -=10
    else:
        print('You have defeated the ', enemy1, '. Well done, warrior!')

else:
    print('Please input a valid fighting style.')

if totalHealth > 0:
    print('Your total health is now', newHealth, '.')
elif totalHealth <= 0:
    print('You are dead!')


newHealth = random.randint((totalHealth - (200 - pointsUsed)), newHealth)

enemy2 = randomEnemy(randomEnemiesList)

print('You limp away from battle, a ', enemy2,' approaches. You must decide to use your magic or your attack skills.')

fightingStyle = input('Would you like to use magic or attack?                   ')

if(fightingStyle == 'attack'):
    while(attackPoints > 10):
        print('You have used 10 attck points. You now have  ', attackPoints, ' attack points.')
        attackPoints -=10
    else:
        print('You have defeated the demagorgan. Well done, warrior!')


elif(fightingStyle == 'magic'):
    while(magicPoints > 10):
        print('You have used 10 magic points. You now have ', magicPoints, ' magic points.')
        magicPoints -=10
    else:
        print('You have defeated the ', enemy2, '. Well done, warrior!')

else:
    print('Please input a valid fighting style.')


if totalHealth > 0:
    print('Your total health is now', newHealth, '.')
elif totalHealth <= 0:
    print('You are dead!')
