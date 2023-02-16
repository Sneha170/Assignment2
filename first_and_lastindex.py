def first_last_index(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            start=i
            while i+1<len(arr) and arr[i+1]==k:
                i=i+1
            return [start,i]
    return [-1,-1] 

m=int(input("Enter number of array elements :\n"))
arr=[]
for i in range(m):
    l=int(input())
    arr.append(l)
print(arr)
k=int(input("Target value:\n"))
j=first_last_index(arr,k)
print("output : ",j)
