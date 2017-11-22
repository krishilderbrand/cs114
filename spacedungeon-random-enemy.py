import random

randomEnemies = ['Demagorgan', 'Trogladite', 'Mindflayer', 'Demadog', 'Ogre', 'Troll', 'Dragon', 'Nazgul']

def randomEnemy(randomEnemies):
    randomNumber = random.randint(0,7)
    print(randomEnemies[randomNumber])

randomEnemy(randomEnemies)
