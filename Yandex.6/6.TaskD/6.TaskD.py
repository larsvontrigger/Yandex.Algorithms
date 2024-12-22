n,a,b,w,h = map(int,input().split())

def modules(d,a,b,w,h,n):
    i1 = w // (b + 2 * d)
    j1 = h // (a + 2 * d)
    
    i2 = w // (a + 2 * d)
    j2 = h // (b + 2 * d)

    return (n <= i1 * j1 or n <= i2 * j2)
        
def base(n,a,b,w,h):
    modulesize = 0
    l = 0
    r = min(w,h)
    
    while l <= r:
        d = (l + r)//2

        if modules(d,a,b,w,h,n):
            modulesize = d
            l = d + 1
        else:
            r = d - 1
    
    return modulesize

print(base(n,b,a,w,h))