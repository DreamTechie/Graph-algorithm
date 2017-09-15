'''This file deals about the operation in folders and files such as swapping certain text with another residing in whole repo'''

import os
import sys
import re


def replace_content(text_to_replace, replace_with, file_path):
    re.sub(text_to_replace,replace_with,file_path)
    return

def write_to_file(f_pointer,content): #this function will replace entire content with the new content

    f_pointer.seek(0)
    f_pointer.write(content)
    f_pointer.truncate() #truncate the file size, default assure current file position is not changed
    return

def read_dir_replace_content(path, word_to_replace, replace_with):

    recursive_replace_flag = False
    check =0
    for root, subdir, files in os.walk(path):

        # so we got every root, subdir and files from that folder, this function will only work for text files for now, others
        # are left for future enhancement

        for filenames in files:

            file_path = os.path.join(root, filenames)

            with open(file_path, 'r+') as f:
                f_content = f.read()

                if word_to_replace in f_content:
                    print('This file' + file_path + ' ' 'contains '+ word_to_replace)

                    if recursive_replace_flag == False:
                        print("Do you want to replace it?"+'\n' + "press 'y' from this file only"+ '\n' + "Press 'ry' to replace from all the files" +'\n' + "or press any character to skip")
                        user_input = raw_input()
                        if user_input=='y':
                            f_content = re.sub(word_to_replace,replace_with, f_content)
                            write_to_file(f,f_content)
                        elif user_input=='ry':
                            f_content = re.sub(word_to_replace,replace_with,f_content)
                            write_to_file(f,f_content)
                            recursive_replace_flag = True
                    else:
                        f_content = re.sub(word_to_replace, replace_with, f_content)
                        write_to_file(f,f_content)
    return