import math

def main():
    while True:
        while True:
            decimal = input("Enter a decimal number: ")
            try:
                numberfloat = float(decimal)
                break
            except ValueError:
                print("Oops! That was not a valid decimal number. Please try again.")

        while True:
            integer = input("Enter an integer number: ")
            try:
                numberint = int(integer)
                break
            except ValueError:
                print("Oops! That was not a valid integer number. Please try again.")

        print("The sum of the decimal number and integer number is: ", numberint + numberfloat)

        print("The product of the decimal number and integer number is: ", numberint * numberfloat)

        print("The difference between the numbers is: ", numberint - numberfloat)


        if numberfloat == 0.0 or numberint == 0:
            print("Sorry, division by zero is not allowed.")
        else:
            print("The first number divided by the second number is: ", numberint / numberfloat)



        squareroot = input("Do you want to find the square root of the decimal number or the integer number? (decimal/integer): ")
        if squareroot == 'decimal':
            if numberfloat > 0:
                print("The square root of the decimal number is: ", math.sqrt(numberfloat))

            else:
                print("Sorry the square root of a negative number is not allowed.")

        elif squareroot == 'integer':
            if numberint > 0:
                print("The square root of the integer number is: ", math.sqrt(numberint))

            else:
                print("Sorry the square root of a negative number is not allowed.")




        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes':
            print("Thank you for playing!")
            break

main()
