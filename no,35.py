c_p=int(input("enter number"))
if c_p>100000:
    print("tex",c_p*15/100)
elif c_p>50000 and c_p<=100000:
    print("tex",c_p*10/100)
elif c_p<=50000:
    print("tex",c_p*5/100)
else:
    print("no tex")