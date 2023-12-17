# 1
# 01
# 101
# 0101
# 10101

def pattern10(n):
    start=1
    for i in range(1,n+1):
        start= 1 if i%2==0 else 0
        for j in range(1,i):
            print(start,end="")
            start=1-start
        print()

n=int(input("enter the n"))
pattern10(n)

