# P task 6 - TL
# Program that can pickle an object of items stored in a List data structure.
# SEE WEEK 8 LECTURE AND LABS ABOUT PICKLING.
import pickle


# Pickling in python is serializing an object
# Data Serialization is the concept of converting structured data into a format that allows it to be stored in such a
# way that its original structure to be recovered.
# AKA Convert the object to a stream of bytes that can be easily stored in a file.


def main():
    # object list
    banking = [[5015687, 20001], [5014323, 31011], [5019483, 1400]]
    # Call pickle function
    pickle_object(banking)


def pickle_object(object):
    # oopen file in binary write
    binary_file = open("object_data.dat", "wb")

    # use pickle.dump to pickle the list
    pickle.dump(object, binary_file)

    # close file
    binary_file.close()


# call main
main()
