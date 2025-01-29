# Python Program to Check Armstrong Number?


def is_armstrong(number):
        # Convert number to string to easily iterate through digits
        num_str = str(number)
        num_digits = len(num_str)

        # Calculate the sum of each digit raised to the power of num_digits
        total = sum(int(digit) ** num_digits for digit in num_str)

        # Check if the sum equals the original number
        return total == number

    # Example usage
number = int(input("Enter a number to check if it is an Armstrong number: "))

if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
else:
        print(f"{number} is not an Armstrong number.")
