##f=open("/home/aadhiseshan/Desktop/new.txt","r")
##
##print("file name is:",f.name)
##
##print("File Mode is:",f.mode)
##
##print("File Propertity is:",f.readable())
##
##print("File Propertity is:",f.writable())
##
##print("File is closed:",f.closed)
##
##f.close()
##
##print("File status is:",f.closed)

file=open("/home/aadhiseshan/Desktop/new.txt","r")

#####add the sentence
##file.write("HI \n")
##file.write("Friends \n")
##file.write("How \n")
##file.write("r \n")
##file.write("u \n")
##
##
###add the list in the text file
##name=['aadhi ','kavi ','ravi']
##file.writelines(name)
##file.close()


output=file.readlines()
info=" ".join(output)
print(output)
file.close()

print("\n File status is closed:",file.closed)

print("\n Go to open a file")
