#pattern8
# *********
#  *******
#   *****
#    ***
#     *
def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(n*2-i*2-1):
            print("*",end="")
        for l in range(i):
            print(" ",end="")
        print()

n=int(input("enter the n"))
pattern8(n)

