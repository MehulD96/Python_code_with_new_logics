#Program to print all prime numbers between an interval

a = int(input("Enter the starting range:"))
b = int(input("Enter the ending range:"))

for i in range (a,b):
	for j in range(2,i+1):
		if i%j==0 and j<i:
			break
		elif(j<i):
			continue
		elif (j==i):
			print("prime no:",i)


############################### OR ####################################


a = int(input("Enter the starting range:"))
b = int(input("Enter the ending range:"))
list = []
for i in range (a,b):
	for j in range(2,i+1):
		if i%j==0 and j<i:
			break
		elif(j<i):
			continue
		elif (j==i):
			list.append(i)