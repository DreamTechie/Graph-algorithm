'''

@author: Saurab Dulal
Date: Nov 13, 2017

Problem Description: This is a recursive solution to the cloth cutting problem - please see the problem
description in README.md file

'''

#using dynamic programming
def clothCuttingDynamicProgramming(length, breadth):
    cuttingMatrix = [[0 for x in range(0, breadth)] for y in range(0, length)]
    cuttingMatrix[3][3] = 2
    cuttingMatrix[4][5] = 9
    cuttingMatrix[3][4] = 10
    cuttingMatrix[12][23] = 100

    for lenX in range(0, length):
        for lenY in range(0, breadth):
            cut = 0
            for k in range(0, int(lenX / 2)):  # hori
                if (cut < (cuttingMatrix[k][lenY] + cuttingMatrix[lenX - k][lenY])):
                    cut = (cuttingMatrix[k][lenY] + cuttingMatrix[lenX - k][lenY])
            for k in range(0, int(lenY / 2)):  # verti
                try:
                    if (cut < (cuttingMatrix[lenX][k] + cuttingMatrix[lenX][lenY - k])):
                        cut = (cuttingMatrix[lenX][k] + cuttingMatrix[lenX][lenY - k])
                except Exception as e:
                    print(e)
            cuttingMatrix[lenX][lenY] = cut

    print(cuttingMatrix)


# the actual length and breadth of the cloth is 20x30, increament is done for 0 th position


#using recursion only
def clothCutting(lenX, lenY, area, input, n, weight=0):

    if n<0:
        return weight
    if(input[n-1]['x']*input[n-1]['y'] > area): #this is orientation less configuration
        return clothCutting(lenX,lenY, area, input, n-1, weight)

    if (input[n-1]['x']*input[n-1]['y'] <= area and input[n-1]['x'] <= lenX and input[n-1]['y'] <=lenY):

        buff_weight = input[n-1]['w']
        try:
            return max(clothCutting(lenX,lenY,area-input[n-1]['x']*input[n-1]['y'], input, n-1, weight+buff_weight),
                    clothCutting(lenX, lenY, area, input, n-1, weight))
        except Exception as e:
            print(e)


#to make sample data set
def make_data_set(input): # [(),()]
    sample_data = []
    for i in input:
        sample_data.append({'x':i[0],'y':i[1],'w':i[2]})
    return sample_data,len(sample_data)


if __name__ == '__main__':

    input = [{'x':3,'y':4,'w':10},{'x':4,'y':5,'w':9},{'x':12,'y':23,'w':100},{'x':3,'y':3,'w':2}]

    input1 = [{'x': 1, 'y': 1, 'w': 10}, {'x': 20, 'y': 20, 'w': 100}]

    #40,70
    sample_data = [(21, 22, 582), (31, 13, 403), (9, 35, 315), (9, 24, 216), (30, 7, 210), (11, 13, 143),
              (10, 14, 140), (14, 8, 110), (12, 8, 94), (13, 7, 90)]

    sample_data1 = [(8, 4, 66), (3, 7, 35), (8, 2, 24), (3, 4, 17), (3, 3, 11), (3, 2, 8), (2, 1, 2)]

    input3,size = make_data_set(sample_data)

    print(clothCutting(20, 30, 20*30, input, len(input))) #since size will be from 0-n, so it will consider n, but the list will be of n-1 size




