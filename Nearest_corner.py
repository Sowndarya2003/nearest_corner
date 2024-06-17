#abs=it return positive value only
d=input()
s=list(input().split())
#find index of d
i1=s.index(d)
ans=999
#till i1
for i in range(0,i1):
    if s[i]=='-':
        if abs(i1-i)-1<ans:
            ans=abs(i1-i)-1
#i1 to last
for i in range(i+1,len(s)):
    if s[i]=='-':
        if abs(i-i1)-1<ans:
            ans=abs(i-i1)-1
print(ans)


        