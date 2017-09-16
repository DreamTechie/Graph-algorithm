'''This file deals about the operation in folders and files such as swapping certain text with another residing in whole repo'''

import os
import sys
import re
import config


def write_to_file(content,file_name):

    if isinstance([content],list):
        with open(file_name, 'a+') as outfile:
            outfile.write('\n'.join(content) + '\n')
    return

def replace_content(text_to_replace, replace_with, file_path):
    re.sub(text_to_replace,replace_with,file_path)
    return

def replace_write_to_file(f_pointer,content): #this function will replace entire content with the new content

    f_pointer.seek(0)
    try:
        f_pointer.write(content)
    except Exception as e:
        config.log_bucket.append("Couldn't write to file 'from_replace'" + e)
        print("Couldn't write to file " + e)

    f_pointer.truncate() #truncate the file size, default assure current file position is not changed

    return

def read_dir_replace_content(path, word_to_replace, replace_with):

    recursive_replace_flag = False
    word_found_counter =0

    for root, subdir, files in os.walk(path): #if path not found it return to where it was called from

        # so we got every root, subdir and files from that folder, this function will only work for text files for now, others
        # are left for future enhancement
        #there is different between input and raw_input

        for filenames in files:

            file_path = os.path.join(root, filenames)

            with open(file_path, 'r+') as f:
                f_content = f.read()

                if word_to_replace in f_content:
                    word_found_counter+= 1;
                    config.log_bucket.append('This file' + file_path + ' ' 'contains '+ word_to_replace)
                    print ('This file' + file_path + ' ' 'contains '+ word_to_replace)

                    if recursive_replace_flag == False:
                        print("Do you want to replace it?"+'\n' + "press 'y' from this file only"+ '\n' + "Press 'ry' to replace from all the files" +'\n' + "or press any character to skip")
                        user_input = raw_input()
                        config.log_bucket.append("User input: "+ user_input)
                        if user_input=='y':
                            f_content = re.sub(word_to_replace,replace_with, f_content)
                            try:
                                replace_write_to_file(f,f_content)
                            except Exception as e:
                                config.log_bucket.append("Cannot write to file :" +e)
                                print("Cannot write to file 'y':" +e)
                        elif user_input=='ry':
                            f_content = re.sub(word_to_replace,replace_with,f_content)
                            try:
                                replace_write_to_file(f,f_content)
                            except Exception as e:
                                config.log_bucket.append("Cannot write to file 'ry':" + e)
                                print("Cannot write to file :" +e)
                            recursive_replace_flag = True
                    else:
                        f_content = re.sub(word_to_replace, replace_with, f_content)
                        try:
                            replace_write_to_file(f, f_content)
                        except Exception as e:
                            config.log_bucket.append("Cannot write to file 'ry+':" + e)
                            print("Cannot write to file :" + e)

    config.log_bucket.append("Word found in total no of " +str(word_found_counter)+ " files")

    return