# Write a program that asks the user to enter an even number at the command line interface and returns the
# sum of all the even numbers up to that value. For example, if the user entered 12, the program returns the
# value 42 (=2+4+6+8+10+12).
def sum_of_evens(user_num):
    if user_num % 2 == 0:
        total = 0
        for num in range(2, user_num + 2, 2):
            total += num
        print(f"Sum of all the even numbers up to {user_num} is: {total}")

    else:
        print(f"{user_num} is NOT an even number.")


def main():
    try:
        user_number = int(input("Enter an even number: "))
        # If the number is even run the calculation
        sum_of_evens(user_number)

    except ValueError:
        print("Bad input. MUST BE AN INTEGER")


main()
