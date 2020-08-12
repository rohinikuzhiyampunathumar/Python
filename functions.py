
def add(x,y):
    c= x+y
    print(c)

add(5,4)
# function that returns a value
def add(x,y):
    c= x+y
    return c
result = add(3,4)
print(result)
# function that returns multiple values
def add_sub(x,y):
    add= x+y
    sub = x-y
    return add,sub
res1,res2 = add_sub(7,5)
print("The addition is ", res1," and the subtraction is ",res2)

# immutuable variables in function
def update(x):
    x=8
    print("The value of x is ",x)
a= 10
update(a)
print("The value is a is ",a)
# list is mutable
def updateList(list):
    list[1] = 5
    print("the address of list inside function is ", end = "")
    print(id(lst))
    print("The value of list inside function is ",list)
lst = [12,2,3]
print("the address of list outside function is ", end="")
print(id(lst))
updateList(lst)
print("The value os list outside function is ",lst)
print("the address of list outside function after update is ", end="")
print(id(lst))


