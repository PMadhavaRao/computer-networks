n=input('enter the data')
bn=''
cnt=0
def bit_stuffing(n,bn,cnt):
    for i in n:
        bn+=i
        if i=='1':
            cnt+=1
        else:
            cnt=0
        if cnt==5:
            bn+='0'
            cnt=0
    print("the byte stuffing string is",bn)
def destffing(n,bn,cnt):
    for i in n:
        if cnt<5:
            bn+=i
        else:
            cnt=0
        if i=='1':
            cnt+=1
        else:
            cnt=0
    print('the dstuffing is ',bn)

bit_stuffing(n,bn,cnt)
destffing(n,bn,cnt)
            
