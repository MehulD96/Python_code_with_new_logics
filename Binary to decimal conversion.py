#Program in Python to convert Binary number to decimal 


a= input("enter binary number:")         #input() gives string a has string value in it
b= a[::-1]                                  #reversing the string and storing it in 'b'
count = 0
ans = 0                                      #initialise 2 variable 'count'&'ans'

'''now we will run a for loop to get the reverse binary number(current string)
to implement the binary to decimal conversion logic{ ex- 1011 to decimal will work as -
1*2^3+0*2^2+1*2^1+1*2^0} we reversed the string because to implement the correct power of base 2 
with binary numbers. it can also be done without reversing it.'''

for i in b:             #b is the reverse string, b here can also be written as "range(len(b))"
    str_len=len(a)      #calculate the length of the string
    c=int(i)            #converting string to integer so that the calculation can be performed

'''check is applied- if the count(number of times a for loop runs) because we need this number
so that we can implement it with the power of 2. it can also be obtained with enumerate(). so if the length
 of count of for loop equals the length of string it breaks'''
    if count==str_len: 
        break
    ans=c*pow(2,count)+ans      # the mathematical formula to convert binary to decimal 
    count += 1                  # increment the count

print("answer is:",ans)         #print the answer
