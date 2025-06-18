#1.Python Program to Append an Item to a List
'''
li = [10,20,30]
print(li)
li.append(101)
print(li)
'''

#2.Python Program to access List Index and Values
'''
li = [10,20,30]
print(li[1])
'''

#3.Python Program to add two Lists
'''
li1 = [10,20,30]
li2 = [10,20,30]
new = []
for i in range(len(li1)):
    new.append(li1[i] + li2[i])
print(new)
'''

#4.Python Program to Change List Items
'''
li = [10,20,30]
print(li)
li[1] = 101
print(li)
'''

#5.Python Program for Arithmetic Operations on Lists
'''
n1 = [10,20,30]
n2 = [5,2,3]
add,sub,mul,div,flo,mod,exp = [],[],[],[],[],[],[]
for i in range(len(n1)):
    add.append(n1[i]+n2[i])
    sub.append(n1[i]-n2[i])
    mul.append(n1[i]*n2[i])
    div.append(n1[i]/n2[i])
    flo.append(n1[i]//n2[i])
    mod.append(n1[i]%n2[i])
    exp.append(n1[i]**n2[i])
print("Addition :- ",add)
print("Subtraction :- ",sub)
print("Multiply :- ",mul)
print("Division :- ",div)
print("Floor :- ",flo)
print("Modulus :- ",mod)
print("Exponent :- ",exp)
'''

#6.Python Program to Calculate the Average of List Items
'''
li = [10,15,20,25,30,35,40]
count = len(li)
total = sum(li)
avg = total / count
print("Average :- ",avg)
'''

#7.Python Program to Clear a List
'''
li = [10,20,30]
print(li)
li.clear()
print(li)
'''

#8.Python Program to check List is Empty or Not
'''
li = []
if(li):
    print("List Is Not Empty")
else:
    print("List Is Empty")
'''

#9.Python Program to Check if the Element Exists in a List
'''
li = [10,20,30]
print(li)
ele = int(input("Enter any element :- "))
if(ele in li):
    print("It is present in list")
else:
    print("Not present in list")
'''

#10.Python Program to Clone or Copy a List
'''
li = [10,20,30]
print(li)
print(id(li))
new = li.copy()
print(new)
print(id(new))
'''

#11.Python Program to Count Occurrence of an element in a List
'''
li = [10,20,30,40,50,40,40]
print(li)
print(li.count(40))
'''

#12.Python program to Count Even and Odd Numbers in a List
'''
li = [11,12,13,14,15]
even = odd = 0
for i in li:
    if(i%2==0):
        even += 1
    else:
        odd += 1
print("Even :- ",even)
print("Odd :- ",odd)
'''

#13.Python program to Count Positive and Negative Numbers in a List
'''
li = [11,-12,13,14,15]
positive = negative = 0
for i in li:
    if(i>0):
        positive += 1
    else:
        negative += 1
print("Positive :- ",positive)
print("Negative :- ",negative)
'''

#14.Python program to find Length of a List
'''
li = [10, 20, 30, 40, 50, 40, 40]
print(len(li))
'''

#15.Python program to find the List Difference
'''
li = [1,2,4,6,8,9]
li1 = [1,3,5,7,9,11]
n1 = list(set(li) - set(li1))
n2 = list(set(li1) - set(li))
print(n1+n2)
'''

#16.Python Program to Find the Average of a List
'''
li = [10, 20, 30, 40, 50, 40, 40]
total = sum(li)
count = len(li)
avg = total / count
print("Average :- ",round(avg))
'''

#17.Python Program to Merge Two Lists
'''
li1 = [10,20,30]
li2 = ['a','b','c']
for i in li2:
    li1.append(i)
print(li1)
'''

#18.Python List Multiplication Program
'''
li = [1,2,3,4,5]
mul = 1
for i in li:
    mul *= i
print(mul)
'''

#19.Python program to find the Sum of All List Elements
'''
li = [10,20,30,40]
total = 0
for i in li:
    total += i
print("Sum :- ",total)
'''

#20.Sum and Average of a List.
'''
li = [10, 20, 30, 40]
print(li)
total = sum(li)
count = len(li)
avg = total/count
print("Total :- ",total)
print("Average :- ",avg)
'''

#21.Sum of Even and Odd List Numbers
'''
li = [10,11,12,13,14,15]
even = odd = 0
for i in li:
    if(i%2==0):
        even += i
    else:
        odd += i
print("Sum of even :- ",even)
print("Sum of odd :- ",odd)
'''

#22.Left Rotate a List by n
'''
li = [10,11,12,13,14,15]
print(li)
n = int(input("Enter how many element shift to left :- "))
new = li[n:] + li[:n]
print(new)
'''

#23.Right Rotate a List by n
'''
li = [10,11,12,13,14,15]
print(li)
n = int(input("Enter how many element shift to right :- "))
for i in range(n):
    new = li.pop()
    li.insert(0,new)
print(li)
'''

#24.Remove an item from a List
'''
li = [10,11,12,13,14,15]
print(li)
ele = int(input("Enter element want to remove :- "))
li.remove(ele)
print(li)
'''

#25.Remove the First element from a List
'''
li = [10, 11, 13, 14, 15]
print(li)
li.pop(0)
print(li)
'''

#26.Remove the Last element from a List
'''
li = [10, 11, 13, 14, 15]
print(li)
li.pop()
print(li)
'''

#27.Iterate Over List Items
'''
li = [10, 11, 13, 14, 15]
for i in li:
    print(i)
'''

#28.Interchange First and Last Elements in a List
'''
li = [10, 11, 13, 14, 15]
print(li)
li[0],li[-1] = li[-1],li[0]
print(li)
'''

#29.Swap two items in a List
'''
li = [10, 11, 13, 14, 15]
print(li)
li[1],li[2]=li[2],li[1]
print(li)
'''
















































    
    








































































































