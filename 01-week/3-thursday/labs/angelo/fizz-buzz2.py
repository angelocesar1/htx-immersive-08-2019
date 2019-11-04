for numbers in range(100): 
    if numbers == 0:
        print('Not Divisible!')
    elif numbers % 3 == 0 and numbers % 5 == 0:
        print('FizzBuzz!')
    elif numbers % 3 == 0:
        print('Fizz!')
    elif numbers % 5 == 0:
        print('Buzz!')
    else:
        print(numbers)
  