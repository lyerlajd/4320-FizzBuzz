def main():
    # initializing counter
    counter = 1

    # looping through counter until it equals 100
    while(counter <= 100):
        # calling function to check if divisible by 3 or 5, then printing response
        print(fizzbuzz(counter))
        # incrementing counter
        counter += 1

def fizzbuzz(number):
    # if divisible by 3 and 5, returning FizzBuzz
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    # if only divisible by 3, returning Fizz
    elif (number % 3 == 0):
        return "Fizz"
    # if only divisible by 5, returning Buzz
    elif (number % 5 == 0):
        return"Buzz"
    # number was not divisble by 3 or 5, just returning number
    else:
        return number


# calling the main function
main()