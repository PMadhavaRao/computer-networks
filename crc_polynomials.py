def getRealData(rn,k):
    n=rn+"0"*(len(k)-1)
    ws=len(k)
    ans=n[:ws]
    for i in range(ws,len(n)):
        add=n[i]
        if len(ans)==ws:
            temp=ans
            ans=""
            for i in range(ws):
              res=str(int(k[i])^int(temp[i]))
              ans+=res
            ans=str(int(ans))
        ans=ans+add
    ans=str(int(ans)^int(k))
    if ans!="0":
        op=rn+"0"*(ws-len(ans)-1)+ans
    else:
        op=rn+"0"*(ws-1)
    return op
def receiver(rn,k):
    n=rn
    ws=len(k)
    ans=n[:ws]
    for i in range(ws,len(n)):
        add=n[i]
        if len(ans)==ws:
            temp=ans
            ans=""
            for i in range(ws):
              res=str(int(k[i])^int(temp[i]))
              ans+=res
            ans=str(int(ans))
        ans=ans+add
    ans=str(int(ans)^int(k))

    if ans!="0":
        print("Correct Data not received")
    else:
        print("Correct Data received")
        
n=input("Enter the Data : ")
k=input("Enter the Key : ")

ans=getRealData(n,k)                                                                     

print("Real Data is ",ans)
check=input("Enter Data : ")
key=input("Enter Key : ")
receiver(check,k)
