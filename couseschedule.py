from collections import deque
n=int(input("Enter the Value of n:\n"))
prerequisites=[[0,1],[3,0],[1,3],[2,1],[4,1],[4,2],[5,3],[5,4]]
print(prerequisites)
prerequisites1=[[3,0],[1,3],[2,1],[4,1],[4,2],[5,3],[5,4]]
def course_schedule(n,prerequisites):
    graph=[[]for i in range(n)]
    indegree=[0 for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]]+=1
    order=[]
    queue=deque([i for i in range(n) if indegree[i]==0])
    while queue:
        vertex=queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                queue.append(neighbor)
    return len(order)==n
result=course_schedule(n,prerequisites)
print("Output :",result)
print(prerequisites1)
result1=course_schedule(n,prerequisites1)
print("Output :",result1)
