#if-else
number=int(input("Enter a number: "))
if number%2==0:
    print("You entered a even number")
else:
    print("You entered a odd number")

num="even: "+str(number) if number%2==0 else "odd: "+str(number)
print(num)

#elif
marks=int(input("Enter your marks: "))
if marks>90 and marks<=100:
    print("Your grade is A")
elif marks>80 and marks<=90:
    print("Your grade is B")
elif marks>65 and marks<=80:
    print("Your grade is C")
elif marks>50 and marks<=65:
    print("Your grade is D")
else:
    print("Your grade is RA")

print("..............")

#for -sequential traversal

num=10
for val in range(num):
    print(val)

print("...........................")

for value in range(1,num):
    print(value)

print("...........................")
for key in range(-10,num):
    print(key)

print("...........................")
for col in range(num,0,-1):
    print(col)
print("...........................")

for num in range(0,20,2):
    print(num)
print("...........................")  

lists=['Gowtham','Guna','Mano','Kavin']
for i in lists:
    print(i)

print("...........................")  

cards=[2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']
smallcard=[]
bigcard=[]
for words in cards:
    print(words)
print("..............")
for word in cards:
    if type(word)==str:
        bigcard.append(word)
    else:
        smallcard.append(word)
print(smallcard)
print(bigcard)
print("..............")

for name in range(len(cards)):
    print(name,cards[name])
print("..............")
#sum of (0 to 10)
print(sum(range(10)))

print("..............")

#check the prime numers
for number in range(2, 10):
    for x in range(2, number):
        if number % x == 0:
            print(number, 'equals', x, '*', number//x)
            break
    else:
        print(number, 'is a prime number')
            
print("..............")
# odd nubmer even numbers
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
print("..............")
#cube of o to 10
for i in range(10): print(i**3)
print("..............")
#while loop
codenum=0
while(codenum<10):
      print(codenum)
      codenum+=1
print("..............")

tables=6
user=1
while(user<=10):
    print(user,'*',tables,'=',user*tables)
    user+=1

print("..............")

# reversing a digit
digits=12345
back=0
rev=0
while digits!=0:
    back=digits%10
    digits=digits//10
    rev=rev*10+back
print(rev)

print("..............")

#palindrome
rome=121
reverse=0
while rome!=0:
    digit=rome%10
    rome=rome//10
    reverse=reverse*10+digit

if(reverse==121):
    print("It is palindrome")
else:
    print("It is not palindrome")
print("..............")

strings="python"
loop=0
while loop<len(strings):
    print(strings[loop])
    loop+=1

print("..............")





