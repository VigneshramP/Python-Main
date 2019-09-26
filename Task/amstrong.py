def main():
	a = b = input ("Enter the number whether it is check AMSTRONG or NOT: ")
	total =0 
	while (b>0):
		reminder = b%10;total = total + (reminder**3)
		b = b/10
	if a==total : print "it is AMSTRONG"
	else : print "it is NOT AMSTRONG"
if __name__ == '__main__':
	main()