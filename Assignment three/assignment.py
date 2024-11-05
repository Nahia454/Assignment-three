student_names=['Sandra','Patricia','Phionah','Anita',]
student_marks=[80,56,78,90]
data=['Sandra','Patricia','Phionah','Anitah']

student_names.insert(2,'faith')
print(student_names)


#print patricia,Faith,Phionah and Anitah
print(student_names[1])
print(student_names[2])
print(student_names[3])


# Add Marsha at the forth position
student_names.append('masha')
print(student_names)

print(student_names[-4])
print(student_names[-3])
print(student_names[-2])
print(student_names[-1])


#Update the name Phionah to Phionah Aladina
student_names[3]='phionah Aladina'
print(student_names)

#Display the length of the students
print("Number of student_names:",len(student_names))


# Print the students name using a 4loop
for names in student_names:
   print (student_names)


# calculate the total mark for the student mark 
student_marks=[80,56,78,90]

def student_marks(sum):
    sum=(80+56+78+90)
    print(f"The student_marks:sum{80,56,78,90}")
student_marks()