#number 23
marks=int(input("enter grade"))
if marks>=80 and marks<=100:
    print("grade a")
elif marks<=60 and marks>=80:
    print("grade b")
elif marks<=50 and marks>=50:
    print("grade c")
elif marks>=45 and marks<=60:
    print("grade d") 
elif marks>25 and marks<=45:
    print("grade e")
else:
    print("fail")           