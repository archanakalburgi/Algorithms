'''
pascal triangle 

at the top :
    1

2nd line :
    1 1 


1
11
121
1331
14641


3rd line in pascal triangle has :  
    1 at the beginning and the end of the line
    addition of the two numbers of the previous line in between 
'''


# def pascal_triangle(rows):
# a[i,j] = a[i-j,j-1] + a[i-1,j+1]

list1 = [] 

for i in range (5):
    temperory_list = []
    for j in range (i*2 + 2):
        if j==0 or j==i :
            temperory_list.append(1)
        else :
            temperory_list.append(list1[i-1][j-1] + list1[i-1][j+1]) 
        list1.append(temperory_list) 

for i in range(5):
    for j in range (4-i):
        print(end = ' ')
    for j in range(i+1):
        print(list1[i][j], end = ' ')
    print()  



# rows = 3 # rows
# columns = (2 * rows) - 2 # columns 

# for row in range(0, rows): 
#    for col in range(0, columns):  
#       print(end=" ") 

#    columns = columns - 1 

#    for col in range(0, row + 1):  
#       print("*", end=" ") 
   
#    print(" ")       
