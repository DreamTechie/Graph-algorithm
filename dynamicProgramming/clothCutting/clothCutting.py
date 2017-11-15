'''

@author: Saurab Dulal
Date: Nov 13, 2017

Developed in Linux OS
Requirement = python 3.x +

Problem Description: This is a recursive and dynamic programming solution to the cloth cutting problem - please see the problem
description in README.md file

'''

import time

#Using Dynamic Programming
def clothCuttingDynamicProgramming(length, breadth, data):

    cuttingMatrix = [[0 for x in range(0, breadth)] for y in range(0, length)]


    #initilizing all the given data
    for i in data:
        if (i['x'] <= length and i['y'] <= breadth):

            cuttingMatrix[i['x']][i['y']] = i['w']

        # if(i['y']<=length and i['x']<=breadth):
        #     cuttingMatrix[i['y']][i['x']] = i['w']


    for lenX in range(0, length):
        for lenY in range(0, breadth):
            cut = 0
            for k in range(0, int(lenX / 2)+1):
                if (cut < (cuttingMatrix[k][lenY] + cuttingMatrix[lenX - k][lenY])):
                    cut = (cuttingMatrix[k][lenY] + cuttingMatrix[lenX - k][lenY])
            for k in range(0, int(lenY / 2)+1):
                if (cut < (cuttingMatrix[lenX][k] + cuttingMatrix[lenX][lenY - k])):
                    cut = (cuttingMatrix[lenX][k] + cuttingMatrix[lenX][lenY - k])

            cuttingMatrix[lenX][lenY] = cut

    return cuttingMatrix[length-1][breadth-1]


#The actual length and breadth of the cloth is 20x30, increament is done for 0 th position

#Using recursion only
def clothCutting(lenX, lenY, area, input, n, weight=0):

    if n<0:
        return weight
    if(input[n-1]['x']*input[n-1]['y'] > area): #this is orientation less configuration
        return clothCutting(lenX,lenY, area, input, n-1, weight)

    if (input[n-1]['x']*input[n-1]['y'] <= area and input[n-1]['x'] <= lenX and input[n-1]['y'] <=lenY):

        buff_weight = input[n-1]['w']
        return max(clothCutting(lenX,lenY,area-input[n-1]['x']*input[n-1]['y'], input, n, weight+buff_weight),
                    clothCutting(lenX, lenY, area, input, n-1, weight))


#To make sample data set
def make_data_set(input): # [(),()]
    sample_data = []
    for i in input:
        sample_data.append({'x':i[0],'y':i[1],'w':i[2]})
    return sample_data

def sample_data(n):

    #20x30
    sample_data1 = [(3, 4, 10), (4, 5, 9), (12,23,100),(3, 3, 2)]

    #40,70
    sample_data2 = [(21, 22, 582), (31, 13, 403), (9, 35, 315), (9, 24, 216), (30, 7, 210), (11, 13, 143),
                    (10, 14, 140), (14, 8, 110), (12, 8, 94), (13, 7, 90)]
    #10x15
    sample_data3 = [(8, 4, 66), (3, 7, 35), (8, 2, 24), (3, 4, 17), (3, 3, 11), (3, 2, 8), (2, 1, 2)]

    # 40x70
    sample_data4 = [(31, 43, 500), (30, 41, 480), (29, 39, 460), (28, 38, 440), (27, 37, 420), (26, 36, 410),
                    (25, 35, 400), (24, 34, 380), (33, 23, 360), (22, 32, 340), (31, 21, 320), (29, 18, 300),
                    (17, 27, 280), (15, 24, 240), (16, 25, 260),
                    (15, 24, 240), (23, 14, 220), (21, 12, 180), (19, 11, 160), (9, 17, 140)]

    #offsetting 0,0 position in each data set
    if n==1:
        return make_data_set(sample_data1),21,31
    if n==2:
        return make_data_set(sample_data2),41,71
    if n==3:

        return make_data_set(sample_data3),11,16
    if n==4:
        return make_data_set(sample_data4),41,71

    else:
        return False

if __name__ == '__main__':


    n = 2
    if sample_data(n)!=False:
        data, length, breadth = sample_data(n)
        start_time = time.time()
        print("The maximum profit using Dynamic programming: " +str(clothCuttingDynamicProgramming(length, breadth, data)))  # since size will be from 0-n, so it will consider n, but the list will be of n-1 size
        diff_time = time.time() - start_time
        print ('and the total time for execution of program :' +str(diff_time) + 'seconds')

        start_time = time.time()
        print("The maximum profit using Recursion: " + str(clothCutting(length, breadth,(length-1)*(breadth-1)
                                                                          ,data,len(data))))  # since size will be from 0-n, so it will consider n, but the list will be of n-1 size
        print('and the total time for execution of program :' + str(time.time() - start_time) + 'seconds')
    else:
        print("sample " + str(n) +' not found' )






