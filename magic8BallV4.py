''' This program gives out a fortune based upon a random number. '''

import random

import sys

# List of fortunes
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

# Title sequence
print()
print('             ===========The Amazing All-knowing Magic 8 Ball===========')
print()
print('                          (Type exit if you are finished)')
print()
print()

# Obtaining a random selection of fortune.
def getAnswer(fortunes):
   randomNumber = random.randint(0,14)
   return(fortunes[randomNumber])

# Function that asks for user input of what they would like to know.
# Question must be more than 7 characters
# User can type exit to exit program
def main():
   print()
   while getAnswer(fortunes) != True:
       print('I am a magic 8 Ball that answers yes or no questions.')
       question = input('Type what you would like to ask.        ')
       if question == 'exit':
           sys.exit()
       elif len(question) <= 7:
           print()
           print('Input a valid question!')
           print()

       else:
           print()
           print(getAnswer(fortunes))
           print()



main()
