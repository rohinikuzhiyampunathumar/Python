for i in range(4):
    for j in range(4):
        print("*",end="")
    print()

for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(4):
    for j in range(4-i):
        print("*", end="")
    print()

nums = [12,23,4,22,6]
for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print('There is no number divisible by 5')


val = 0
for j in range(2,100,1):
    for i in range(2,100,1):
        if j%i==0:
            val+=1
            if val >2:
                break
    if val==1:
        print("The number ",j," is prime")
    val = 0

