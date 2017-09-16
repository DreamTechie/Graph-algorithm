#!/usr/bin/python
# finding matching characters in given two strings and return the count of matches
import plot
import skyline
import fileOperation
import config
import datetime
import logHandler as lh


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
    try:
        fileOperation.read_dir_replace_content(path, word_to_replace, replace_with)
    except Exception as e:
        print("Couldn't read dir and replace content :"+ e)
def main():
    # skyline.skyline_config()

    print(datetime.datetime.now())
    f_log_name = config.log_file
    log_object= lh.log_handler()
    log_pointer = log_object.give_me_a_log_pointer()

    print >> log_pointer, "*******************Bigning of this session of interpretation******************:"
    print >> log_pointer, datetime.datetime.now()  # or f.write('...\n')
    return

    try:
        word_replace()
    except Exception as e:
        print("Couldn't replace world: " +e)

if __name__ == '__main__':
    main()
