print()
print()
print('====Welcome to Change Return. Please insert dollars and loose change.====')
print()
print('How many dollars and cents are you needing change for?')
print('(Please include 2 decimals for the small change)')
print()
initialBalance = round(float(input()), 2 ) * 100
numQuarters = int(initialBalance // 25)
runTotal = int(initialBalance - (numQuarters * 25))
numDimes = runTotal // 10
runTotal = runTotal - (numDimes * 10)
numNickels = runTotal // 5
runTotal = runTotal - (numNickels * 5)
numPennies = runTotal // 1
runTotal = runTotal - (numPennies * 1)
print('Here is your change.')
print('Quarters: ' , numQuarters)
print('Dimes: ' , numDimes)
print('Nickels: ' , numNickels)
print('Pennies: ', numPennies)
print()
print('Thank you. Now keep the change you filthy animal!')
print()
