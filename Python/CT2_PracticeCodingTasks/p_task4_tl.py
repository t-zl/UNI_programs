# Practice task 4 - TL - ANAGRAM CHECKER

# Write and program that reads two words in from the keyboard,
# determines whether these are
# anagrams and produces a report detailing the character make-up of each word.

def are_anagrams(w1, w2):
    dict1 = {}
    dict2 = {}

    #   Tally word 1

    for i in w1:
        if i in dict1:
            # increase tally for that key in dictionary
            dict1[i] = dict1[i] + 1

        else:
            # Add a new key for the letter and add value for tally
            dict1[i] = 1

    #   Tally word 2

    for i in w2:
        if i in dict2:
            # increase tally for that key in dictionary
            dict2[i] = dict2[i] + 1

        else:
            # Add a new key for the letter and add value for tally
            dict2[i] = 1

    anagram_check = dict1 == dict2

    if anagram_check:
        print(f"{w1} and {w2} are anagrams!")

    else:
        print("Not anagrams.")

    # report detailing the character make-up - calls function
    print(word_report(dict1, w1))
    print(word_report(dict2, w2))


def word_report(word_dict, word):
    report = f"{word} contains: "
    # sort word_dict alphabetically
    # word_dict = sorted(word_dict)

    for letter in word_dict:
        # build the report string that prints the letter and the tally
        if len(word_dict) < 2:
            report += f"{word_dict[letter]}{letter}"

        # if at last letter in dictionary, print 'and' before it
        elif letter == list(word_dict)[-1]:
            report += f"and {word_dict[letter]}{letter}"

        else:
            # If not last letter
            report += f"{word_dict[letter]}{letter}, "

    return report


def main():
    word1 = input("Enter First Word: ").lower()
    word2 = input("Enter Second Word: ").lower()
    # used .lower() to make all characters lowercase.

    are_anagrams(word1, word2)


main()
