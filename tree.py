# author: Chengkun Li
# date: May, 15, 2023
# file: Make the input as inorder, postorder, or preorder from a binary tree
# input: postfix
# output: inorder/preorder/postorder format expression

from stack import Stack

class BinaryTree:
    # make the values of the tree
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # create a new branch on the left side of the tree
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # create a new branch on the right side of the tree
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # return the right child of the current root
    def getRightChild(self):
        return self.rightChild
    
    # return the left child of the current root
    def getLeftChild(self):
        return self.leftChild
    
    # assign the root of the current tree branch
    def setRootVal(self,obj):
        self.key == obj

    # return the root value of the tree
    def getRootVal(self):
        return self.key
    
    # return the string in format
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):

    # create a tree from the postfix given
    def make_tree(postfix):
        s = Stack()
        symbols = ['+','-','*','/','^']
        # loop all the all characters in postfix
        for i in postfix:
            # if i is not an symbols.
            if i not in symbols:
                # push it in to the stack as a ExpTre format
                new_tree = ExpTree(i)
                s.push(new_tree)
            # else pop two variable from the stack: x and y
            else:
                x = s.pop()
                y = s.pop()
                # make an another tree and set root to the current character
                another_tree = ExpTree(i)
                # set the leftChild to x
                another_tree.leftChild = x
                # set the rightChild to y
                another_tree.rightChild = y
                # push the another_tree to the stack
                s.push(another_tree)
        # return the last item in the stack, which is the whole tree
        return s.pop()
    
    # return an expression string in preorder when traversing/parsing the tree
    def preorder(tree):
        s = ''
        # if tree is not empty.
        if tree != None:
            # get root of the current tree
            s+= str(tree.getRootVal())
            #get all the values in RightChild as preorder
            s+= ExpTree.preorder(tree.getRightChild())
            #get all the values in LeftChild as preorder
            s+= ExpTree.preorder(tree.getLeftChild())
        # return the string
        return s
    
    # return an expression string in inorder when traversing/parsing the tree
    # flag is for not adding parentheses for whole expression
    def inorder(tree, flag = False):
        s = ''
        # if tree is not empty.
        if tree != None:
            # if leftChild and rightChild have nothing, then don't need to add parentheses.
            x = True if tree.leftChild == None and tree.rightChild == None and flag else False

            if not x: s+= '('
            #get all the values in RightChild as inorder
            s+= ExpTree.inorder(tree.getRightChild(), flag=True)
            # get root of the current tree
            s+= str(tree.getRootVal())
            #get all the values in LeftChild as inorder
            s+= ExpTree.inorder(tree.getLeftChild(), flag=True)
            if not x: s+= ')'

        # return the string
        return s
      
    # return an expression string in postorder when traversing/parsing the tree  
    def postorder(tree):
        s = ''
        # if tree is not empty.
        if tree != None:
            #get all the values in RightChild as postorder
            s+= ExpTree.postorder(tree.getRightChild())
            #get all the values in LeftChild as postorder
            s+= ExpTree.postorder(tree.getLeftChild())
            # get root of the current tree
            s+= str(tree.getRootVal())

        # return the string    
        return s
    
    # evaluate the expression string returned from inorder(tree)
    def evaluate(tree):
        return eval(ExpTree.inorder(tree))
    
    # return the string as inorder
    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
# test a BinaryTree
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0

