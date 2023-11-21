'''statement (or) expression is syntaticaly correct, it may cause an error when an attepmt
is made to execute it.errors detecting executions are called  exception

every excption in python is a class
all exception classes are child/sub classes of baseexception
during runtime ,if exception occurs, python will throw us the exception class name and stop the program immediately / '''

#Zero division error - when an attempt is made to divide a number by zero
num1=10
num2=0
print(num1/num2)


# syntax error - such as misspelled keyword , a missing colon (or) unbalanced paranthesis
for i in range(1,10):
    print(i) 


# name error - when a variable (or) function name is not fount in the current scope

print(2+ten)

def fun():
    return 1
f()

#type error - such as adding string to an integer. when  an operator (or) function is applied to an object of the wrong type

print(10 + 'G')

#index error - when an index is out of range in list ,tuple

lists=[1,2,3,4,5]
print(lists[5])

#key error - when the key is not found in dictionary

dicts={'name':'gowtham','age':25}
print(dicts)
print(dicts['name'])
print(dicts['place'])


#value error - when  function (or) method is called with an invalid argument (or)input. such as trying to convert a string to integer.when the string doesn't represent a valid integer
num1=int(input())
num2=int(input())
print(num1/num2)

#attribute error- when an attribute (or) method is not found an object

class student:
    def subject(self):
        pass
s=student()
print(s.subject)
print(s.obj)

j=5
print(j.append(6))

#IO error - such as reading (or) writing a file
#import error - when an import statement fails to find (or) load a module

# try and except statement - catching exception
# finally - used to execute the necessary code for the programe
try:
    num1=int(input('Enter a number ')) 
    num2=int(input('Enter a number '))
    print(num1/num2)

except ZeroDivisionError:
    print('divided by zero,pleas check')

except ValueError:
    print('check if numbers are given by user')

finally:
    print('outer finally')

try:
    num1=int(input('Enter a number ')) 
    num2=int(input('Enter a number '))
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print('divided by zero,pleas check')
    finally:
        print('inner finally')
except ValueError:
    print('check if numbers are given by user')

finally:
    print('outer finally')

# user defined exception
# raise allows the programmer to force a specific execption to occur
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def divide(a, b):
    if b == 0:
        raise MyCustomException("Division by zero is not allowed.")
    return a / b


try:
    result = divide(10, 0)
except MyCustomException as e:
    print("An error occurred: ",e)
else:
    print(f"Result: ",result)


class InsufficentBalanceException(Exception):
    def __init__(self,message):
        self.message=message
balance=1000
try:
   amount=int(input("enter amount to withdraw"))
   if amount<balance:
       raise InsufficentBalanceException("check your balance")

except InsufficentBalanceException:
    print('I am user defined exception handling area')
