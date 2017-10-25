width = int(input('What is the width of your wall in feet? '))
height = int(input('What is the the height of your wall in feet? '))
price_per_gallon = float(input('What is the cost of a gallon of paint? '))
coats_of_paint = round(float(input('How many coats of paint will you apply? ')) , 2)
gallons_of_paint = width * height // 400
cost = round((gallons_of_paint * coats_of_paint * price_per_gallon), -2)
print('The total cost is going to be ' + str(cost) + '.')
