#python program to print the below pattern
#       *    
#      ***
#     *****
#    *******
#   *********


def pattern7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()

n=int(input("enter the n"))
pattern7(n)
