
#number 2 question
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>c and a<b:
    print(a,"is second lergest")
elif c<a and c>b:
    print(c,"is second leargest")
elif b>a and a>c:
    print(b,"is second leargest")
else :
    print("not second leargest")   