import math

while True:
    print("Welcome to the Versatile Calculator!")
    print("Choose an option:")
    print("1. Bond")
    print("2. Investment")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "bond":
        # Bond Calculation
        try:
            initial_amount = float(input("Enter the present value of the house: "))
            interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
            years = int(input("Enter the number of years: "))

            monthly_repayment = initial_amount * (interest_rate / 12) / (1 - (1 + interest_rate / 12) ** (-years * 12))

            print(f"The monthly repayment amount is: {monthly_repayment:.2f}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice == "investment":
        # Investment Calculation
        try:
            initial_amount = float(input("Enter the amount of money you are depositing: "))
            interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
            years = int(input("Enter the number of years you plan on investing for: "))
            interest_type = input("Enter 'simple' or 'compound' interest: ").strip().lower()

            if interest_type == "simple":
                total_amount = initial_amount * (1 + interest_rate * years)
            elif interest_type == "compound":
                total_amount = initial_amount * math.pow((1 + interest_rate), years)
            else:
                print("Invalid interest type. Please enter 'simple' or 'compound'.")
                continue

            print(f"The total amount after {years} years will be: {total_amount:.2f}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    else:
        print("Invalid choice. Please choose 'bond' or 'investment'.")

    play_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for using the Financial Calculator. Goodbye!")
        break


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
