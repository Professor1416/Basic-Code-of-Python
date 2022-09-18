import grade
per = sub1 + sub2 + sub3 + sub4 + sub5 
per2 = per / 5
print "Persentage:-",per2,"%"

if per2 >= 90:
	print "Grade A"

elif per2 >= 80:
	print "Grade B"

elif per2 >= 70:
	print "Grade C"

elif per2 >= 60:
	print "Grade D"

elif per2 >= 40:
	print "Grade E"

else:
	print "Grade F"
