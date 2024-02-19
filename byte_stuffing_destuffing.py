def byteStuffing(n):
    ns=""
    for i in n:
        if i=="E" or i=="F":
            ns+="E"
        ns+=i

    ns="F"+ns+"F"
    return ns

def byteDeStuffing(n):
    os=""
    for i in range(1,len(n)-1):
        if not (n[i]=="E" and (n[i+1]=="E" or n[i+1]=="F")):
            os+=n[i]
        if n[i]=="E" and i==len(n)-2:
            os+=n[i]

    return os

os=input("Enter the Original Frame : ")
bs=byteStuffing(os)
print("The Byte Stuffing of ",os," is ",bs);

bs=input("Enter the ByteStuffed Frame : ")
os=byteDeStuffing(bs)
print("The Original String of ",bs," is ",os)
