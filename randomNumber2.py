import random

print('This is a Random Number generator.')

randomInput= len(input('Give me information, and I will give you a random number.'))

randomNumber = random.randint(randomInput, 250)

def getAnswer():

      return randomNumber

finalAnswer = getAnswer()
print(finalAnswer)
