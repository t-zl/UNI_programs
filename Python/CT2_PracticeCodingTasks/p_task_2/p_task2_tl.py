# Write a program that reads the file and outputs
# (a) the average age of the group correct to 1 decimal place (dps)
# (b) the percentage of the group (correct to 1dps) with each eye colour.

# Initialize list
opt_list = []


# Read file in to list of lists  [colour,age]
def read_file():
    infile = open("optometry.txt", "r")

    # Search through and parse the file to the list
    for row in infile:
        start = 0  # Used to point to current position in each line
        string_builder = []
        # Don't read the comment/labels in the file
        if not row.startswith('#'):
            for index in range(len(row)):
                if row[index] == ',' or index == len(row) - 1:
                    string_builder.append(row[start:index])
                    start = index + 1
                    # print(string_builder) # test

            # Build the list
            opt_list.append(string_builder)

    # Comvert every age value to integer
    for i in opt_list:
        i[1] = int(i[1])

    infile.close()


# performs calculations for average and percentage from dictionary
def get_average_age():
    # inititalize running total
    total_age = 0
    for person in opt_list:
        age = person[1]
        total_age += age

    avg_age = format(total_age / len(opt_list), '.1f')
    return avg_age


def get_tally_colours():
    # Tally each eye colour
    colour_tally = {}
    for person in opt_list:
        colour = person[0]

        if colour in colour_tally:
            colour_tally[colour] += 1
        else:
            colour_tally[colour] = 1
    return colour_tally


def calculate_percentages(tally):
    amount_of_people = len(opt_list)
    for colour in tally:
        print(f"Percentage of {colour} eyes: {format((tally[colour] / amount_of_people) * 100, '.1f')}%")


def main():
    read_file()
    print(opt_list)  # TEST
    print(f"The average age of everyone was {get_average_age()}\n")
    calculate_percentages(get_tally_colours())

    print(get_tally_colours())


# call the main function
main()
