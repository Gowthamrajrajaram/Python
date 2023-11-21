# add=lambda x,y:x+y
# print(add(10,27))

# print('...............')

# squareofnumber=lambda num:num*num
# print(squareofnumber(5))

# print('...............')

# bigoftwo=lambda num1,num2:num1 if num1>num2 else num2
# print(bigoftwo(2,3))


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])