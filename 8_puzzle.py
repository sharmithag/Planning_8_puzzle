# -*- coding: utf-8 -*-
"""
@author: SG
"""

import numpy as np
import ast 

'''
In python,list is treated as a stack. Hence, lists to store nodes and dictionary to store parent and child info for back tracking are implemented.

Initial and Goal nodes given here

'''

initial = [1,4,7,5,0,8,2,3,6]

goal= [1,4,7,2,5,8,3,6,0] 

def Input_Matrix(k):
    '''
    THe function Input_Matrix does the input list nodes to 3x3 matrix conversion 
    '''
    input_list=np.array([k]) 
    if len(input_list) ==9:
        for i in range(0,len(input_list),3):
            k.append(input_list[i]) 
            k.append(input_list[i+1])
            k.append(input_list[i+2])
            i+=1
    k=np.reshape(k,(3,3))
    return(k)

def save_as_list(m):
    '''
    The function save_as_list converts the matrix back to list
    '''
    a=[]
    for i in m[0].tolist():
            a = a +i
    return a

def ZeroLocator(current):
    '''
    The function ZeroLocator finds the zero tile in the matrix and return its position
    '''
    current=np.reshape(current,(3,3))
    for i in range(0,3):
        for j in range(0,3):
            if current[i][j]==0:
                row=i
                col=j
    return([row,col])



def ActionMoveLeft(current): 
    r=ZeroLocator(current)[0]
    c=ZeroLocator(current)[1]
    if c!=0:
        current[r][c-1],current[r][c] = current[r][c],current[r][c-1]                              #swapping elemets
        return(current,True)
    else:
        return(current,False)

def ActionMoveRight(current):
    r=ZeroLocator(current)[0]
    c=ZeroLocator(current)[1]
    if c!=2:
        current[r][c+1],current[r][c] = current[r][c],current[r][c+1]                              #swapping elemets
        return(current,True)
    else:
        return(current,False)

def ActionMoveUp(current):
    r=ZeroLocator(current)[0]
    c=ZeroLocator(current)[1]
    if r!=0:
        current[r-1][c],current[r][c] = current[r][c],current[r-1][c]                             #swapping elemets
        return(current,True)
    else:
        return(current,False)

def ActionMoveDown(current):
    r=ZeroLocator(current)[0]
    c=ZeroLocator(current)[1]
    if r!=2:
        current[r+1][c],current[r][c] = current[r][c],current[r+1][c]                            #swapping elemets
        return(current,True)
    else:
        return(current,False)
    

traversed=[]                                                                                    #traversed nodes
parent = [] 
back_track = {}                                                                                 #Backtracking as dictionary
i=0
parent.append([initial])
solved = 0

def generate_path(initial,goal): 
    '''
    The funtion generate_path is the key function that takes the initial and goal nodes as inputs and do the left, right,up, down actions to reach the goal node.

    '''
    
    traversed.append(initial)
    
    global solved                                                                              #calling the global variable solved
    
    if initial==goal:
        
        print('initial and goal nodes are same')
        
    elif initial!=goal:
        

            layer=1
            
            for c in parent: 
                
                if solved==[]:                                                              #used to break the code after goal eached
                    break
                    
                else:
                    
                    parent.append([])                                                        
                    print('In layer  : ',   layer)
                    for i in c:                                                          #for ever element, inside every list of lists in the parent node

                        l_temp=i.copy() 
                        l=ActionMoveLeft(Input_Matrix(  l_temp))                         #moving left
                        l=save_as_list(l) 

                        r_temp=i.copy() 
                        r=ActionMoveRight(Input_Matrix(  r_temp))                       #moving right
                        r=save_as_list(r)   

                        u_temp=i.copy() 
                        u=ActionMoveUp(Input_Matrix(  u_temp))                          #moving up
                        u=save_as_list(u)    
                         
                        d_temp=i.copy() 
                        d=ActionMoveDown(Input_Matrix(  d_temp))                        #moving down
                        d=save_as_list(d)  

                        back_track[str( l_temp)] = []                                   #Adding a new empty value for the Parent
                        if l not in traversed :   
                            back_track[str( l_temp)].append(l)
                        if   l_temp!=  r_temp: 
                            back_track[str( r_temp)] = []                               #Adding a new empty value for the Parent
                        if r not in traversed :   
                            back_track[str( r_temp)].append(r)     
                        if   r_temp!=  u_temp: 
                            back_track[str( u_temp)] = []                               #Adding a new empty value for the Parent
                        if u not in traversed :   
                            back_track[str( u_temp)].append(u)     
                        if   u_temp!=  d_temp: 
                            back_track[str( d_temp)] = []                               #Adding a new empty value for the Parent
                        if d not in traversed :   
                            back_track[str( d_temp)].append(d)     
                         

                        if l not in traversed :   
                            traversed.append(l)  
                            parent[ layer].append(l) 
                        if r not in traversed:   
                            traversed.append(r) 
                            parent[ layer].append(r) 
                        if u not in traversed:   
                            traversed.append(u) 
                            parent[ layer].append(u) 
                        if d not in traversed:   
                            traversed.append(d) 
                            parent[ layer].append(d)

                    for val in traversed:                                           #checking if any of the matrices in this layer is a goal
                        if val==goal: 
                            print('GOAL REACHED')
                            solved=[]                                               #reinitializing the solved to an empty list to break the loop

                layer+=1


generate_path(initial,goal) 


'''
backtracking list to save in text file
'''
val_unchanged = goal                                                        
val = goal                                                                       #goal saved to append later
start = initial                                                             
back_track_list=[]                                                          
while val!=start:
    for parent_node, child_node in back_track.items():    
        while val in child_node:
            parent_node= ast.literal_eval(parent_node)                           #for converting strings of lists, to pure lists
            val = parent_node                                               
            back_track_list.append(val)                                          #appending the values to the backtracking list
back_track_list=back_track_list[::-1]                                            #reversing the list
back_track_list.append(val_unchanged)                                            #appending the start point to show complete traversal



print('Forward from initial to goal')
print('\n')
for i in back_track_list:
    print(Input_Matrix(i))
    print('\n')

print('Backward from goal to initial')
print('\n')
back_track_list=back_track_list[::-1]
for i in back_track_list:
    print(Input_Matrix(i))
    print('\n')


'''
creating text files
'''

nodepath_list = []                                                                         
for i in back_track_list:
    m = Input_Matrix(i) 
    
    new=[]
    for i in m:
        for d in i:
            new.append(d)
    nodepath_list.append(new)

F = open('nodePath.txt', 'w')

for c in nodepath_list:
    for i in c:
        F.write(str(i)+' ')
    F.write('\n')
    
F.close() 

F = open('Nodes.txt', 'w')

for i in range(len(traversed)):
#     F.write(str(i))
    F.write('\t')
    F.write(str(traversed[i]))
    F.write('\n')
    
F.close() 

F = open('NodesInfo.txt', 'w')
'''
NodesInfo gives the layer traversed and the corresponding node detail

'''
c=0
for r in range(len(parent)):
    l = len(parent[r])
    for i in range(l):
        c=c+1
        F.write(str(r)+' \t'+str(c-1))
        F.write('\n')
F.write('\n')
    
F.close() 
