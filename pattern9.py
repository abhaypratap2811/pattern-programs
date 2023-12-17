#pattern9
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pattern9(n):
    for i in range(2*n-1):
        stars= 2*n-i if i>n else i
        for j in range(1,stars):
            print("*",end="")
        print()

n=int(input("enter the n"))
pattern9(n+1)

