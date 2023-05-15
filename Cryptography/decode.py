import math

def code(s):
    n = int(math.sqrt(len(s)))+1 if s else 0
    while len(s)!=n**2: s=s+chr(11)
    arr = [s[n*k:n*(k+1)] for k in range(n)]
    return '\n'.join(''.join(arr[j][i] for j in range(n)[::-1]) for i in range(n))
    
    

def decode(s):
    arr = [s[::-1] for s in s.split('\n')]
    return ''.join(''.join(arr[j][i] for j in range(len(arr[0]))) for i in range(len(arr))).replace(chr(11),'')




