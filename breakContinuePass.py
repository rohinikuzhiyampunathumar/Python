av = 3
ip = int(input("Enter the number of candies that you want: "))
i=1
while i <=ip:
    if i > av:
        print("Out of stock")
        break
    print("Candy")
    i+=1
# continue will skip that particular entry in the loop
for i in range(1,100):
    if i%3==0:
        continue
    print(i)
# pass will be used you dont have any code in that block
print("Exercise for pass statement")
for i in range(1,10):
    if i%2==0:
        pass
    else:
        print(i)
