from copy import deepcopy

sum = 20
def construct_tree(given_node={1:2,2:4,3:7,4:0,5:10}, max_sum=0):


    for node in given_node:
        print(node)
        if max_sum == 20:
            return max_sum
        max_sum = max_sum+node
        max_sum = construct_tree(given_node, max_sum)

    return max_sum



def bestCutting(length, breadth, number, cuttingSize):


    cuttingSizeList = cuttingSize #Deep copy is used to pass by value in python,

    for i in range(1, number):

        buffer = deepcopy(cuttingSizeList[i])

        for j in range(0,i):

            #need to check length and breadth
            xCutting = cuttingSizeList[j]['x']+cuttingSizeList[i]['x']
            yCutting = cuttingSizeList[j]['y']+cuttingSizeList[i]['y']
            wCutting = cuttingSizeList[j]['w']+cuttingSizeList[i]['w']

            if (xCutting <= length and yCutting <= breadth):

                if wCutting > buffer['w']:
                    buffer['x'] = xCutting
                    buffer['y'] = yCutting
                    buffer['w'] = wCutting

        cuttingSizeList[i]['x'] = buffer['x']
        cuttingSizeList[i]['y'] = buffer['y']
        cuttingSizeList[i]['w'] = buffer['w']

    return cuttingSizeList





if __name__ == '__main__':

    input = [{'x':3,'y':4,'w':10},{'x':4,'y':5,'w':9},{'x':12,'y':23,'w':100},{'x':3,'y':3,'w':2}]

    construct_tree()
    #cuttingSizeList = bestCutting(20,30,4,input)
    #print(cuttingSizeList)

