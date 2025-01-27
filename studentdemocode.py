class Student:
	def __init__(self,name,rollnum,age):
		self.name=name
		self.rollnum=rollnum
		self.age=age
	def display_details(self):
		print("Name: ",self.name)
		print("Rollnum: ",self.rollnum)
		print("Age :",self.age)
	@staticmethod
	def store_stud_details(studdict,name,regnum,age,marks):
		studdict[regnum]={
			"name":name,
			"age":age,
			"marks":marks
		}
		return studdict
	@staticmethod
	def get_avg_marks(studdict):
		avg_list={}
		for regnum,details in studdict.items():
			marks=details["marks"].values()
			#print("-------------",marks)
			avg_marks=sum(marks)/len(marks)
			avg_list[regnum]=avg_marks
		return avg_list
	def get_topper(studdict):
		avg_list=Student.get_avg_marks(studdict)
		max_score=max(avg_list.values())
		topper=[regnum for regnum,score in avg_list.items() if score==max_score ]
		print(max_score)
		print(topper)
		for reg in topper:
			details=s
			8884
			011tuddict[reg]
			print(f"Reg no. {reg},name: {details['name']},Avg_marks:{max_score}")
		#print(avg_list_f)
studdict={'2023bit507': {'name': 'shruti', 'age': '21', 'marks': {'pp': 80, 'maths': 100, 'dbms': 70}}, '2023bit049': {'name': 'dhanshri', 'age': '22', 'marks': {'pp': 55, 'maths': 100, 'dbms': 98}}, '2023bit023': {'name': 'sahil', 'age': '25', 'marks': {'pp': 100, 'maths': 45, 'dbms': 123}}}
#print(Student.get_avg_marks(studdict))
#num_students=int(input("enter the number of student how wants to store details"))

'''for i in range(num_students):
	name=input("enter name-->")
	num=input("enter regnum-->")
	age=input("enter age-->")
	marks={}
	total_subjects=int(input("entertotal number of subjects-->"))
	for j in range(total_subjects):
		subject=input("enter subject name-->")
		score=int(input(f"enter Marks for {subject}"))
		marks[subject]=score
		#storing details to dictonary
		Student.store_stud_details(studdict,name,num,age,marks)'''
#print(Student.store_stud_details(studdict,name,num,age,marks))
Student.get_topper(studdict)
