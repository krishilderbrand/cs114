''' This program gives out a fortune based upon a random number. '''

import random

import sys

def exit():
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()


fortunes = ['No habla inlges.',
'Why certainly!',
'Probably not?...',
'Outlook is not good.',
'Of course.',
'You should consider not asking a computer so many questions.',
'Ask me later, and this isn\'t because I don\'t know right now.',
'No.',
'Yes.',
'Chances seem pretty good on this one.',
'I could see it going either way.',
'You should have consulted a PC.',
'I\'m positive that it will happen.',
'Indubitably!',
'Unfortunately no.',]

print()
print('             ===========The Amazing All knowing Magic 8 Ball===========')
print()
print()

def getAnswer(fortunes):
   randomNumber = random.randint(0,14)
   return(fortunes[randomNumber])


def main():
   print()
   while getAnswer(fortunes) != True:
       print('I am a magic 8 Ball that answers yes or no questions.')
       question = input('Type what you would like to ask.        ')
       while len(question) <= int(7):
           print('Type a valid question!')
           break
       else:
          print()
          print(getAnswer(fortunes))
          print()


main()
