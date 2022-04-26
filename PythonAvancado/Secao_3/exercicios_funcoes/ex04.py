def fizzBuzz(var):
    if var % 5 == 0 and var % 3 == 0:
        return 'FizzBuzz'

    elif var % 2 == 0:
        return 'fizz'

    elif var % 5 == 0:
        return 'buzz'

    else:
        return var


print(fizzBuzz(2))
print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(7))
