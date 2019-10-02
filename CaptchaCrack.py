from PIL import Image,ImageDraw
from pathlib import Path
def bw(name):
    """Make captcha black-and-white"""
    im=Image.open(name).convert("RGB")
    for i in range(0,135):
        for j in range(0,50):
            q=im.getpixel((i,j))
            if q[0]==0:
                im.putpixel((i,j),(255,255,255))
            else:
                im.putpixel((i,j),(0,0,0))
    im.save(name)
    im.close()
def change():
    """Convert all to black and white"""
    c=0
    pathlist = Path("/Users/apple/Desktop/captchas1").glob("**/*.png")
    for path in pathlist:
        if c%100==0:
            print(c)
        bw(path)
        c+=1
def succ(Q,L,r):
    """A step in letter extraction"""
    n=len(Q)
    if n==0:
        Q.append(L[0])
        del(L[0])
    z=-r
    testlist=Q[z:]
    for i,j in testlist:
        if (i,j+1) in L:
            L.remove((i,j+1))
            Q.append((i,j+1))
        if (i,j-1) in L:
            L.remove((i,j-1))
            Q.append((i,j-1))
        if (i+1,j) in L:
            L.remove((i+1,j))
            Q.append((i+1,j))
        if (i-1,j) in L:
            L.remove((i-1,j))
            Q.append((i-1,j))
    m=len(Q)
    r=m-n
    return (Q,L,r)
def group(name):
    """Split image into letters"""
    im=Image.open(name).convert("RGB")
    L=[]
    for i in range(0,135):
        for j in range(0,50):
            q=im.getpixel((i,j))
            if q==(255,255,255):
                L.append((i,j))
    splitlist=[]
    while len(L)!=0:
        r=1
        Q=[]
        while r!=0:
            (Q,L,r)=succ(Q,L,r)
        Q.sort()
        splitlist.append(Q)
    count=0
    for comp in splitlist:
        comp.sort()
        x1=comp[0][0]
        x2=comp[-1][0]
        length=x2-x1+3
        pmoc=list(map(reversed,comp))
        pmoc=list(map(tuple,pmoc))
        pmoc.sort()
        y1=pmoc[0][0]
        y2=pmoc[-1][0]
        height=y2-y1+3
        number=len(comp)
        for ind in range(0,number):
            z=comp[ind]
            comp[ind]=(z[0]-x1+1,z[1]-y1+1)
        orig=name.split("/")
        orig=orig[-1]
        newname="/Users/apple/Desktop/CaptchaLetters/"+str(count)+"_"+orig
        count+=1
        new=Image.new("RGB",(length,height),(0,0,0))
        d=ImageDraw.Draw(new)
        d.point(comp)
        new.save(newname)
        new.close()
    im.close()
def splitall():
    """Split all to letters"""
    c=0
    pathlist = Path("/Users/apple/Desktop/captchas1").glob("**/*.png")
    for path in pathlist:
        if c%100==0:
            print(c)
        path=str(path)
        group(path)
        c+=1
def loops(name):
    """Number of loops in a letter"""
    im=Image.open(name).convert("RGB")
    L=[]
    lth=im.size[0]
    hth=im.size[1]
    for i in range(0,lth):
        for j in range(0,hth):
            q=im.getpixel((i,j))
            if q==(0,0,0):
                L.append((i,j))
    splitlist=[]
    while len(L)!=0:
        r=1
        Q=[]
        while r!=0:
            (Q,L,r)=succ(Q,L,r)
        Q.sort()
        splitlist.append(Q)
    return (len(splitlist)-1)
def vsucc(Q,L,r):
    """A step in bar extraction"""
    n=len(Q)
    if n==0:
        Q.append(L[0])
        del(L[0])
    z=-r
    testlist=Q[z:]
    for i,j in testlist:
        if (i,j+1) in L:
            L.remove((i,j+1))
            Q.append((i,j+1))
        if (i,j-1) in L:
            L.remove((i,j-1))
            Q.append((i,j-1))
    m=len(Q)
    r=m-n
    return (Q,L,r)
def vert(name):
    """Gets bars"""
    im=Image.open(name).convert("RGB")
    L=[]
    lth=im.size[0]
    hth=im.size[1]
    for i in range(0,lth):
        for j in range(0,hth):
            q=im.getpixel((i,j))
            if q==(255,255,255):
                L.append((i,j))
    splitlist=[]
    while len(L)!=0:
        r=1
        Q=[]
        while r!=0:
            (Q,L,r)=vsucc(Q,L,r)
        Q.sort()
        splitlist.append(Q)
    splitlist.sort(key=len)
    return len(splitlist[-1])
    
    
        
    
        
    
    
    
    
                
    
        
        
