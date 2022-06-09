a=int(input("enter nimber"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a<c or a>b and a>c:
    print("a is second largest number")
elif b>a and b>c or b>a and b>c:
    print("b is second largest number")
elif c>a and c>b or c>a and c>b:
    print("c is second largest number")
else:
    print("it is not second largest number")

