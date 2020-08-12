i = 1
# While loop , end command will print next print in the same loop
while i <= 5:
    print("Hello ", i, end="")
    print("hi")
    i+=1
#For Loop
x =['abc',25, 3.5]
for i in x:
    print(i)
y = 'defg'
for i in y:
    print(i,end="")
for i in [23,45,67,'test']:
    print(i)
# will print till 20 from 11
for i in range(11,21,1):
    print(i)
# will print till 12 from 20
for i in range(20,11,-1):
    print(i)
# will print till 10 from 1
for i in range(1,11):
    if i%5!=0:
        print(i)

