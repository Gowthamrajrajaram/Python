prac_list=[44,55,888,56,756,123]
#len
print(len(prac_list))
print("....................................................")
#count
new_list=[1,2,3,51,1,1,2,2,2,3,4]
print(new_list.count(1))
print(new_list.count(2))
print(new_list.count(3))
print(new_list.count(4))
print(new_list.count(5))
print("....................................................")

#index
print(new_list.index(1))
print(new_list.index(3))
print(new_list.index(51))
print(new_list.index(2))
print(new_list.index(4))

print("....................................................")
#append 
old_list=[]
old_list.append(1)
old_list.append(50)
old_list.append(100.1)
old_list.append("gowtham")
print(old_list)

print("....................................................")
#insert
num_list=[20,30,40,50]
num_list.insert(0,10)
num_list.insert(5,60)
print(num_list)

print("....................................................")
#extend
list1=[10,20,30,40,50]
list2=["gowtham","mano","kavin"]
list1.extend(list2)
print(list1)

print("....................................................")

#remove
list1.remove(10)
print(list1)

print("....................................................")
#pop
print(list1.pop(1))
print(list1.pop())
print(list1.pop(2))
print(list1)

print("....................................................")
#reverse

list2.reverse()
print(list2)

print("....................................................")
# sort
sort_list=[20,45,89,1,56,10]
sort_list2=["vimal","gowtham","thuli","premi"]
sort_list.sort()
sort_list2.sort()
print(sort_list)
print(sort_list2)

print("....................................................")

#concatenation
lista=[1,2,3]
listb=[4,5,6]
listc=lista+listb
print(listc)

print("....................................................")
# repetition 
print(lista*3)
print(listb*2)

print("....................................................")
#clear
print(lista.clear())

print("....................................................")