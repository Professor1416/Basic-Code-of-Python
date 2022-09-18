#Logical Operator
a = 50
b = 30

#Logical AND

if(not((a > b) and (a != b))): # !(a=50 > b=30) is False && (a=50 != b=30) is True; Therefore this statement is False.
                               # when both statement are True then result will be True.
                               # '!'not is True statement consider False and False statement consider to True.
	print "this statement is true"

else:
	print "this statement is false"

#Logical OR
if ((a < b) or (a != b)): #(a=50 < b=30) is False || (a=50 != b=30) is True; therefore this statement is True.
                          #if one(or both) statement is True then result will be True, Otherwise it returns False.
	print "this statement is true"
else:
	print "this statement is false"


#OUTPUT

#Logical AND
#this statement is false

#Logical OR
#this statement is true




                                              #Prashant Dasnur