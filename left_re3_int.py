x = int(input("Enter number of rows: "))
n=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
    n+=1
    print()