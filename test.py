import random
randomEnemiesList = ['Demagorgan', 'Trogladite', 'Mindflayer', 'Demadog', 'Ogre', 'Troll', 'Dragon']

def randomEnemy(randomEnemiesList):
    randomNumber = random.randint(0,6)
    return randomEnemiesList[randomNumber]

enemy = randomEnemy(randomEnemiesList)

print('As you are walking briskly, a ', enemy,' approaches. You must decide to use your magic or your attack skills.')
