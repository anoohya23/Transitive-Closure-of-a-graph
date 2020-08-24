"""
Transitive Closure of the graph
1.	Enter the total Nodes
2.	Enter N1 N2  (N1 space N2 )
3.	Once done with adding edges just press ENTER to exit the loop.
4.	The adjacency matrix and transitive closure of graph is printed.

"""
matrix = []

nodes=int(input("Number of nodes:"))

for i in range(nodes):
    matrix.append([0]*nodes)

rowCol_names=[]
#edges=int(input("Number of Edges:"))

rowCol_input=[]
inp = input("N1 N2 ")
while(inp!=''):
    rowCol_input=[]
    
    for j in inp.split():
        rowCol_input.append(j)

    if(rowCol_input[0] not in rowCol_names):
        rowCol_names.append(rowCol_input[0])

    if(rowCol_input[1] not in rowCol_names):
        rowCol_names.append(rowCol_input[1])

    matrix[rowCol_names.index(rowCol_input[0])][rowCol_names.index(rowCol_input[1])] = 1
    
    inp = input("N1 N2 ")
#print(matrix,rowCol_names)
print("The adjacency matrix")
for i in range(nodes): 
    for j in range(nodes): 
        print(matrix[i][j], end = " ") 
    print()
t = [ [0 for i in range(nodes)]] * nodes


t=matrix
            
    
for k in range(nodes): 
    for i in range(nodes):
        for j in range(nodes):
            t[i][j]=t[i][j] or (t[i][k] and t[k][j])

print("The Transitive Closure of graph is")
for i in range(nodes): 
    for j in range(nodes): 
        print(t[i][j], end = " ") 
    print()            
    
