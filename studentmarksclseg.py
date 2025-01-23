class Student:
	def __init__(self,n,m):
		self.name=n
		self.marks=m
	def display(self):
		print("hi",self.name)
		print("your markss are-->",self.marks)
	def calculate_grade(self):
		if self.marks >= 600:
			print("Grade A")
		elif self.marks<600 or self.marks>400:
			print("yougot B grade ")
		elif self.marks <400 or self.marks>200:
			print("grade C")
n=eval(input("enter the number of students mark you want"))
i=0
while i<n:
	name=input("enter your name ")
	marks=eval(input("enter your total marks"))
	s=Student(name,marks)
	s.display()
	s.calculate_grade()
	print("*"*50)
	i+=1
