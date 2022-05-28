f=open("question3.txt","r")
for i in f:
    if "delhi" in i:
        a=open("delhi.txt","a")
        a.write(i)
    elif "shimla" in i:
        a=open("shimla.txt","a")
        a.write(i)
    else:
        a=open("other.txt","a")
        a.write(i) 
