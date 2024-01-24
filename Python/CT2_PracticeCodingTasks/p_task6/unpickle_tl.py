# Program to unpickle the binary data into the prescribed list format specified by you iin the first program.

import pickle
# use pickle.load


def main():
    # open file in binary read
    input_file = open("object_data.dat", "rb")

    # Call the UNpickle function
    print(unpickle_object(input_file))


def unpickle_object(file):
    # use pickle.load to unpickle
    new_object = pickle.load(file)

    # Return the unpickled
    return new_object


# call main
main()

