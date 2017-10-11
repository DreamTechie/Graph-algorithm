'''
Hints:
1) There are 64 kinds of bases in the world
2) Be eXclusive OR inclusive
3) The key is your mind
4) Long live Igor Pavlov


def crack_it():
'''

import base64
import itertools

def ___decoding_msg___():
    encoded = "ThXJ3QdxaW3COCHVOSBtaW5keW8tciBtaW5keRphQIJtSPWtv+Ibt0fIwZhOh3B8V5Uyat7wwjh+Q+ShnPS4zGNCfsBKh4PDW7H1Hig63NQAP8425m28gxZsSXPzic2vrvgPuif0QBp9aW5lfWl1cykmaWlveG90USNsaGs5eW90ciwnaWZueP8kxOJtaWtlaHR1ESACaQBkHm8HckFtHW4XeUF1BiAVaRpkeW9heCFt6e3WfHVHoSF4b29kWe/B8yBt"
    # encoded=base64.b64decode(encoded)

    print(encoded)
    # return
    number = []
    for i in range (0,len(encoded)):
        number.append(ord(encoded[i]))
    key = 'your mind'
    # key = base64.b32encode(key)

    key_ = []

    for i in range(0,len(key)):
        key_.append(ord(key[i]))

    key_length = len(key_)

    # print(len(number)/8)
    #now performing xor operation cypher with key
    key_counter =0
    message = []
    print(number)
    #calculating xor of key and the message
    for n in number:

        if key_counter==(key_length-1):
            key_counter=0
        else:
            key_counter=key_counter+1

        message.append(n^key_[key_counter])

    m=[]
    for i in range(0,len(message)):
        m.append(chr(message[i]))

    print(m)
    # print(base64.b32decode(buffer))



# # itertools.combinations(iterable, r)
# def combinaion(array):
#     combination = []
#     for L in range(0,len(array)+1):
#         for subset in itertools.permutations(array,L):
#             if(len(subset)==len(array)):
#                 combination.append(subset)
#     print(combination)
#     return combinaion


# def oper(a,b,c,d)
#
#     a = ['+','-','/','*']
#
#      if (1a3b4c6d) == 24:
#          return True:
#      else()

# a = combinaion(['+','-','*','/'])
# print("aaaa")
# print(a)


def main():
    ___decoding_msg___()

if __name__ == '__main__':
    main()