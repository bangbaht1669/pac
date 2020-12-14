n = 3
for i in range(1,n+1,1):
    if i==1:
        print(n*"#")
    elif i== 2 and n == 3:
        print("#","#") 
    elif i>1 and i<n:
        print("#",(n-4)*" ","#")
    
    elif i==n:
        print(n*"#")
    