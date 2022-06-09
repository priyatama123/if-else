#number 22
year=int(input("enter number"))
salary=int(input("enter number"))
if salary>=5:
    bonus=salary*5/100
    total=salary+bonus
    print("total",total)
else:
    print("none")    