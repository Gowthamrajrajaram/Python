def add(name):
    print('Hi')
    print(name)
    print('Welcome to python')

add('Gowtham')

print('......................')
#return statement

def squareofnumber(num):
    return num*num
result=squareofnumber(5)
print(result) 

print('......................')

def calculate(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1*num2
    return add,sub,mul,div

print(calculate(10,150))
print(type(calculate(10,150)))

print('......................')
# types of argument
# 1.positional argument
# 2.keyword argument
# 3.default argument
# 4.variable length argument

#1.positional argument
def add(no1,no2):
    return no1+no2
print(add(100,50))
print('......................')

#2.keyword argument
def wish(name,age):
    print('hi',name,age)
wish(name='gowtham',age=22)

print('......................')

#3.default argument
def wish(name='admin'):
    print('Hi',name)
wish('Gowtham')
wish()

print('......................')

#4.variable length argument
def calculatetotal(*num):
    total=0
    for subject in num:
        total=total+subject
    print(total)
calculatetotal(90)
calculatetotal(80,90,50)