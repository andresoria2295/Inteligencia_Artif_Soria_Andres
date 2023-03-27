import numpy as np
import copy

#Take input node from user
def take_input():
  print("Enter a start node row wise (e.g 1 2 3 0 4 5 8 6 7)")
  A= [int(i) for i in input().split()]
  return A

# Find Blank tile in the node
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i   # Return Blank Tile Location

# Move up tile
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  if b>2:
    U[b]=U[b-3]  # Swap Tiles
    U[b-3]=0
  return U       # Return New Node

# Move down tile
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  if b<6:
    D[b]=D[b+3]  # Swap Tiles
    D[b+3]=0
  return D       # Return New Node
   
# Move left tile
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]  # Swap Tiles
    L[b-1]=0
  return L       # Return New Node

# Move right tile
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]  # Swap Tiles
    R[b+1]=0
  return R       # Return New Node

# Generate path from action set generated by BFS
def generate_path(path,N):
  file = open("nodePath.txt", "w")      # open text file
  file.writelines(column(N)+ '\n')      # write path
  print(column(N))
  for p in range(len(path)):            # Check the action sets
    if path[p]=="U":                   
      b=BlankTileLocation(N)
      N=ActionMoveUp(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
    elif path[p]=="D":
      b=BlankTileLocation(N)
      N=ActionMoveDown(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
    elif path[p]=="L":
      b=BlankTileLocation(N)
      N=ActionMoveLeft(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
    elif path[p]=="R":
      b=BlankTileLocation(N)
      N=ActionMoveRight(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
  file.close()                           # Close File

# Add Node to Child list and find no of childs per parent
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)             
  if P!=A:                             # Check if node is new or same
    child=child+A+Pdir                 # Append new node and its action set
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c                 #Return total child nodes, nodes, nodes per parent

# convert node to column wise
def column(N):
  F=copy.deepcopy(N)
  F=str(N[0])+" "+str(N[3])+" "+str(N[6])+" "+str(N[1])+" "+str(N[4])+" "+str(N[7])+" "+str(N[2])+" "+str(N[5])+" "+str(N[8])
  return F                           # Return node column wise

# BFS algorithm to reach goal node
def run(N):
  inv=0
  for i in range(8):               # Check Solvability
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  if inv%2!=0:                     # Exit if not solvable
    print("No solution exists for this initial state")
    return [0],[0],0,0
  else:
    print(" solution exists for this initial state",'\n',"Maximum time required to solve can be 1hr 30mins",'\n',"Solving...")
  file2 = open("Nodes.txt", "w")
  explored=[]                      # Intialize variables
  Parent= N
  child=[]
  cn=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  while f==0:                      # Access different tree levels
    child.clear()
    for c in range(no_of_parents): # Access different node in a particular level
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        file2.writelines(column(P)+ '\n')
        break
      if not P in explored:        # Check for child node if parent not in explored
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)
        file2.writelines(column(P)+ '\n')    # Write to explored nodes list txt
      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  file2.close()
  print(cn)
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored),1   # Return final actionset, no of nodes per parent, total no of explored nodes and 1
 
# Generate NodeInfo.txt file from no of childs per parents data
def generate_nodeinfo(o,f):
  file1 = open("NodesInfo.txt", "w")   # Open File
  u=0
  j=0
  temp=1
  file1.writelines(str(1)+" "+str(0)+" "+str(0)+'\n')
  for i in range(1,f):
    if o[j]==0:
      temp=temp+1
      j=j+1
    file1.writelines(str(i+1)+" "+str(temp)+" "+str(0)+'\n')   # write child node, Parent Node and cost
    if o[j]!=0:
      u=u+1
      if o[j]-u==0 and o[j]!=0:
        j=j+1
        temp=temp+1
        u=0
  file1.close()                        # Close File

# Call Functions
A=take_input()   # Taking input from user
NP,o,x,f=run(A)  # Run the BFS Algorithm
if f==1:
  generate_nodeinfo(o,x) # Generate NodeInfo.txt
  generate_path(NP,A)    # Generate nodePath.txt

