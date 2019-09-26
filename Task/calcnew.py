# Basic Calculator Programming  
# Using Function And Return Value
def  Add(x,y):
	return x+y
	
def Subtraction (x,y):
	return x-y

def Division (x,y):
	if x>=y:
		return x/y
	else :
		return y/x

def Modulus (x,y):
	if x>=y:
		return x%y
	else :
		return y%x

def recurFactorial(x):
	if x==1:
		return x
	else:
		return x*recurFactorial(x-1)
def main():
	# User Input Details 
	a = int (input ("Enter First Number :"))
	b = int (input ("Enter Second Number :"))
	print "Enter your operation: "
	print "1.Addition"
	print "2.Subtraction"
	print "3.Division"
	print "4.Modulus"
	print "5.Factorial"
	c = int (input("Enter Your Choice : (1/2/3/4/5): "))

	if c==1:
		print "The Addition Two Numbers is :",Add(a,b)

	elif c==2:
		print "The Subtraction Two Numbers is :",Subtraction(a,b)

	elif c==3:
		print "The Division Two Numbers is :",Division(a,b)

	elif c==4:
		print "The Modulus Two Numbers is :",Modulus(a,b)

	elif c==5 :
		print "The Factorial of First Number is: ",recurFactorial(a)

	else :
		print "Invaild Input"
if __name__ == '__main__':
	main()