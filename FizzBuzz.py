def main():
    counter = 1

    while(counter <= 100):
        print(check(counter))
        counter += 1

def check(number):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif (number % 3 == 0):
        return "Fizz"
    elif (number % 5 == 0):
        return"Buzz"
    else:
        return number

main()