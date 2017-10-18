print('Greetings warrior.  Art thou ready to battle in Dungeon Crawler?')
print('Answer yes or no, warrior!')
choice = input()
if(choice == 'no'):
  print('Then flee coward!')
else:
  print('Welcome, please create your character\'s name.')
name = input()
print('Alright warrior, ' + name + ', what is thy character type?')
characterType = input()
print('Now choose how many Magic points thou would like. The total amount of your Magic points will determine thy attack points. Magic Points plus Attack points will equal 100.')
magicPoints = int(input())
while(magicPoints >= 100):
    print('Please choose a valid amount, imbecile!')
    magicPoints = int(input())
while(magicPoints <= 0):
    print('Thou can\'t be seriously condsidering a value less than 0!')
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
print('Death monster approaches. You must have 80 magic points or more to defeat.')
if(magicPoints < 80):
    print('You\'re dead!')
else:
    print('Well done' + name + ' you defeated the Death monster!')
