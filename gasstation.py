m=int(input("Enter number of gas elements\n"))
gas=[]
print("Enter gas elements")
for i in range(m):
    l=int(input())
    gas.append(l)
print(gas)
n=int(input("Enter number of cost elements\n"))
cost=[]
print("Enter cost elements")
for i in range(n):
    k=int(input())
    cost.append(k)
print(cost)
def gas_station(gas,cost):
    remaining=0
    prev_remaining=0
    candidate=0
    for i in range(len(gas)):
        remaining+=gas[i]-cost[i]
        if remaining<0:
            candidate=i+1
            prev_remaining+=remaining
            remaining=0
    if candidate==len(gas) or remaining+prev_remaining<0:
        return -1
    else:
        return candidate
    
result=gas_station(gas,cost)
print("result is ",result)
