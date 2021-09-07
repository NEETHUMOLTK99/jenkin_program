import sys
from calcu_class_using_sys import cal


while True:
	def menu():
		print("1.Addition")
		print("2.Subtraction")
		print("3.multiplication")
		print("4.Division")
		print("5.Exit")
	menu()	
	arg1 = int(sys.argv[1]) # choice
	arg2 = int(sys.argv[2]) #1st no
	arg3 = int(sys.argv[3]) #2nd no
	a = arg2 # 1st no
	b = arg3 # 2nd no
	
	obj = cal(a,b) # creating object
	if arg1 == 1:
		print("Sum is",obj.add()) # calling add fn
		break
	elif arg1 == 2:
		print("Difference is",obj.sub()) # calling sub fn
		break
	elif arg1 == 3:
		print("Multiplication is",obj.mul()) # calling mul fn
		break
	elif arg1 == 4:
		print("Division is",obj.div()) # calling div fn
		break
	elif arg1 == 5:
		break
	else:
		print("Invalid choice")
