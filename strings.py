string='gowthamraj'
print(string[5])
print(string[2])
print(string[9])
print(string[0])

print('#length')

print(len(string))

print('space removing')
#remove space
#rstrip() To remove space at right hand side
#lstrip() To remove space at left hand side
#strip() To remove space at both side
string_city=' hydrabad '
print(string_city.rstrip())
print(string_city.lstrip())
print(string_city.strip())

print('find')
#forbackward direction
#rfind() - returns the rightmost index of the substring if found in the given string. If not found then it returns -1
#rindex
#find
sub='I am using a laptop to work'
print(sub)
print(sub.find('am'))
print(sub.rfind('i'))
print(sub.rindex('u'))

print('#casefold')
#casefold() method is used to convert string to lowercase.
string="GOWTHAMRAJ"
print(string.casefold())

print('#count')
#count
str_count='abcdabcdabcdabcd'
print(str_count.count('a'))
print(str_count.count('d'))

print('#replacing')

#replacing
subs=sub.replace('laptop','computer')
print(subs)

print('#spliting')
#spliting

bad=sub.split()
for i in bad:
    print(i)

print('#joining')
#joining

name=('gowtham','mano','kavin')
jo='>'.join(name)
print(jo)

print('# changing case of string')
# changing case of string

#upper 
#lower
#swapcase upper will be lower and lower will be upper
#title first char in every word
#capitalize first char of str
names='Python is very Easy'
print(names.upper())
print(names.lower())
print(names.swapcase())
print(names.title())
print(names.capitalize())

print('#startswith #endswith')

#startswith
#endswith

print(names.startswith('l'))
print(names.startswith('P'))
print(names.endswith('l'))
print(names.endswith('y'))

print('checking')

print('gowtham25'.isalnum())
print('gowtham25'.isalpha())
print('gowtham'.isalpha())
print('2563'.isdigit())
print('GOWTHAM'.isupper())
print('gowtham'.islower())
print('Learning'.istitle())
print(' '.isspace())

print('#formating')

#formating
name='gowtham'
salary=10000
age=22
print("{} 's salary is {} and his age is {}".format(name,salary,age))
print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))

print('#isalnum')

names='Hariraj123'
print(names.isalnum())

#isalpha
print(names.isalpha())
print(name.isalpha())
#isdecimal
num='1223'
print(names.isdecimal())
print(num.isdecimal())
#isdigit
expr="44²"
print(expr.isdigit())
print(num.isdigit())
#isnumeric
number='⅓'
print(number.isnumeric())

#isidentifier -It only consists of alphanumeric characters and underscore (_)
#Doesn’t start with a space or a number
id='Gowtham_25'
ids=' mano_25'
print(id.isidentifier())
print(ids.isidentifier())


