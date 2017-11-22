
''' This program gives out a fortune based upon a random number. '''

import random

fortunes = ['No habla inlges.',
'Why certainly!.',
'Probably not?...',
'Outlook is not good.',
'Of course.',
'You should have consulted a PC.',
'It doesn\'t matter, computers will enslave you anyways.',
'No.',
'Yes.'
]

def getAnswer(fortunes):
    randomNumber = random.randint(0,9)
    return(fortunes[randomNumber])

def main():
    print()
    print('I am a magic 8 Ball that answers yes or no questions.')
    input('Type what you would like to ask.        ')

    fortune = getAnswer(fortunes)
    print(fortune)

main()
