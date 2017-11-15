
''' This program gives out a fortune based upon a random number. '''

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'No habla inlges.'
    elif answerNumber == 2:
        return 'Why certainly!.'
    elif answerNumber == 3:
        return 'Probably not?...'
    elif answerNumber == 4:
        return 'Outlook is not good.'
    elif answerNumber == 5:
        return 'Of course.'
    elif answerNumber == 6:
        return 'You should have consulted a PC.'
    elif answerNumber == 7:
        return 'It doesn\'t matter, computers will enslave you anyways.'
    elif answerNumber == 8:
        return 'No.'
    elif answerNumber == 9:
        return 'Yes.'


def main():
    print()
    print('I am a magic 8 Ball that answers yes or no questions.')
    input('Type what you would like to ask.')

    r = random.randint(1,9)
    fortune = getAnswer(r)
    print(fortune)

main()
