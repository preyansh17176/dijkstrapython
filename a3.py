### PREYANSH RASTOGI
### 2017176


### IP HOMEWORK 3



### MODULES IMPORTED
from sys import maxsize as maxi




### FUNCTION TO INPUT GLOBAL LISTS
def lists_input(n=5,connections=[],weights=[]):
    T=''
    for i in range (n):
        x =[]
        z =[]
        T = int(input())
        for j in range(T):
            y =str(input())
            y =y.split(' ')
            x.append(int(y[0])) 
            z.append(int(y[1])) 
        weights.append(z)
        connections.append(x)


        
### FUNCTION TO SOLVE DIJKSTRA'S SINGLE SOURCE SHORTEST PATH PROBLEM
def dijkstra(a,graph):
    ## SPLITTING THE GRAPH BACK INTO CONNECTIONS,WEIGHTS
    connections=graph[0]
    weights=graph[1]
    ## LIST OF UNVISITED VERTICES
    Q=[]
    ## LIST CONTAINING DIJKSTRA DISTANCE 
    dist =[]
    
    ## FOR LOOP TO INITIALISE ((Q WITH ALL THE VERTICES)) AND ((DIST WITH INFINITY))
    for i in range(len(connections)):
        dist.append(maxi)
        Q.append(i)

    dist[a] = 0

    while len(Q) > 0:

        ## LIST CONTAINING DISTANCES FROM SOURCE OF VERICES PRESENT IN Q
        dist_copy =[]
        for i in Q:
            dist_copy.append(dist[i])

        ## FINDING THE VERTEX NUMBER AT MINIMUM DISTANCE   
        for i in Q:
            if min(dist_copy)== dist[i]:
                u = i
                break 
    
        Q.remove(u)

        ## GETTING THE DISTANCES OF THAT VERTEX'S NEIGHBOURS
        i=0
        for v in connections[u]:
            temp = dist[u] + weights[u][i]
            dist[v] = min(dist[v],temp)
            ## INCREMENTING IT  TO ACCESS THE NEXT INDEX OF WEIGHT
            i+=1

    ## RETURNING THE DIJKSTRA DISTANCE
    return dist



### FUNCTION TO SOLVE BREADTH FIRST SEARCH PROBLEM
def breadthfirstsearch(a,graph):
    
    ## SPLITTING THE GRAPH BACK INTO CONNECTIONS,WEIGHTS
    connections=graph[0]
    weights=graph[1]

    ## LIST OF UNVISITED VERTCES 
    Q=[]
    ## LIST CONTAINING DIJKSTRA DISTANCE
    dist=[]
    dist=dijkstra(a,graph)
    dist_bfs=[]

    ## INITIALISING Q WITH VERTICES WITHOUT INFINITE DISTANCES
    for i in range(len(dist)):
        dist_bfs.append(maxi)
        if dist[i]!= maxi:
            Q.append(i)

    ## LIST TO TAKE THE BFS PATH
    bfs=[]
    
    ## LIST TO TAKE ALL THE LAYERS, WITH EACH LAYER IN EACH INDEX
    layers=[]
    layers.append([a])
    
    ## WILL BE USED TO ACCESS THE FIRST LAYER
    i=0
    
    dist_bfs[a]=0
    
    ## CREATING A COPY OF Q, WILL BE USED IN FINDING THE  DIST_BFS
    Q_copy=list(Q)
    
    ## THIS LOOP WILL CREATE A LIST OF LAYERS
    ## THIS LOOP WILL ITERATE TILL Q IS EMPTY
    while len(Q) > 0:
        x= []
        ## INITIALLY THE LOOP WILL ITERATE FOR 0'TH LAYER
        ## IN SECOND ITERATION OF WHILE, IT WILL ITERATE ON 1ST LAYER
        ## THIS INCREMENT IS MADE THROUGH THE (( i+=1 )) GIVEN AFTER WHILE LOOP
        for j in layers[i]:
            
            ## VISITED VERTICE WILL NOT VIEWED AGAIN
            if j in Q:
                ## VIEWING IT NOW, SO REMOVING IT FROM Q
                Q.remove(j)
                ## CHECKING OUT THE NEIGHBOURS OF j AND IF IT NOT IN ANY OF THE LAYERS 
                for v in connections[j]:
                    if v in Q : #### NOT REQUIRED -- WILL ALWAYS IN Q 
                        if v in x :
                            pass
                        else:
                            k =False
                            for i in range(len(layers)):
                                
                                if v in layers[i]:
                                    k = True
                            if not k:
                                ## ADDING VERTICES IN iTH LAYER 
                                x.append(v)
        ## ADDING THE NEXT LAYER
        layers.append(x)
        ## INCREMENTING i TO ACCESS THE NEXT LAYER
        i+=1
    i=0
    j=0
    Q_copy.remove(a)
    for i in range(len(layers)):
        for j in layers[i]:
            z=0
            for k in connections[j]:
                if k in Q_copy:
                    Q_copy.remove(k)
                    temp=dist_bfs[j]+weights[j][z]
                    dist_bfs[k]=temp
                z+=1
                
    for i in range(len(layers)):
        for j in layers[i]:
            bfs.append(j)
            
    ### return bfs
    return dist_bfs
    

### FUNCTION TO CHANGE THE WEIGHTS TO 1 
def change_weights(graph):
    connections=graph[0]
    weights=graph[1]
    for i in range(len(connections)):
        for j in range(len(connections[i])):
            weights[i][j]=1

    graph=[connections,weights]
    


### APPLICATION SCRIPT
if __name__ == '__main__':
    
    connections =[]
    weights = []
    ### n  is  No. in list connections
    n = int(input())
    lists_input(n,connections,weights)
    graph=[connections,weights]
    ### a is the source vertice
    a  =  int(input())
    dist = dijkstra(a,graph)
    ### a is the layer 0 vertice
    b  =  int(input())
    dist_bfs = breadthfirstsearch(b,graph)
    print (dist)
    print (dist_bfs)

    
    change_weights(graph)
    dist = dijkstra(a,graph)
    dist_bfs = breadthfirstsearch(b,graph)
    print (dist)
    print (dist_bfs)
  

