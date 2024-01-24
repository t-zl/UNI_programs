# An algorithm, A1, takes a list of n integers and performs a computation.
# Write two functions T1 and T2 which evaluate the above times for a given input n. At what value of n does
# algorithm A2 become more time-efficient (i.e. takes less time to perform the same computation) than A1?
#

def T1(n):
    result = 0.0045 * (n ** 3)
    # result = 0.0045 * n ** 3
    return result


def T2(n):
    result = 0.36 * (n ** 2) + (0.15 * n)
    # result = 0.36 * n ** 2 + 0.15 * n
    return result


# function to determine when algorithm A2 becomes more time-efficient
def more_efficient():
    value_of_n = 1
    keep_going = True

    while keep_going:
        if T1(value_of_n) > T2(value_of_n):
            keep_going = False

        else:
            value_of_n += 1

    return value_of_n


def main():
    # user_input = float(input("Enter a number for n: ")) # TEST
    # print(T1(user_input))  # Test
    # print(T2(user_input))  # Test
    print(f"\nAlgorithm A2 becomes more time-efficient than A1 at value: {more_efficient()}")


main()
