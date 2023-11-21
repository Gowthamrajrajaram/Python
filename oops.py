# object - combination of states and behaviours
# class- template or blueprint

class supermarket:
      """ This is my supermarket""" #documentation string
      def __init__(self):# __init__ is called automatically when the object is created 
        print('This is my constructor')
# constructors is getting called/invoked automatically whenever we create object
soap=supermarket()
soap.brand='Lux'
soap.price=50
soap.discount=25

choclate=supermarket()
choclate.brand='Dairy milk'
choclate.price=100
choclate.discount=10

bread=supermarket()
bread.brand='abc'
bread.price=60
bread.discount=5

print(soap.brand)


print('...........................................')
class superMarket:
    def __init__(self,brand,price,discount):
        self.brand=brand
        self.price=price
        self.discount=discount

soap=superMarket('Lux',50,15)#initializing object specific informaation
bread=superMarket('abcd',60,10)
choclate=superMarket('Dairymilk',100,5)
print(bread.price)
print(choclate.discount)


print('..........................................')

class Supermarket:
    manufacturer='abc manufacuring pvt' #class specific variable
    marketer='gowthem supermarket'
    def __init__(self,brand,price,discount):
        self.brand=brand#instance variable
        self.price=price
        self.dicount=discount

soap=Supermarket('Lux',50,15)
bread=Supermarket('abcd',60,10)
choclate=Supermarket('Dairymilk',100,5)
rice=Supermarket('Ponny',1000,25)
rice.manufacturer='abc rice mill'
print(rice.brand)
print(Supermarket.manufacturer)# we can access class specific variable using classname
print(Supermarket.marketer)
print(rice.manufacturer)#we can access class using object and also modify the object specific information

print('..........................................')

# Functions - Methods
# Types of Methods
# 1.instance method
# 2.class method
# 3. static method

#1.instance method
class student:
    def __init__(self,name,mark):
        self.name=name
        self.marks=mark
    def display(self):#instance method
        print('Hi',self.name,'your mark is',self.marks)

student1=student('Gowtham',97)
student1.display()

#2. class method

class office:
    noofholidays=10
    @classmethod #decorators
    def checkholidays(cls,branch):
        print('This is our branch',branch,'has',cls.noofholidays)

office.checkholidays('chennai')

#3. static method
class calculator:
    @staticmethod
    def add(num1,num2):
        print('result is',num1+num2)
calculator.add(100,200)

print('.................................')
#inhritance- an object of one class behaving as an object of another class
#has relationship
#car has engine

class engine:
    milage=20
    def __init__(self):
        self.petrol=True

    def enginestart(self):
        print('Engine smooth starting')

class car:
    def __init__(self):
        self.engine=engine()

    def drive(self):
        print(self.engine.milage)
        self.engine.enginestart()

KIA=car()
KIA.drive()

print('....................................')
# is relationship
# parent child relationship

class vasanthandco:#parent class or superclass
    branch='vadapalani'
    def __init__(self):
        self.headoff_offer=1000
    
class vasanthandcomadurai(vasanthandco):#child class or sub class
    branch="Madurai"
    def __init__(self):
        super().__init__() # accesing a parent class constructor
        self.branchoff_offer=500

customer=vasanthandcomadurai()
print(customer.headoff_offer)
print(customer.branch)

print('....................................')

class humanbeing:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def activity(self):
        print("Reading books")

class employee(humanbeing):
    def __init__(self,name,emp_no,salary):
        super().__init__(name,22)
        self.name=name
        self.empno=emp_no
        self.salary=salary
    
    def dowork(self):
        print("working")

    def emp_details(self):
        print(self.name)
        print(self.empno)
        print(self.salary)

employee1=employee('Gowtham',120,20000)
employee1.dowork()
employee1.emp_details()
employee1.activity()

print('....................................')
#Types of inheritance
# 1.single inheritance - a subclass inherits from a single superclass
# 2.mutiple inheritance - a subclass can inherit from multiple superclasses
# 3.multilevel inheritance - a class inherits from another class, which in turn inherits from another class
# 4.Hierarchical Inheritance - multiple classes inherit from a single superclass
# 5. Hybrid inheritance -  a combination of two or more types of inheritance

#1.single inheritance


# 2.mutiple inheritance 
class father:
    def drawing(self):
        print('father drawing')

class mother:
    def goingtojob(self):
        print('mother going to job')

class child(father,mother):
    def studying(self):
        print('child is studying')

family=child()
family.studying()
family.drawing()
family.goingtojob()


print('...............................')
#3. multilevel ineritance
class grandparent:
    def agriculture(self):
        print('Watering a plants')

class parent(grandparent):
    def reading(self ):
        print('reading a books')

class child(parent):
    def excercise(self):
        print('doing excercise daily')

c=child()
c.agriculture()
c.reading()
c.excercise()
print('.......................................')
# 4.Hierarchical Inheritance
class Honda:
    def givesalary(self):
        print('Honda salary')

class Bikes(Honda):
    def designbikes(self):
        print('Honda bikes')

class cars(Honda):
    def designcars(self):
        print('Honda cars')

emp1=cars()
emp1.givesalary()
emp1.designcars()
emp2=Bikes()
emp2.designbikes()

print('....................................')
# 5. Hybrid inheritance

#using super() acessing all types of methods(static,class,instance method)
# super() - superclass -class level variable , superclass  - instance variable
#super() - from child class constructor and child class instance method
# from child class, class methods - accessing parent class instance method and constructors using super() is not working
class parent:
    i=10  #class variable
    def __init__(self):
        self.j=50

    def test(self):
        print('Testing in super class')

    @staticmethod
    def test1():
        print('parent static method')

    @classmethod
    def test2(cls):
        print('parent class method')
    

class C(parent):
    def __init__(self):
        super().__init__()
        super().test()
        super().test1()
        super().test2()

    def m1(self):
        print(super().i)
        print(self.j)
        super().test()
        super().test1()
        super().test2()
    
    @classmethod
    def display(cls):
        super(C,cls).test(cls)

c=C()
c.m1()
c.display()

print('.................................')
# polymorphism - many forms

# operator overloading
# method overloading
# constuctor overloading

# operator overloading
class book:
    def __init__(self,pages):
        self.page=pages
    
    def __add__(self,other):
        return self.pages + other.pages

thirukkural=200
thiruvasagam=150
print(thirukkural+thiruvasagam)

print('...................................')

class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def __gt__(self,other):
        return self.price> other.price

m1=mobile('vivo',15000)
m2=mobile('samsung',20000)
print(m1>m2)

print('.........................................')

class mobile:
    def __init__(self,brand,price,offer):
        self.brand=brand
        self.price=price
        self.offers=offer

    def __gt__(self,other):
        return self.price> other.price
    
    def __add__(self,other):
        return self.offers + other.ccoffer

class creditcard:
    def __init__(self,brand,ccoffer):
        self.brand=brand
        self.ccoffer=ccoffer


m1=mobile('vivo',15000,1000)
m2=mobile('samsung',20000,1500)
cc=creditcard('vivo',500)
print(m1+cc)

print('........................................')
# method overloading - same method name with different no of arguments
#method overloading allows you to define multiple methods with the same name in a class, but with different parameter lists
class test:
    def calculate(self, *no):
        total=0
        for i in no:
            total=total+i
        print(total)

t=test()
t.calculate(10,20)
t.calculate(10,20,30)

print('.............................................')
#constructor overloading  - constructor overloading allows you to define multiple constructors with different parameter lists within a class
class supermarkets:
    def __init__(self,*content):
        print("constructor check")

obj1=supermarkets('soap',20,2)
obj2=supermarkets('rice',60)

print('...............................')

#method overriding - subclass to provide a specific implementation for a method that is already defined in its superclass.

class parent:
    def study(self):
         print("Engg or Medical")

class child(parent):
    def play(self):
        print("playing kabadi")

    def study(self):
        print("Humanities / science")

c=child()
c.study()

print('.........................................')

#constuctor overriding - subclasses by using the super() function 

class parent:
    def __init__(self):
        print('parent class constructor')
    def study(self):
         print("Engg or Medical")

class child(parent):
    def __init__(self):
        super().__init__()
        print('child class constructor')

    def play(self):
        print("playing kabadi")

    def study(self):
        print("Humanities / science")

c=child()
c.study()

print('...........................................')

#abstraction - showing only the necessary data and hiding unwanted
#abc - abstract base class
from abc import *






print('.............................................')

#encapsulation - databinding

class Test:
    a=100
    _b=200 #_ protect
    __c=300 # __private
    def __init__(self):
        self.__no=1234
    def display(self):
        print(self.a)
        print(self._b)
        print(self.__c)

t=Test()
#t.display()
print(Test._b)
print(t._Test__no) # using this type accessing a private variable outside class