def fibonachi(m):
    if m==1 or m==2:
        return 1
    return fibonachi(m-1) + fibonachi(m-2)


k=int(input("value:"))
i=1
res=0
while k != res and k>res:
    res=fibonachi(i)
    i+=1

if k== res:
    print("Is fibonachi")
else:
    print("Is not fibonachi")