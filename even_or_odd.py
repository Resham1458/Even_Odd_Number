def check():
    c = input("Do you want to try another number?")

    if c == 'yes':
        print("Go ahead!")
        number()
    else:
        print("Goodbye!")

def number():
    number = int(input("Please enter any random number:"))

    if number % 2 == 0:
        print("You entered an even number")
    else:
        print("You entered an odd number")

    check()
number()
