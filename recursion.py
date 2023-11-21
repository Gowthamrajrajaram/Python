# def getusernamepass(username,password):
#     if username != 'abcd':
#         print('Invalid username')

#         username=input('Enter user name ')
#         password=input('Enter password ')
#         getusernamepass(username,password)
#     elif password != 'abcd':
#         print('Invalid password ')
#         username=input('Enter user name ')
#         password=input('Enter password ')
#         getusernamepass(username,password)
#     else:
#         print(username,password)

# username=input('Enter user name ')
# password=input('Enter password ')
# getusernamepass(username,password)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
result= factorial(5)
print(result)#120

print('.....................')


def sumofdigit(num):
    if num==0:
       return 0

    else:
        rem=num%10
        no=num//10  
        return rem + sumofdigit(no)

print(sumofdigit(1873))#19
