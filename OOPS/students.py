import matplotlib.pyplot as plt
students=["Arun","Bina","Chitra","Deepak","Esha"]
marks=[85,90,78,92,88]
plt.title ("Marks of Students")
plt.plot(students,marks)
plt.show()
plt.bar(students,marks)
plt.title("Marks of Students")
plt.show()
plt.pie(marks, labels=students) 
plt.title("Marks of Students")
plt.show()