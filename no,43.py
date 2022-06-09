age=int(input("enter age"))
sex=input("enter sex")
day=int(input("enter day"))
if age>=18 and age<=30 and sex=="m":
    wages=day*700
    print("wages",wages)
elif age>=18 and age<=30 and sex=="f":
    wages=day*750
    print("wages",wages)
elif age>=30 and age<=50 and sex=="m":
    wages=day*800
    print("wages",wages)
elif age>=30 and age<=40 and sex=="f":
    wages=day*850
    print("wages",wages)
else:
    print("none")        
