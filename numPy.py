from numpy import *
# saves everything in float
arr = array([1,4,5,6,5,3.2]) # will convert everything to float
print(arr.dtype)
print(arr)
arr1 = linspace(0,15,16) # will divide this to 16 parts
print(arr1)
arr2 = arange(1,15,2) # splits by 2
print(arr2)
arr3 = logspace(1,3,5) # divides to 5 parts with an ending limit of 10 power 3
print(arr3)
arr4 = zeros(5)
print(arr4)
arr5 = ones(5)
print(arr5)
arr6 = ones(5,int)
print(arr6)
plus = array([1,2,3,4,5])
plus = plus + 5
print(plus)
newAr1 = array([4,2])
newAr2 = array([3,2])
newAr = newAr1+newAr2
print(newAr)
print(concatenate([newAr1,newAr2]))
print(sum(newAr))
print(min(newAr1))
print(max(newAr2))
print(sort(newAr1))
newAr3 = newAr1.view()
print(newAr3)
print("The adrress of newAr3 is ", id(newAr3))
print("the address of newAr1 is ", id(newAr1))
newAr1[0] = 5
print(newAr1)
print(newAr3) # both will see the change due to shallow copy and they are linked, diff address
newAr4 = newAr2.copy()
print(newAr4)
print("The adrress of newAr4 is ", id(newAr4))
print("the address of newAr2 is ", id(newAr2))
newAr2[0] = 6
print(newAr2)
print(newAr4) # only source will see the change due to deep copy and they are linked, diff address
newAr5 = newAr1
print(newAr5)
print("The adrress of newAr5 is ", id(newAr5))
print("the address of newAr2 is ", id(newAr1))
newAr1[0] = 8
print(newAr5)
print(newAr1) # both will see the change as they noth share the same address
