#4x4 MATRIX SOLVER - BY MADHURYA

#To display the matrix
def display(a):
    print("\nThe Matrix is : \n")
    print("__________________________")
    for i in range(4):
        for j in range(4):
            if a[i][j]>0:
                print("+{:.2f}".format(a[i][j]),end='  ')
            else:
                print("{:.2f}".format(a[i][j]),end='   ')
        print("\n")
    print("__________________________")   
#To check if it's in row echlon form:
def row_echleon(a):
        if a[1][0]==0:
            if a[2][0]==0 and a[2][1]==0:
                if a[3][0]==0 and a[3][1]==0 and a[3][2]==0:
                    print("\n MATRIX IS CONVERTED INTO ROW ECHELON FORM\n")
                    quit()
#Start of the program:                   
print("_________________________________________________________")
print("\n  *********** MADHURYA HAIT'S DS ASSIGNMENT ***********")
print("_________________________________________________________")
print("\nNOTE : Enter the decimal elements of the Matrix row-wise & separate them with ',' !\n")
r1=eval(input("Enter First Row : "))
r2=eval(input("Enter Second Row : "))
r3=eval(input("Enter Third Row : "))
r4=eval(input("Enter Forth Row : "))
a=[r1,r2,r3,r4]
#Checking if it's a valid 4x4 matrix !
for i in range(4):
    print(a[i])
    if a[i]==(0.0, 0.0, 0.0, 0.0):
        print("\n Your matrix must be of 4x4 Dimention \n")
        quit()       
display(a)
row_echleon(a)
#if pivot is 0 then swap the rows 
if a[0][0]==0:
    if a[1][0]!=0:
        swap=a[0]
        a[0]=a[1]
        a[1]=swap
    elif a[2][0]!=0:
        swap=a[0]
        a[0]=a[2]
        a[2]=swap
    elif a[3][0]!=0:
        swap=a[0]
        a[0]=a[3]
        a[3]=swap
    else:
        print("\n Your matrix must be matrix of 4x4 Dimention \n")
        quit()
pivot=a[0][0]
#solving first column
arr=a[0]
arr2=[]
row=a[1]
row2=[]
row3=[]    
pi=a[1][0]
if pi !=0:
    for k in (arr):
        temp=k/pivot
        arr2.append(temp)
    for s in (arr2):
        temp= (s*pi)
        row2.append(temp)
    i=0
    for l in (row):
        temp2= l - row2[i]
        i+=1
        row3.append(temp2)  
    a[1]=row3     
display(a)
row_echleon(a)
arr3=[]
row=a[2]
row2=[]
row3=[]
pi=a[2][0]
if pi !=0:
    for k in (arr):
        temp=k/pivot
        arr3.append(temp)
    for s in (arr3):
        temp= (s*pi)
        row2.append(temp)
    i=0
    for l in (row):
        temp2= l - row2[i]
        i+=1
        row3.append(temp2)
    a[2]=row3     
display(a)
row_echleon(a)
arr4=[]
row=a[3]
row2=[]
row3=[]
pi=a[3][0]
if pi !=0:
    for k in (arr):
        temp=k/pivot
        arr4.append(temp)
    for s in (arr4):
        temp= (s*pi)
        row2.append(temp)
    i=0
    for l in (row):
        temp2= l - row2[i]
        i+=1
        row3.append(temp2)
    a[3]=row3     
display(a)
row_echleon(a)
#Changing the pivot again 
if a[1][1]==0:
    if a[2][1]!=0:
        swap=a[1]
        a[1]=a[2]
        a[2]=swap
    elif a[3][1]!=0:
        swap=a[1]
        a[1]=a[3]
        a[3]=swap
    else:
        print("\n Your matrix must be matrix of 4x4 \n")
        quit()        
pivot=a[1][1]
#solving second column
arr=a[1]
arr5=[]
row=a[2]
row2=[]
row3=[]
pi=a[2][1]
if pi !=0:
    for k in (arr):
        temp=k/pivot
        arr5.append(temp)
    for s in (arr5):
        temp= (s*pi)
        row2.append(temp)
    i=0
    for l in (row):
        temp2= l - row2[i]
        i+=1
        row3.append(temp2)     
    a[2]=row3    
display(a)
row_echleon(a)
arr6=[]
row=a[3]
row2=[]
row3=[]
pi=a[3][1]
if pi !=0:
    for k in (arr):
        temp=k/pivot
        arr6.append(temp)
    for s in (arr6):
        temp= (s*pi)
        row2.append(temp)
    i=0
    for l in (row):
        temp2= l - row2[i]
        i+=1
        row3.append(temp2)
    a[3]=row3    
display(a)
row_echleon(a)
#Changing the pivot again 
if a[2][2]==0:
    if a[3][2]!=0:
        swap=a[3]
        a[3]=a[2]
        a[2]=swap
    else:
        print("\n Your matrix must be matrix of 4x4 \n")
        quit()       
pivot=a[2][2]
#solving third column
arr=a[2]
arr7=[]
row=a[3]
row2=[]
row3=[]
pi=a[3][2]
if pi !=0:
    for k in (arr):
        temp=k/pivot
        arr7.append(temp)
    for s in (arr7):
        temp= (s*pi)
        row2.append(temp)
    i=0
    for l in (row):
        temp2= l - row2[i]
        i+=1
        row3.append(temp2)
    a[3]=row3    
display(a)
row_echleon(a)
