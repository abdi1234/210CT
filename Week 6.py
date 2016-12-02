#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
  

def in_order(tree):

    stack = []
    finished = False


    while (finished == False):  

        if tree != None:        #If tree isnt empty
            stack.append(tree)  #add the node to the stack

            tree = tree.left    #move to the tree to the left side

        else:

            if (len(stack) > 0):#if the length of the stack is more than 0
                tree = stack.pop()#moves the most recent value from stack to tree
                print(tree.value)
                tree = tree.right#moves to the right value
            else:
                finished = True
 
if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,11)
  tree_insert(t,6)
  tree_insert(t,2)
  tree_insert(t,5)
  tree_insert(t,8)
  tree_insert(t,1)
  in_order(t)
