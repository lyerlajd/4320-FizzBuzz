def main():
    counter = 1

    while(counter <= 100):
        check(counter)
        counter += 1

def check(number):
    response = ""
    if (number % 3 == 0 and number % 5 == 0):
        response += "FizzBuzz"
    elif (number % 3 == 0):
        response += "Fizz"
    elif (number % 5 == 0):
        response += "Buzz"
    else:
        response += str(number)
    print(response)

main()