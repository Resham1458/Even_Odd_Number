def check():
    c = input("Do you want to try another number?")

    if c == 'yes':
        print("Go ahead!")
        number()
    else:
        print("Goodbye!")

def number():
    number = int(input("Please enter any random number:")) #asks user to enter random number

    if number % 2 == 0:                                    #tests for the even number
        print("You entered an even number")
    else:
        print("You entered an odd number")

    check()
number()
