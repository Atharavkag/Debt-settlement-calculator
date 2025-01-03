#This code does not contain GUI 
def org(transistionlist):
    status={}
    for bnam,indic in transistionlist.items():
        if bnam not in status:
            status[bnam]=0
        for lnam ,paisa in indic.items():
            if lnam not in status:
                status[lnam]=0
            status[bnam]-=paisa
            status[lnam]+=paisa
    return status
def portion(status):
    positive=[]
    negative=[]
    for nam,balance in status.items():
        if balance>0:
            positive.append((nam,balance))
        elif balance<0:
            negative.append((nam,balance))
    trans=[]
    while positive and negative:
        lnam,lbalance=positive[0]
        bnam,bbalance=negative[0]
        trans_amount=min(lbalance,bbalance)
        trans.append((bnam,lnam,trans_amount))
        positive[0]=(lnam,lbalance-trans_amount)
        negative[0]=(bnam,bbalance-trans_amount)
        if positive[0][1]==0:
            positive.pop(0)
        if negative[0][1]==0:
            negative.pop(0)
    return trans

trans={}

n=int(input("enter the number of people involved:"))
person=[]
for i in range(n):
    name=input(f"enter the name of person{i+1}:")
    person.append(name)
    trans[name]={}
for i in person:
    num_lnam=int(input(f"enter the number of people who gave money to {i}:"))
    for _ in range(num_lnam):
        lnam=input(f"enter name of lender for {i}:")
        amount=int(input(f"enter the amount {lnam} gave to {i}:"))
        trans[i][lnam]=amount
organize=org(trans)
settle=portion(organize)

print("\nSimplified Balances:")
for nam,bal in organize.items():
    if bal>0:
        print(f"{nam} is owed ${bal}")
    elif bal<0:
        print(f"{nam} is owes ${bal}")
    else:
        print(f"{nam} is settled")
    
print("\noptimal settlements")
if settle:
    for bnam,lnam,amount in settle:
        print(f"{bnam} should pay ${amount} to {lnam}")
else:
    print("every one is settled!!!!")
        
'''5
A 2 t1 t2
B 1 t1
C 1 t1
D 1 t2
E 1 t2
4
B A 300
C A 700
D B 500
E B 500

--------

5
A 2 t1 t2
B 1 t1
C 1 t1
D 1 t2
E 1 t2
4
B A 300
C A 700
D B 500
E B 500

--------------------

6
B 3 1 2 3
C 2 1 2
D 1 2
E 2 1 3
F 1 3
G 2 2 3
9
G B 30
G D 10
F B 10
F C 30
F D 10
F E 10
B C 40
C D 20
D E 50'''