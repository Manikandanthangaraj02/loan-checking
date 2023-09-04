a=int(input())
b=int(input())
if(a>=20000 or b<=25):
    loanamount=int(input("give required loan amount:"))
    if(loanamount<=50000):
        print("eligible for loan")
    elif(loanamount>50000):
        print("maximum loan amount is 50000")
else:
    print("not eligible for loan")
