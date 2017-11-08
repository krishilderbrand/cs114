
print('')
print('')
print('==============Space Dungeon==============')
print('')
print('')

print('Greetings warrior.  Are youready to battle in Space Dungeon?')
print('Answer yes or no, warrior!')
choice = input()
if(choice == 'no'):
  print('Then flee coward!')
else:
  print('Welcome, please create your character\'s name.')
name = input()
print('Alright warrior, ' + name + ', what is thy character type?')
characterType = input()
print('Now choose how many Magic points you would like. The total amount of your Magic points will determine your attack points. Magic Points plus Attack points will equal 100.')
magicPoints = int(input())
while(magicPoints >= 100):
    print('Please choose a valid amount, imbecile!')
    magicPoints = int(input())
while(magicPoints <= 0):
    print('You can\'t be seriously condsidering a value less than 0!')
    magicPoints = int(input())
else:
    print('Your magic points are ' , magicPoints, '.')
attackPoints = 100 - magicPoints
print(name + ', you have chosen to be a ' + characterType + ' with ' + str(magicPoints) + ' magic points, and ' + str(attackPoints) + ' attack points.')
print('Does this information look accurate?')
accuracy = input()
if(accuracy == 'no'):
    print('Then thou must master the computer before proceeding.')
else:
    print('Let us begin your quest ' + name + '!')

print()
print('A wise man approaches and gives you some well-timed, wise advice.')
print()
print('Greetings warrior ' + name + '!')
print('I know your name because I am wise.')
print('On your quest you will meet many obstacles.')
print('As you fight the evils of this universe your magic and attack points will diminish.')
print('Your total health points equals 100.')
print('Now go and do what you set out to do!')

print()
print()
print('You walk in a hurry, he was creeping you out anyway.')
print()
print()

totalHealth = int(100)

magicPointsUsed = magicPoints - 10
attackPointsUsed = attackPoints - 10
totalMagicPoints = magicPoints - magicPointsUsed
totalAttackPoints = attackPoints - attackPointsUsed



#while attackPoints > 0 == True:
#    print('You have ', attackPoints, ' attack points.')
#    attackPoints -=10

#for totalHealth in range(5):












totalPointsUsed = totalMagicPoints+ totalAttackPoints

print('As you are walking briskly, a demagorgan approaches. You must decide to use your magic or your attack skills.')

fightingStyle = input('You may choose to use magic or choose to use your attacking skills. Would you like to use magic or attack?')

while fightingStyle == 'attack':
    print(totalAttackPoints)

while fightingStyle == 'magic':
    print(totalMagicPoints, )
else:
    print('Please input a valid fighting style.')



magicPointsUsed = int(input('How many Magic Points would you like to use?'))
attackPointsUsed = int(input('How many Attack Points would you like to use?'))



while totalPointsUsed <= 45:
    input('Fight stronger. The demagorgan is going to kill you!') and print('You have ' + totalMagicPoints + ' and ' + totalAttackPoints + ' left.')
else:
    print('You have defeated the demagorgan!') and print('You have ' + totalMagicPoints + ' and ' + totalAttackPoints + ' left.')

print('Your total points used')
