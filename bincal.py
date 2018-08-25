import math

x=int(input('Enter the number in base 10: '))
rem=[]

while(x/2>0):
	rem.append(x%2)
	x=x/2
	x=math.floor(x)

rem=rem[::-1]

print('\nThe given number in base 2 is: ', end='')

for i in rem:
	print(i, end='')
print()



