
import random

 #fortunes
fortune1 = 'You are going to die within 7 years.'
fortune2 = 'You are going to overdraw your account soon.'
fortune3 = 'You will win a beauty pageant in the near future.'
fortune4 = 'Stop buying lottery tickets because you are worth a million bucks.'
fortune5 = 'You will eventually be hit on by a computer program.'
fortune6 = 'The path to success is started by failures.'
fortune7 = 'Avoid going outside today, it may prove fatal.'
fortune8 = 'Consider choosing a new career path.'
fortune9 = 'Continue with the direction you are heading.'


print()
print()
print('================This is a Magic 8 Ball.================')
print()

input('Tell me your name and I will tell you your fortune.      ')

print()
print()

random_num = random.randint (1, 9)

if random_num == int(1):
    print(fortune1)
elif random_num == int(2):
    print(fortune2)
elif random_num == int(3):
    print(fortune3)
elif random_num == int(4):
    print(fortune4)
elif random_num == int(5):
    print(fortune5)
elif random_num == int(6):
    print(fortune6)
elif random_num == int(7):
    print(fortune7)
elif random_num == int(8):
    print(fortune8)
elif random_num == int(9):
    print(fortune9)


print()
print()
