print("\t Game Starts\n")
print("Now the task is to move all of them to right side of the river\n")
print("Rules:1.Boat can carry atmost 2 people\n2.Boat cannot be empty\n3.Cannibal number greater than missionaries then cannibals can eat missionaries")
print('\n')
lm=3
lc=3
rm=0
rc=0
k=0
userC=0
userM=0

print('\nMMMCCC|---|\n')
try:
    while True:
        while True:
            print("Left side->Right side")
            uM=int(input("Enter no of missionaries: "))
            uC=int(input("Enter no of cannibals: "))
            if (uM==0 and uC==0):
                print("Boat cannot be empty")
            elif (uM+uC<=2) and (lm-uM>=0) and (lc-uC>=0):
                break
            else:
                print("Try again") 
        lm-=uM 
        lc-=uC 
        rm+=uM
        rc+=uC
        k+=1
        print("\n")
        for i in range(0,lm):
            print("M",end='')
        for i in range(0,lc):
            print("C",end='')
        print('|---|',end='')
        for i in range(0,rm):
            print("M",end='')
        for i in range(0,rc):
            print("C",end='')
        print("\n")
        if((lc==3 and lm==2) or (lc==3 and lm==1) or (lc==2 and lm==1) or (rc==3 and rm==2) or (rc==3 and rm==1) or (rc==2 and rm==1)):
            print("You lost! Cannibals eat missionaries")
            break
        if rm+rc==6:
            print("You won! Congrats\n")
            print('Total attempts: ',k)
            break
    
        while True:
            print("Right side->Left side")
            userM=int(input("Enter no of missionaries: "))
            userC=int(input("Enter no of cannibals: "))
            if (userM==0 and userC==0):
                print("Boat cannot be empty")
            elif userM+userC<=2 and (rm-userM>=0) and (rc-userC>=0):
                break
            else:
                print("Try again") 
        rm-=userM 
        rc-=userC 
        lm+=userM
        lc+=userC
        k+=1
        print("\n")
        for i in range(0,lm):
            print("M",end='')
        for i in range(0,lc):
            print("C",end='')
        print('|---|',end='')
        for i in range(0,rm):
            print("M",end='')
        for i in range(0,rc):
            print("C",end='')
        print("\n")
        if((lc==3 and lm==2) or (lc==3 and lm==1) or (lc==2 and lm==1) or (rc==3 and rm==2) or (rc==3 and rm==1) or (rc==2 and rm==1)):
            print("You lost! Cannibals eat missionaries")
            break
        if rm+rc==6:
            print("You won! Congrats\n")
            print('Total attempts: ',k)
            break
except EOFError as e:
    print("Invalid input! please try again ")