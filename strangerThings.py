import random
import sys

"""text based game where user makes decisions which affect a series of
encounters with 'enemies'"""


#Title sequence
print('')
print('')
print('                      ============== STRANGER THINGS==============')
print('                                   Chapter 1 - Hawkins')
print()
print('                           *********WARNING! SPOILERS!!!********')
print('')
input('Input any requested information. Press enter through instructions and dialogue.')

#Dictionary of Character Traits
player = {
'name': '',
'HP': 100,
'magicPoints': 0,
'attackPoints': 0}

#Confirm if the user wants to play
def start():
    print()
    print('Greetings random citizen of Hawkins. Are you ready to play?')
    print()
    choice = input('Answer yes or no.                                   ')
    if(choice == 'no'):
        print('Then flee coward!')
        sys.exit()
    else:
        print('Let\'s begin.')

start()        

#Beginning to define the character traits.
player['name'] = input('Please create your character\'s name.                ')

#Function to instruct user about the Magic Point and Attack Point value system.
def startInfo():
    print()
    print('Magic points will determine your attack points.')
    print('Magic points plus Attack points can only equal 100 in total.')

startInfo()

#Magic Points requested
player['magicPoints'] = int(input('Now choose how many Magic points you would like.     '))

#Determining Attack Points
while(player['magicPoints'] >= 100):
    player['magicPoints'] = int(input('Please choose a valid amount, imbecile!'))

while(player['magicPoints'] <= 0):
    player['magicPoints'] = int(input('You can\'t be seriously condsidering a value less than 0!'))
else:
    print()
    print('Your magic points are now ' + str(player['magicPoints']) + '.')
    print()
    player['attackPoints'] = 100 - player['magicPoints']
    
#Checking to see if the Profile is accurate
def accuracyOfProfile():
    print(player['name']+ ' will have ' + str(player['magicPoints']) + ' magic points, and ' + str(player['attackPoints']) + ' attack points.')
    accuracy = input('Does this information look accurate?                 ')
    if(accuracy == 'no'):
        print('Then you must master the computer before proceeding.')
        sys.exit()
    else:
        print()
        input('Let\'s finally begin this, ' + player['name'] + '!')
        print()
        print('             ===================Chapter 2 The Mad Scientist=================')

accuracyOfProfile()
 

#Scientis Character Introduced
def scientist():
    print()
    print('A Hawkins Lab Scientist approaches and gives you some well-timed, advice.')
    input('He whispers to you.')
    input(' Hello ' + player['name'] + '.')
    input(' I know your name because, as you are aware, we\'ve been monitoring you.')
    input(' Another dimension has opened up, which we are calling the Upside Down.')
    input(' 2 kids, Barb and Will, are lost in the Upside Down.')
    input(' Only you can save them and close the portal to the Upside Down.')
    input(' On your quest you will meet many obstacles.')
    input(' Your total health points equals 100 & this will decrease in battle as well.')
    input(' Now go and save us all!')

scientist()

#Character Reaction
print()
input('You walk in a hurry, he was creeping you out anyway.')
print()

print('             ===================Chapter 3 The Upside Down=================')

input('It\'s late at night.')
input('You decide to check out Hawkins High School for any anomolies.')
input('You break into the school.')
input('Everything is dark inside.')
input('You call out for Will and Barb.')
input('As you are searching the abandoned halls you hear a noise.')
input('The lights start to flicker rapidly.')
input('Just then something comes out of the wall towards you.')


enemy1 = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Mind Flayer'
}

enemy2 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Demagorgan'
}

enemy3 = {
'HP': 30,
'attack': 30,
'defense': 30,
'name': 'Demadog'
}

enemy4 = {
'HP': 25,
'attack': 25,
'defense': 25,
'name': 'Trogladite'
}

enemy5 = {
'HP': 15,
'attack': 15,
'defense': 15,
'name': 'Vines from the Upside Down.'
}


def game_over(player):
    print("GAME OVER -- ", player['name'], "You have died and become forgotten like Barb.")
    return sys.exit()


def get_item(player):
    item_list = ["a Milky Way", "Ego Waffles", "Halloween Candy", "Karen Wheeler's Casserole"]

    print("You find ", item_list[random.randint(0, 3)], ".", "Your health increased by ",
    (abs(player['HP'] - 100)), "HP.")
    player['HP'] += (abs(player['HP'] - 100))
    return player


def attack(opponent):
    rand_damage = random.randint(5, 30)
    opponent['HP'] -= rand_damage
    print(rand_damage, " damage!")
    return opponent


def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        input()
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack(oppo1)
            input()
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print(player['name'], 'HP: ', oppo1['HP'])
    print(oppo2['name'], ' HP: ', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 70:
        fight(player, opponent)
        # if player['HP'] <= 0:
        #     return game_over(player)
        print()
        input('Press enter to continue')
        print()
    elif player['HP'] < 30:
        get_item(player)
    elif opponent['name'] == 'Mind Flayer':
        fight(player, opponent)
        # return player
    else:
        get_item(player)
        print()
        input('Press enter to continue')
        print()

def randomEnemy():
    enemyNumber = random.randint(1,5)
    if enemyNumber == 1:
        return enemy1
    elif enemyNumber == 2:
        return enemy2
    elif enemyNumber == 3:
        return enemy3
    elif enemyNumber == 4:
        return enemy4
    else:
        return enemy5
    



"""There are multiple encounters, either against an enemy or finding an item"""


def main():
    # fight(player, enemy1)

    # get_item(player)
    print()
    print('encounter 1...\n\n')
    encounter(player, randomEnemy())
    input('You are pulled into the Upside Down.')
    input('Particles float in the air')
    input('It is a cold, dark, and grungy version of Hawkins.')
    print()
    print('encounter 2...\n\n')
    encounter(player, randomEnemy())
    print()
    print('encounter 3...\n\n')
    encounter(player, enemy1)
    print()
    print("You have sealed the Upside Down and saved Will. Barb still dies, but you have saved the rest of Hawkins! -- WINNER", player['name'], " HP: ", player['HP'])
    print()



if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
