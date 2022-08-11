#You have go to school staff get the our class studend details

#get the info after store the student data's (i.e) name,age & percentage in student list

#and so y have store the in three values in the list

#Finally check the percentage is greater than 75% after print the percentage greater than 75% in particular student data's

#PROGRAM


student=[]

student_count=int(input("please tell your Class strangth: "))

for i in range(student_count):
    name,age,percentage = input("Enter the name, age, percentage seprated by space: ").split()
    student.append(name)
    student.append(age)
    student.append(percentage)
print(student)

print("\n***********************************************************************************************************************************")
print("\n\t Student_Name \t\tStudent_Age \t\t Student_Percentage ")
print("\n*********************************************************************************************************************************** \n")

no=1
for j in student:
    if no%3 == 0:
        if int(j)>75:
            print("\t\t",student[no-3],end=" ")
            print("\t\t\t",student[no-2],end=" ")
            print("\t\t\t",j,"\n")
        print()
    no+=1
