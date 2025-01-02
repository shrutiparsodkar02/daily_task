def sunday():
	return ("sunday")
def monday():
	return ("mon")
def tuesday():
	return ("tuesday")
def default():
	return ("hello shruti")
switcher={1:sunday,2:monday,3:tuesday,4:default}
def switch(days_of_week):
	print("days--->",switcher.get(days_of_week,default)())
switch(8)
