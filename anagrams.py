
s1=input("Enter string 1\n")
s2=input("Enter string 2\n")
def anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)
result=anagrams(s1,s2)
print(" output :-",result)
