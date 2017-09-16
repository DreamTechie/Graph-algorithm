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
    config.log_bucket.append("The directory is :"+path)
    print("What do you want to replace?\n")
    word_to_replace = raw_input()
    config.log_bucket.append("Word to replace :" + word_to_replace)
    print("Replace with?\n")
    replace_with = raw_input()
    config.log_bucket.append("Replace with :" + replace_with)
    try:
        fileOperation.read_dir_replace_content(path, word_to_replace, replace_with)
    except Exception as e:
        config.log_bucket("Couldn't read dir and replace content :"+ str(e))
        print("Couldn't read dir and replace content :"+ str(e))

    #dump to log file
    fileOperation.write_to_file(config.log_bucket,config.log_file)
    config.log_bucket = []


def main():
    # skyline.skyline_config()
    config.log_bucket.append("*******************Bigning of this session of interpretation******************:")
    config.log_bucket.append(str(datetime.datetime.now()))

    try:
        word_replace()
    except Exception as e:
        config.log_bucket.append("Couldn't replace world: " +str(e))
        fileOperation.write_to_file(config.log_bucket,config.log_file)
        print("Couldn't replace world: " +str(e))

if __name__ == '__main__':
    main()
