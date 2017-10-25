print('Welcome to Change Return. Please insert dollars and loose change.Please include 2 decimals for the small change.')
print('How many dollars and cents are you needing change for?')
initialBalance = round(float(input()), 2 ) * 100
numQuarters = initialBalance // 25
runTotal = initialBalance - (numQuarters * 25)
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
print('Thank you. Now keep the change you filthy animal!')
