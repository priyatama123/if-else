month=input("enter month")
day=int(input("enter day"))
if month in ("dec","janu","feb"):
    if day<=31 or day<=28:
        print("winter")
    elif month in ("march","april","may"):
        if day<=31 or day<=30:
            print("spring")
    elif month in ("june","july","aug"):
         if day<=31 or day<=30:
            print("summer")
elif month in ("sep","oct","nov"):
            if day<=31 or day<=30:
                print("autumn")
            
else:
    print("none")                 
