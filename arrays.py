from array import *
# import array as arr

# use this if you are using import array as arr
# vals = arr.array('i',[4,-3,7,3])
# print(vals)
# vals.reverse()
# print(vals)

vals = array('i',[7,8,4,-3,6,8])
print(vals)
for i in range(6):
    print(vals[i])
for i in range(len(vals)):
    print(vals[i])
for i in vals:
    print(i)
# assigning values to a new array from the old array
newArr = array(vals.typecode, (a for a in vals))
# if you know the type of the other array then you can use the below
newArr1 = array('i',(a for a in vals))
print(newArr1)

# while loop
i=0
while i < len(newArr):
    print(newArr[i])
    i+=1

# Array values fron user input
ipArr = array('i',[])
size = int(input("Enter the length of the array"))
for i in range(size):
    value = int(input("Enter the value :"))
    ipArr.append(value)
print(ipArr)

# To search a value in the array and to print the index of that element
srch = int(input("Enter the search value"))
k = 0
for e in ipArr:
    if(e==srch):
        print(k)
    k+=1
#another direct way
print(ipArr.index(srch))