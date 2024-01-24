# Write a program that reads the contents of the file (using appropriate file I/O code) into a 2-dimensional list/array.
# The program should request the user to enter, via the command line interface, a charge account
# number before the program checks whether the number is valid by searching for it in the 2d list. If the
# account number is found in the list, the program should display an output message indicating the number
# is valid and return the account balance. If the account number is not found in the list, the program should
# display a message indicating the number is invalid and offer the user a further attempt to enter a correct number.

# READ INTO A 2D List/Array
# using from learned in week 8 labs

# Initialize list
accounts_list = []

# Initialize variable to store balance of found account number. This will be declared global.
found_balance = ''


def read_file():
    # read the account file
    infile = open('bank_accounts.txt', 'r')

    # Search through and pare the file to the list
    for row in infile:
        start = 0  # Used to point to current position in each line
        string_builder = []
        # Don't read the comment/labels in the file
        if not row.startswith('#'):
            for index in range(len(row)):
                # If we're reading the comma, or we're at the last letter of the row
                if row[index] == ',' or index == len(row) - 1:
                    string_builder.append(row[start:index])
                    start = index + 1

            # Build up our list
            accounts_list.append(string_builder)
    infile.close()


def is_in_list(acc_num):
    global found_balance
    # Search through whole list and determine whether number is in list
    # If it is - boolean true &  If not - boolean false
    for account in accounts_list:
        if account[0] == acc_num:
            found = True
            found_balance = account[1]
            break

        else:
            found = False

    return found


def output_message():
    print(accounts_list)
    search_num = input("Enter account number to search: ")

    # Checks if found was true
    if is_in_list(search_num):
        print(f"Account {search_num} found.")
        # Print the balance by the balance associated with the index of the found accounts number.
        print(f"Account Balance: {found_balance}")  # using global found_balance variable
    else:
        print(f"Account {search_num} NOT FOUND.")
        # Offer a further attempt to enter a correct number.
        search_num = input("Re-enter account number to search: ")

        if is_in_list(search_num):
            print(f"Account {search_num} found.")
            print(f"Account Balance: {found_balance}")

        else:
            print("NOT FOUND. Cannot Search again.")


def main():
    # Read the file
    read_file()
    # print(accounts_list) # TEST

    # This function searches the list using the function "is_in_list()" and then displays the result message.
    output_message()


main()

# NOTES - Possible impovements
# Use 'with' statement for file handling?  e.g. with open(FILE)
# Avoid using global variables
# Use list comprehensions - when creating 2d list
# Avoid unnecessary code duplication - when account is not found.
