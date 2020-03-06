
def euclidean(a,b):
    x,y=0,1
    return (((a[x]-b[x])**2)+((a[y]-b[y])**2))**0.5

with open('berlin52.txt','r') as f:
    l=f.readlines()

berlin_52=[list(map(int,i.strip().split())) for i in l]

def nearest_neighbour(coordinates):
    x,y=0,1

    visited=[False]*len(coordinates)
    i=1
    dist=0
    order=[i]
    import math
    while(sum(visited)<52):
        visited[i]=True
        dmin=math.inf
        for j in range(len(coordinates)):
            if(visited[j]==False):
                d=euclidean(coordinates[j],coordinates[i])
                if(d<dmin):
                    dmin=d
                    k=j
        i=k
        order.append(k)
        dist+=dmin
        visited[k]=True
        # print(sum(visited),end=" ")
    print(order)
    print(dist)

nearest_neighbour(berlin_52)