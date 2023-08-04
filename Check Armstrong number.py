#Program to identify if a number is an Armstrong number

a = input("Enter 1st number:") 		#take input, input s a string not integer
count = c = 0				#initialise variables
for i in a:
	i= int(i)			#start for loop on string and convert 'i' into integer
					 to perform calculation because  calculation can not be done on string
	if count > (b:=len(a)):		#walrus operator is used with 'b' 
		break
	c= c + pow(i,b)			#calculate sum of the digits of number
	
	count+=1
print(c)
if c== int(a):					#if the sum is equal to the input number it is armstrong number
	print("it is a armstrong number:")
else:
	print("not an armstrong numb.")