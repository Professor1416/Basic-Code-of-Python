#Break And Continue Statement

a = 10

while(a <= 20):#(a=10 <= 20) the condition is True; then excute conditional code.
	if(a == 15):#a==15)when... #block of code to be executed if the condition is True
		a = a + 1
		print "in if statement of a is:",a
		continue	 #Continue:-when the loop iterate for the first time the value of i=10, the if statement result will be false, so the else condition 2 is implemented.
		  			 #loop iterates again now i=15; if condition result will be 'True' and the code stop in between and strat new iterate unitl the end condition met. 
					 #Break :- when the loop iterates for first time, the value of i=10, the if statement result will be false, so the else condition is executed.
			 		 #loop iterates again now i=15; if condition result will be 'True' and loop breaks.
	print "the value of a is",a
	a = a + 1 #a++ for this condition 'a <= 20'. value increase upto 20.

#OUTPUT
#//Continue
#the value of a is 10
#the value of a is 11
#the value of a is 12
#the value of a is 13
#the value of a is 14
#in if statement of a is: 16
#the value of a is 16
#the value of a is 17
#the value of a is 18
#the value of a is 19
#the value of a is 20


#//Break
#the value of a is 10
#the value of a is 11
#the value of a is 12
#the value of a is 13
#the value of a is 14
#in if statement of a is: 16












									#Prashant Dasnur