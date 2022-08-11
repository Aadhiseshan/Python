###Explain  the List Properties?
##
###==> List is a Compound d/t
##
###==> List indicated with [ ] square brackets, seprated by comma(,)
##
###==> List is mutable d/b
##
###==> List can contain 'n' no of elements
##
###==> List can contain hetro-geneous d/t
##
###==> List allowed duplicate values
##
###==> List maintain insertion order

#=====================================================================================================#

###How to create a list?

li=["Aadhi",123,True]

print(type(li))

print(li)

#=====================================================================================================#

#create a list using slice operator?

name=["raja","roja",'ravi',123,'Kumar']

#using index operator

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

#using slice opertaor

print(name[0:3])  #in this method is used to print 0th possition value to 3rd possition value

print(name[:])  #in this slice operator is print the full list value

#=====================================================================================================#


#List Functions

##1) append(item)
##2) insert(index,element)
##3) remove(item)
##4) pop(index)
##5) clear()
##6) extend(list)
##7) count()
##8) reverse()
##9) copy()
##10) index(element)
##11)sort()



#Create a Empty list

lst=[1,2,4,5,6,8,6,4,2,2,9,10]

#1) append()
#This append() function is used to add the value list in last possition

print(lst)
lst.append(20)
print(lst)

#2) insert(index,element)

print(len(lst))

lst.insert(0,'aadhi')

print(lst)

#3) remove(item)

lst.remove(4)
print(lst)

#4) pop(index)

lst.pop(6)
print(lst)

#5) clear()

lst.clear()
print(lst)

#6) extend(list)

name=['ram','ravi','kanna']

lst.extend(name)
print(lst)

#7) count()
count=lst.count(2)
print(count)

#8) reverse()
lst.reverse()
print(lst)

#9) index(element)
ind=lst.index(10)
print(ind)

#10) sort()
lst.sort()
print(lst)

#11) copy()
name=['ravi','raj','ram']
name=lst.copy()
print(name)

#=====================================================================================================#

Nested list

create a Nested list

A=[1,2,3,'ram','ravi','prabu','kanna','p','u','o','1','7']
B=['Aadhi','Vicky','Ponnarasu','kavi',5,6,4,6,'b','k','35621']

tenth=[A,B]

print(tenth)
no=0

 #Using loop statement print the list

while loop

while no<len(tenth):
    print(tenth[no])
    no+=1

for loop
for i in tenth:
    print(i)


#using loop statement print inside the list items

while loop

while no<len(tenth):
    i=0
    while i<len(tenth[no]):
        print(tenth[no][i])
        i+=1
    print()
    no+=1

 for loop

for i in range(len(tenth)):
    for j in range(len(tenth[i])):
        print(tenth[i][j])
    print()

#========================================================================================================#

#print the list items in only string's or print only alphabets

#for loop

for i in range(len(tenth)):
    for j in range(len(tenth[i])):
        if type(tenth[i][j]) == str and tenth[i][j].isalpha() :
            print(tenth[i][j])
    print()


#while loop

i=0
while i<len(tenth):
    j=0
    while j<len(tenth[i]):
        if type(tenth[i][j]) == str and tenth[i][j].isalpha():
            print(tenth[i][j])
        j+=1
    print()
    i+=1

#==========================================================================================================#
#Get the value in user print the two power numbers

no=int(input("Enter the any no: "))
square=[]

for i in range(no+1):
    square.append(i ** 2)
    print(square)
#=====================================================================================================#

#write the program on how to get the data and store the list

total_stud=int(input("Enter the Student Strength: "))

Data=[]

i=0
while i<total_stud:
    name=input("Enter the Student Name: ")
    Data.append(name)
    i+=1
print(Data)

