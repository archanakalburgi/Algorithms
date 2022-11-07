def reverse_input_string(s):
    p1 = 0
    p2 = len(s)-1
    
    while p1<p2:
        first=s[p1]
        last=s[p2]
        
        s[p1]=last
        s[p2]=first
        
        p1+=1
        p2-=1
        
    return s

print(reverse_input_string(['a','r','c','h','a','n','a'])) 