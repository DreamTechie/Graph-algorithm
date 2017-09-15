#!/usr/bin/python
# finding matching characters in given two strings and return the count of matches
import plot
import skyline
import fileOperation


def count_match_in_string(str1, str2):
    count = 0
    for i in range(len(str2)):
        if str1[i] == str2[i]:
            count = count + 1
    return count

def word_replace():
    print("Please enter a directory to replace word from all the files from that directory\n")
    path = raw_input()
    print("What do you want to replace?\n")
    word_to_replace = raw_input()
    print("Replace with?\n")
    replace_with = raw_input()
    fileOperation.read_dir_replace_content(path, word_to_replace, replace_with)

def main():
    # skyline.skyline_config()
    word_replace()

if __name__ == '__main__':
    main()
