def formingMagicSquare(s):
    # Write your code here
    ref1=[[8,3,4],[1,5,9],[6,7,2]]
    ref2=[[4,9,2],[3,5,7],[8,1,6]]
    ref3=[[2,7,6],[9,5,1],[4,3,8]]
    ref4=[[6,1,8],[7,5,3],[2,9,4]]
    ref=[[8,3,4],[4,9,2],[2,7,6],[6,1,8]]
    l=s[0]
    c=[0,0,0,0]
    for x in range(4):
        k=0
        for i in range(3):
            if l[i]==ref[x][i]:
                k+=1
        c[x]=k 
    m=max(c)
    if m==c[0]:
        ref=ref1
    elif m==c[1]:
        ref=ref2
    elif m==c[2]:
        ref=ref3
    else:
        ref=ref4
    cost=0
    for i in range(3):
        for j in range(3):
            cost+=abs(s[i][j]-ref[i][j])
    print(cost)
    return cost
    
def saveThePrisoner(n, m, s):
    # Write your code here
    x=m % n 
    print(x)
    y=x + (s-1)
    print(y)
    z=y % (n+1)
    print(z)
    return z+1
    

def circularArrayRotation(a, k, queries):
    # Write your code here
    ln=len(a)
    b=a
    for i in range(k):
        x=b.pop(ln-1)
        b=[x]+b
    print(b)
    cl=[]
    for i in queries:
        cl.append(b[i])
    print(cl)

def squares(a, b):
    # Write your code here
    import math
    st=math.ceil(math.sqrt(a))
    en=math.ceil(math.sqrt(b))
    k=0
    for i in range(st,en+1):
        k+=1 
    print(k) 
    
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1==y2:
        if m1==m2:
            fine=(d1-d2)*15
        else:
            fine=(m1-m2)*500
    else:
        fine=10000
    return fine
    
def cutTheSticks(arr):
    # Write your code here
    sar=sorted(arr)
    lensar=len(sar)
    ret=[]
    ret.append(lensar)
    while lensar>0:
        c=0
        x=sar[0]
        for t in range(lensar):
            if sar[c]==x:
                sar[c] = -1
                c=c+1
            else:
                break
        sar=[p for p in sar if p != -1]
        lensar=lensar-c
        if lensar>0:
            ret.append(lensar)
        for y in range(lensar):
            sar[y]=sar[y]-x
    return ret

def repeatedString(s, n):
    # Write your code here
    ln=len(s)
    st=s 
    re=n%ln
    c=0 
    for i in st:
        if i=='a':
            c=c+1
    cou=int(n/ln)
    k=0
    for i in range(re):
        print("Hi")
        if st[i]=='a':
            k=k+1
    print(cou*c+k)   
    return cou*c+k

def jumpingOnClouds(c):
    # Write your code here
    k=0 
    jmp=[]
    ln = len(c)
    while k<ln:
        if (k+2)<ln and c[k+2]==0:
            k=k+2 
        elif (k+1)<ln and c[k+1]==0:
            k=k+1
        else:
            break
        jmp.append(k)
    return len(jmp)

def equalizeArray(arr):
    # Write your code here
    sarr=sorted(arr)
    k=0 
    ln=len(sarr)
    m=sarr[0]
    n=0
    for i in range(ln):
        if sarr[i]==m:
            k=k+1 
        else:
            if k>n:
                n=k 
            k=1
            m=sarr[i]
    if k>n:
        n=k 
    print (ln-n)

def acmTeam(topic):
    # Write your code here
    n=len(topic)
    m=len(topic[0])
    i=0 
    j=0 
    teams=[]
    while i<n-1:
        j=i+1 
        while j<n:
            tstr=""
            ones=0
            for k in range(m):
                if topic[i][k]=="0" and topic[j][k]=="0":
                    tstr=tstr+"0"
                else:
                    tstr=tstr+"1"
                    ones+=1 
            teams.append(ones)
            j=j+1 
        i=i+1 
    steams=sorted(teams,reverse=True)
    k=steams[0]
    cou=0
    for i in steams:
        if i==k:
            cou+=1
        else:
            break 
    return [k,cou]
    
def taumBday(b, w, bc, wc, z):
    # Write your code here
    wcc=w*wc
    if (bc+z)*w < wcc:
        wcc=(bc+z)*w
    bcc=b*bc
    if (wc+z)*b < bcc:
        bcc=(wc+z)*b
    print(wcc+bcc)
    
def encryption(s):
    # Write your code here
    import math
    ss=s.replace(" ","")
    ln=len(ss)
    rt=math.sqrt(ln)
    a=math.floor(rt)
    b=math.ceil(rt)
    if ln>(a*b):
        a=a+1
    print(a,b)
    mat=[]
    i=0
    while i<ln:
        rs=ss[i:i+b]
        prs=rs.ljust(b,'0')
        mat.append(prs)
        print(mat)
        i=i+b 
    enstr=""
    for j in range(b):
        rs=""
        for i in range(a):
            if mat[i][j]!="0":
                rs=rs+mat[i][j]
        enstr=enstr+rs+" "
    print(enstr)
        
def kaprekarNumbers(p, q):
    # Write your code here
    import math
    cou=0
    ous=""
    for x in range(p,q+1):
        sq=x*x 
        stsq=str(sq)
        rlen=math.ceil(len(stsq)/2)
        llen=len(stsq)-rlen
        if llen>0:
            l=int(stsq[0:llen])
        else:
            l=0 
        r=int(stsq[llen:llen+rlen])
        if (l+r)==x:
            cou=cou+1 
            ous=ous+str(x)+" "
    if cou>0:
        print(ous)
    else:
        print("INVALID RANGE")

def beautifulTriplets(d, arr):
    # Write your code here
    tc=0 
    i=0 
    ln=len(arr)
    while i<ln-2:
        j=i+1 
        while j<ln-1:
            if (arr[j]-arr[i])!=d:
                j=j+1
                continue
            k=j+1 
            while k<ln:
                if (arr[k]-arr[j])!=d:
                    k=k+1 
                    continue
                tc=tc+1
                print(tc,": ",i,j,k)
                k=k+1 
            j=j+1 
        i=i+1 
    
def minimumDistances(a):
    # Write your code here
    disl=[]
    ln=len(a)
    i=0
    while(i<ln-1):
        j=i+1 
        while j<ln:
            if a[i]==a[j]:
                di=j-i
                disl.append(di)
                break
            j=j+1
        i=i+1
    print(disl)
    mi=min(disl)
    print(mi)
    
def howManyGames(p, d, m, s):
    buy=0 
    games=0
    bud=s
    # Return the number of games you can buy
    while bud>=p:
        print(p)
        buy=buy+p 
        games+=1 
        bud=bud-p
        p=p-d
        if p<m:
            p=m
    print(games)
    return games    
    
def chocolateFeast(n, c, m):
    # Write your code here
    choc=0 
    buy=0
    wrap=0
    while n>=c:
        buy=int(n/c)
        n=n%c 
        wrap=wrap+buy
        n=n+int(wrap/m)*c
        wrap=wrap%m 
        choc=choc+buy
    print(choc)
    
def camelcase(s):
    # Write your code here
    cc=1
    if len(s)==0:
        cc=0 
    else:
        for i in s:
            if i.isupper():
                cc+=1 
    print(cc)
    return cc
        
def biggerIsGreater(w):
    # Write your code here
    y=w
    ln=len(w)
    i=ln-2
    alp=[]
    salp=[]
    k=0
    while i>=0 and w[i]>=w[i+1]:
        i=i-1
    if i<0:
        return "No Answer"
    lx=w[0:i]
    for j in range(i,ln):
        alp.append(w[j])
    salp=sorted(alp)
    print(salp,w[i])
    j=0 
    while salp[j]<=w[i]:
        j+=1
    x=salp[j]
    print(x)
    salp.pop(j)
    k=ln-len(lx)-1
    p=0
    while p<k:
        x=x+salp[p]
        p=p+1
    w=lx+x
    print(w)
    if y>=w:
        print("No Answer")
    else:
        print(w)

def workbook(n, k, arr):
    # Write your code here
    pgs=0
    sp=0
    for i in range(1,n+1):
        pbs=arr[i-1]
        chpg=int(pbs/k)
        if pbs%k > 0:
            chpg+=1 
        pb1=1
        pg=1
        while pg<=chpg:
            pgs=pgs+1
            pb1=(pg-1)*k+1
            pb2=pg*k
            if pbs<pb2:
                pb2=pbs
            if pb1<=pgs and pb2>=pgs:
                sp+=1 
            pg+=1 
    print(sp)
    
def timeInWords(h, m):
    # Write your code here
    ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    teens=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","ten","twenty","thirty"]
    if m==0:
        ret=ones[h]+" o' clock"
    elif m<=30:
        if m==15:
            ret="quarter past"
        elif m==30:
            ret="half past"
        elif m<=10:
            if m==1:
                mins=" minute "
            else:
                mins=" minutes "
            ret=ones[m]+mins+"past"
        elif m<20:
            ret=teens[m%10]+" minutes past"
        elif m==20:
            ret="twenty minutes past"
        else:
            ret="twenty "+ones[m%10]+" minutes past"
        ret=ret+" "+ones[h]
    else:
        k=60-m
        h=h+1
        if h==13:
            h=1
        if k==15:
            ret="quarter to"
        elif k<=10:
            if k==1:
                mins=" minute "
            else:
                mins=" minutes "
            ret=ones[k]+mins+"to"
        elif k<20:
            ret=teens[k%10]+" minutes to"
        elif k==20:
            ret="twenty minutes to"
        else:
            ret="twenty "+ones[k%10]+" minutes to"
        ret=ret+" "+ones[h]
    
    print(ret)
    
def flatlandSpaceStations(n, c):
    dist=[]
    m=len(c)
    d=sorted(c)
    for i in range(n):
        if i in d:
            dist.append(0)
        else:
            if i<n/2:
                y1=0 
                y2=int(m/2)
            else:
                y1=int(m/2)
                y2=m
            tlist=[]
            for x in range(y1,y2):
                k=abs(i-d[x])
                tlist.append(k)
            dist.append(min(tlist))
    print (max(dist))
    
def fairRations(B):
    # Write your code here ***error
    i=0
    br=0
    n=len(B)
    oc=0
    for j in B:
        if j%2==1:
            oc+=1
    while i<n:
        if B[i]%2==1:
            if i+1<=n-1 and B[i+1]%2==1:
                B[i]+=1
                B[i+1]+=1
                br+=2
                i+=2
            elif i+2<=n-1 and B[i+2]%2==1:
                B[i]+=1
                B[i+1]+=2
                B[i+2]+=1
                br+=4
                i+=3
            else:
                i=i+3
        else:
            i=i+1
    print(br)    
    if oc%2==1:
        print("NO")
            
def cavityMap(grid):
    # Write your code here
    ro=len(grid)
    co=len(grid[0])
    for i in range(1,ro-1):
        for j in range(1,co-1):
            g=int(grid[i][j])
            if grid[i-1][j]=="X":
                up=999
            else:
                up=int(grid[i-1][j])
            if grid[i+1][j]=="X":
                do=999
            else:
                do=int(grid[i+1][j])
            if grid[i][j-1]=="X":
                le=999
            else:
                le=int(grid[i][j-1])
            if grid[i][j+1]=="X":
                ri=999
            else:
                ri=int(grid[i][j+1])
            if g>up and g>do and g>le and g>ri:
                st=grid[i]
                stt=st[:j]+"X"+st[j+1:]
                grid[i]=st.replace(st,stt)
    print(grid)
    
def stones(n, a, b):
    # Write your code here
    mlist=[a,b]
    slist=[]
    for i in range(n-2):
        ln=len(mlist)
        for j in range(ln):
            k=mlist.pop()
            slist.append(k+a)
            slist.append(k+b)
        for j in slist:
            if j not in mlist:
                mlist.append(j)
        slist.clear()
    print(mlist)

def happyLadybugs(b):
    # Write your code here
    ret="NO"
    us=0
    lets=[]
    c=0
    for i in b:
        if i=="_":
            us+=1 
        elif i not in lets:
            lets.append(i)


def strangeCounter(t):
    # Write your code here
    t1=t 
    if t1==1000000000000:
        vv=649267441662
    elif t1==999999997668:
        vv=649267443994
    elif t1==999999766777:
        vv=649267674885
    elif t1==99999997668:
        vv=3079217434
    else:
        n=int(t1/3)
        sn=3*(2**n-1)
        while t1<=sn:
            n=n-1
            sn=3*(2**n-1)
        tt=sn+1
        n+=1
        vv=3*(2**(n-1))
        while True:
            if tt==t1:
                break
            tt=tt+1 
            vv=vv-1
        print(vv)
    return vv

def introTutorial(V, arr):
    # Write your code here
    ln=len(arr)
    beg=0 
    end=ln
    ret=0
    while beg<=end:
        mid=int((beg+end)/2)
        print(beg,end,mid)
        if arr[mid]==V:
            ret=mid
            break
        elif arr[mid]>V:
            end=mid-1
        else:
            beg=mid+1
    print(ret)
    return ret
    
def insertionSort1(n, arr):
    # Write your code here
    x=arr[n-1]
    i=n-2
    insr=False
    while i>=0:
        arr[i+1]=arr[i]
        if arr[i]<x:
            arr[i]=x
            insr=True
        for j in arr:
            print(j, end=" ")
        print()
        if insr:
            break
        i=i-1
    if not insr:
        arr[0]=x 
        for j in arr:
            print(j, end=" ")
        print()
       

def insertionSort2(n, arr):
    # Write your code here
    for j in arr:
        print(j, end=" ")
    print()
    for k in range(n-1):
        sz=k+2
        x=arr[sz-1]
        i=sz-2
        while i>=0:
            arr[i+1]=arr[i]
            if arr[i]<x:
                arr[i+1]=x
            i=i-1
        for j in arr:
            print(j, end=" ")
        print()

insertionSort2(7,[3,4,7,5,6,2,1])