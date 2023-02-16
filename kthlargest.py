def kth_largest_element(arr,k):
    n=len(arr)
    arr.sort()
    return arr[n-k]


m=int(input("Enter number of array elements:\n"))
arr=[]
print("Enter array Elements")
for i in range(m):
    l=int(input())
    arr.append(l)
print(arr)
k=int(input("Target value\n"))
j=kth_largest_element(arr,k)
print("output : ",j)


