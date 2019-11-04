# Prompt the user for his name using the input function.
# Upon receiving his name, you will say hello to him
"""name = input('What is your name?')
print('Hello' + str(name) + '!')

#Same as the first exercise, but this time 
#print the user's name in ALL CAPS, and also tell 
#them the number of letters in their name. Example session:
name = input('WHAT IS YOUR NAME? ')
name_length = len(name)
print('HELLO, ' + str(name.upper()) + '! YOUR NAME HAS ' + str(len(name)) + ' LETTERS IN IT!')

#Prompt the user for the missing words to a
#Madlib sentenceusing the input function. 
#You will make up your own Madlib sentence!
print('Please fill in the blanks below.')
print("___name___'s favorite coding langauge is ___language___.")
name = input('What is name? ')
language = input('What is language? ')
print(str(name) + "'s favorite coding language is " + str(language))

#The user will enter a number between 0 to 6 inclusive. 
#Given this number, print a day of the week. 
#0 for Sunday, 1 for Monday, 2 for Tuesday, and so on.
while True:
    day = int(input('Day (0-6)? '))
    if day == 0:
        print('Sunday')
    if day == 1:
        print('Monday')
    if day == 2:
        print('Tuesday')
    if day == 3:
        print('Wednesday')
    if day == 4:
        print('Thursday')
    if day == 5:
        print('Friday')
    if day == 6:
        print('Saturday')

#Prompt the user for a day of the week just like the previous problem. 
#Except this time print "Go to work" if it's a work day 
#and "Sleep in" if it's a weekend day. 
while True: 
    day = int(input('Day (0-6)? '))
    if day == 1:
        print('Go to work!')
    elif day == 2:
        print('Go to work!')
    elif day == 3:
        print('Go to work!')
    elif day == 4:
        print('Go to work!')
    elif day == 5:
        print('Go to work!')
    else:
        print('Sleep in!')

#Prompt the user for a number in degrees Celsius
#and convert the value to degrees in 
#Fahrenheit and display it to the user.
print("I can convert Celsius to Fahrenheit")
while True:
    temp = int(input('Temperature in C '))
    print(str((temp*1.8)+32) + ' F')"""

#Prompt the user for two things:
#The total bill amount:
#The level of service, which can be one of the following: good, fair, or bad
#Calculate the tip amount and the total amount (bill amount + tip amount).
#The tip percentage based on the level of service is based on:

#good -> 20%
#fair -> 15%
#bad -> 10%
while True:
    total = int(input('Total Bill Amount? '))
    service = input('Level of Service? ')
    if service == 'good':
        print(total + (total * 0.2))
    elif service == 'fair':
            print(total + (total * 0.15))
    elif service == 'bad':
            print(total + (total * 0.1))






