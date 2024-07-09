print("\t Games start")
lm=3
lc=3
rm=0
rc=0
k=0
userc=0
userm=0
uc=0
um=0
print("MMMCCCC|---|")
try:
    while True:
        while True:
            print("Left side -> Right side")
            uc= int(input("Enter the no of cannibals: "))
            um=int(input("Enter the no of missionaries: "))
            if um==0 and uc==0:
                print("boat cannot be empty")
            elif (um+uc>2 and lm-um>=0 and lc-uc>=0):
                print("retry")
            else:
                break
        
        lm=lm-um
        lc=lc-uc
        k+=1
        rm=rm+um
        rc=rc+uc
        for i in range(lm):
            print("M",end='')
        for i in range(lc):
            print("C",end='')
        print("|---|",end='')
        for i in range(rm):
            print("M",end='')
        for i in range(rc):
            print("C",end='')
        print("\n")

        if ((lc==3 and lm==1) or (lc==2 and lm==1) or (lc==3 and lm==2) or (rc==3 and rm==1) or (rc==2 and rm==1) or (rc==3 and lm==2)):
            print("Cannibals eat missionaries")
            break
        if (rm+rc==6):
            print("Congrats you won the game!")
            print("Total attempts ", k)
            break

        while True:
            print("Left side <- Right side")
            userc= int(input("Enter the no of cannibals: "))
            userm=int(input("Enter the no of missionaries: "))
            if userm==0 and userc==0:
                print("boat cannot be empty")
            elif (userm+userc>2 and lm-userm>=0 and lc-userc>=0):
                print("retry")
            else:
                break
        
        rm-=userm
        rc-=userc
        k+=1
        lm+=userm
        lc+=userc
        for i in range(lm):
            print("M",end='')
        for i in range(lc):
            print("C",end='')
        print("|---|",end='')
        for i in range(rm):
            print("M",end='')
        for i in range(rc):
            print("C",end='')
        print("\n")

        if ((lc==3 and lm==1) or (lc==2 and lm==1) or (lc==3 and lm==2) or (rc==3 and rm==1) or (rc==2 and rm==1) or (rc==3 and lm==2)):
            print("Cannibals eat missionaries")
            break
        if (rm+rc==6):
            print("Congrats you won the game!")
            print("Total attempts ", k)
            break
            

except EOFError as e:
    print("\n Invalid input, retry")
