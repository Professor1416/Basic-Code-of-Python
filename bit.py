#Birwise Operator

a = 50 #00110010 in binary. 
b = 30 #00011110 in binary.
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

#Bitwise AND
c = a & b #00110010 & 00011110 = 00010010 i.e means is '18'.
print ("the value of (a & b):",c)

#Bitwise OR
d = a | b #00110010 | 00011110 = 00111110 i.e means is '62'.
print ("the value of (a | b):",d)

#Bitwise Exclusive XOR
e = a ^ b # 00110010 ^ 00011110 = 00101100 i.e means is '44'.
print ("the value of (a ^ b):",e)

#Bitwise Complement
f = ~a # -(50+1)= i.e means is '-51'.
print ("the value of (~a):",f)

#Bitwise Complement
g = ~b # -(30+1)= i.e means is '-31'.
print ("the value of (~ b):",g)

#Bitwise Shift Left
h = a << 2 #50=00110010 << 2 :- 11001000 i.e means is '200'.
           #Shift with 2 zero to left side.
print ("the value of (a << 2):",h)

#Bitwise Shift Right
i = a >> 2 #50=00110010 >> 2 :-  001100 i.e means os '12'.
           #Shift with 2 zero to right side.
print ("the value of (a >> 2): ",i)

#Output
#the value of (a & b): 18
#the value of (a | b): 62
#the value of (a ^ b): 44
#the value of (~a): -51
#the value of (~ b): -31
#the value of (a << 2): 200
#the value of (a >> 2):  12





                                    #Prashant Dasnur