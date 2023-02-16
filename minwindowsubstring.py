s1=input("Enter string s1\n")
s2=input("Enter Sting s2\n")
from collections import Counter
def min_window_substring(s1,s2):
    n,m=len(s1),len(s2)
    if m>n or s2=="":
        return ""
    freqt=Counter(s2)
    start,end=0,n
    satisfied=0
    freqs=Counter()
    left=0
    for right in range(n):
        freqs[s1[right]]+=1
        if s1[right] in freqt and freqs[s1[right]]==freqt[s1[right]]:
            satisfied+=1
        if satisfied==len(freqt):
            while s1[left] not in freqt or freqs[s1[left]]>freqt[s1[left]]:
                freqs[s1[left]]-=1
                left+=1
            if right-left+1<end-start+1:
                start,end=left,right
    return s1[start:end+1] if end-start+1<=n else ""
result=min_window_substring(s1,s2)
print("output  ",result)
