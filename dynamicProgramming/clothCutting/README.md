## Problem Statement

DVP 6.14 ) Cutting cloth. You are given a rectangular piece of cloth with dimensions X × Y , where X and Y are positive integers, and a list of n products that can be made using the cloth. For each product i ∈ [1, n] you know that a rectangle of cloth of dimensions ai × bi is needed and that the final selling price of the product is ci. Assume the ai, bi, and ci are all positive integers. You have a machine that can cut any rectangular piece of cloth into two pieces either horizontally or vertically. Design an algorithm that determines the best return on the X × Y piece of cloth, that is, a strategy for cutting the cloth so that the products made from the resulting pieces give the maximum sum of selling prices. You are free to make as many copies of a given product as you wish, or none if desired.

### Input 
The input will be specified in a file as follows. The first line will be the
integers X, Y , separated by whitespaces. The next line will be n. The next n lines will be ai
, bi
, ci
in that order separated
by whitespaces. For example, one input is:
- 20 30
- 4
- 3 4 10
- 4 5 9
- 12 23 100
- 3 3 2
### Output 
Your output should be the best return that you can get. You do not need to print the strategy.


### Requirements 
- python 3.x+ 
- OS: Linux  

### Executing the program
[ python3 ] [ file_name ] [ filename ]
<code> - python3 clothCutting.py sampledata </code >

File name must be submitted while executing the program, as the program takes the input of a file name from the console

### Limitations 
- Program produces output for a orientations insensitive products i.e. x,y is consider same as y,x input. To make it orientation sensative, please comment out line 21-31 in *clothCutting.py*
- Need to provide a file name as a input while executing the program from the commandline(only option available)
- There should not be any \r (carriage return) after the last line (x,y product line in our case) of the file(important requirement)

### Refrences
http://www.geeksforgeeks.org/knapsack-problem/
http://cmup.fc.up.pt/cmup/engmat/2011/seminario/Artigos2011/Joao_Rebelo_2.pdf
http://androidprogramme.blogspot.com/2014/11/kite-cutting-problem-using-dynamic.html
