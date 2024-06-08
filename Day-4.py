#Tree layout
#post-left,right,root
#inorder-left,root,right
#pre-root,left,right
##Breadth First search code

# def bfs(start,graph):
#     visited=[start]
#     q=[start]
#     while len(q) != 0:
#         ele=q.pop(0)
#         for i in graph[ele]:
#             if i not in visited:
#                 q.append(i)
#                 visited.append(i)
#     return visited      
# graph={"A":["B","C"],
#        "B":["A","C","D"],
#        "C":["A","B","E"],
#        "D":["B","E"],
#        "E":["D","C"]}
# res=bfs("E",graph)
# print(res)
'''

##Dfs
def DFS(start,graph,visited = None):
    if visited ==None:
       visited=[]
    visited.append(start)
    for ne in graph[start]:
        if ne not in visited:
            DFS(ne,graph,visited)
    return visited
graph={
"A":["B","C"],
"B":["A","C","D"],
"C":["A","B","E"],
"D":["B","E"],
"E":["C","D"],
}
res=DFS("E",graph)
print(res)

##

"""
zone C: abc  kld    start:[abc,efg]
zone B: cde  ijk    dest:[kld,ijk]
zone A: efg  ghi    op:[c,ab]

"""

def railways(start,dest):
    if start=="abc" or dest=="kld":
        print("A")
    elif start=="abc" or dest=="ijk":
        print("AB")
    elif start=="abc" or dest=="efg":
        print("ABC")
    elif start=="cde" or dest=="kld":
        print("BC")
    elif start=="cde" or dest=="ijk":
        print("B")
    elif start=="cde" or dest=="ghi":
        print("BA")
    elif start=="efg" or dest=="ghi":
        print("C")
    elif start=="efg" or dest=="kld":
        print("AC")
    elif start=="efg" or dest=="ijk":
        print("AB")
start=input("Start:")
dest=input("Destination:")
railways(start,dest)                                
    
'''
"""
zone C: abc  kld    start:[abc,efg]
zone B: cde  ijk    dest:[kld,ijk]
zone A: efg  ghi    op:[c,ab]

"""

def train(zone,start,destination):
    if zone=="A":
        if start=="efg" or (destination== "ijk " and destination=="cde") :
            print("AB")                                                           
        elif start=="efg" or (destination=="abc" and destination=="kld"):
            print("ABC")
        else:
            print("A")
    if zone=="B":
        if start=="cde" or (destination== "ghi" and destination=="efg") :
            print("AB")
        elif start=="cde" or (destination=="abc" and destination=="kld"):
            print("BC")
        else:
            print("B")    
    if zone=="C":
        if start=="abc" or (destination== "ijk " and destination=="cde") :
            print("AB")
        elif start=="abc" or (destination=="efg" and destination=="ghi"):
            print("ABC")
        else:
            print("C")    
zone=input("enter zone:")
start=input("enter start:")
destination=input("enter destination:")     
train(zone,start,destination)   
