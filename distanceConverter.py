


print('=======Welcome to the amazing Distance Converter!=======')

print()


distance = float(input('Please enter the distance.   '))
units = input('Please input the unit of measurement (miles, kilometers, feet, meters.   ')
targetUnits = input('Please input the measurement you would like it converted to (miles, kilometers, feet, meters).   ')








milesToKilometers = float(distance / 1.60934)
milesToFeet = float(distance * 5280)
milesToMeters = float(distance * 1609.34)
kilometersToMiles = float(distance * 1.60934)
kilometersToFeet = float(distance / 3280.84)
kilometersToMeters = float(distance / 1000)
feetToMiles = float(distance / 5280)
feetToKilometers = float(distance * 3280.84)
feetToMeters = float(distance * 3.28084)
metersToKilometers = float(distance * 1000)
metersToMiles = float(distance * 1609.34)
metersToFeet = float(distance/ 3.28084)




if units == 'miles':
    if targetUnits == 'kilometers':
        print('You have ' + str(milesToKilometers) + ' kilometers.')
    elif targetUnits == 'feet':
        print('You have ' + str(milesToFeet) + ' feet.')
    elif targetUnits == 'meters':
        print('You have ' + str(milesToMeters) + ' meters.')
elif units == 'kilometers':
    if targetUnits == 'miles':
        print('You have ' + str(kilometersToMiles) + ' miles.')
    elif targetUnits == 'feet':
        print('You have ' + str(kilometersToFeet) + ' feet.')
    elif targetUnits == 'meters':
        print('You have ' + str(kilometersToMeters) + ' meters.')
elif units == 'feet':
    if targetUnits == 'miles':
        print('You have ' + str(feetToMiles) + ' miles.')
    elif targetUnits == 'kilometers':
        print('You have ' + str(feetToKilometers) + ' kilometers.')
    elif targetUnits == 'meters':
        print('You have ' + str(feetToMeters) + ' meters.')
elif units == 'meters':
    if targetUnits == 'miles':
        print('You have ' + str(metersToMiles) + ' miles.')
    elif targetUnits == 'feet':
        print('You have ' + str(metersToFeet) + ' feet.')
    elif targetUnits == 'kilometers':
        print('You have ' + str(metersToKilometers) + ' kilometers.')
