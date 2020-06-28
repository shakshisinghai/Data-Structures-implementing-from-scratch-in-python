class Node:
	def __init__(self):
		self.left=None
		self.right=None
		self.value=None

class BinaryTree:
  def __init__(self, l):
    self.__head=Node()
    self.__createBT(l)
  
  @property 
  def head(self):
    return self.__head

  @property 
  def height(self):
    """
    height: Returns the height of Binary tree
    """
    return BinaryTree.__findheight(self.head)
  
  @height.setter
  def height(self, height):
     raise Exception("Can't set Height")
    
  def insertelement(self,element):
    """
    insertelement
    Input:
      Element to be inserted in the Binary tree
    """
    flag=0
    root=self.head
    newNode=Node()
    newNode.value= element
    if self.head.value==None:
      self.__head=newNode
      root=self.head
    else:
      while flag==0:
        while element<root.value:
          if root.left==None:
            root.left=newNode
            flag=1
            break
          root=root.left
        while element>root.value:
          if root.right==None:
            root.right=newNode
            flag=1
            break
          root=root.right

  def __createBT(self, l):
    for element in l:
      self.insertelement(element)
  
  @staticmethod
  def __findheight(root):
    if root==None:
      return 0
    else :
      return max(BinaryTree.__findheight(root.left),BinaryTree.__findheight(root.right))+1
    
  
    

  @staticmethod
  def __preOrder(root):
    if root==None:
      return []
    else:
      return [root.value] + BinaryTree.__preOrder(root.left)+ BinaryTree.__preOrder(root.right)  
  
  @staticmethod 
  def __inOrder(root):
    if root==None:
      return []
    else:
      return  BinaryTree.__inOrder(root.left)+ [root.value] + BinaryTree.__inOrder(root.right)
   
  @staticmethod
  def __postOrder( root):
    if root==None:
      return []
    else:
      return  BinaryTree.__postOrder(root.left)+ BinaryTree.__postOrder(root.right)+ [root.value] 
   
  
  
  
  
  def traverse(self,order):
    """
    traverse
    Input:
      Order: Order in which you want to traverse the binary tree."PRE","POST", "IN" order can be given as input.
    Output:
      Returns a list according to the input order 
    """
    l1=[]
    if (order)=="PRE":
      l1=BinaryTree.__preOrder(self.head)
    if (order)=="IN":
      l1=BinaryTree.__inOrder(self.head)
    if (order)=="POST":
      l1=BinaryTree.__postOrder(self.head)
    return l1
  
  @staticmethod
  def __find(root, element):
    prevroot=None
    while root!=None and element!=root.value:
      while root!=None and element<root.value:
        prevroot=root
        root=root.left
      while root!=None and element>root.value:
        prevroot=root
        root=root.right
    return root, prevroot
  
  
  def findelemet (self,element):
    """
    findelement
    Input: 
      the element you want to find in the tree
    Output:
      returns the pointer of that element
    """
    elementroot, prevroot=BinaryTree.__find(self.head, element)
    return elementroot
  
  def delete(self,element):
    """
    delete
    Input:
      element you want to delete
    """
    current, prevroot=BinaryTree.__find(self.head,element)
    if current.left== None and current.right==None:
      if prevroot.value> element :
        prevroot.left=None 
      else:
        prevroot.right=None
    elif current.left!= None and current.right==None :
      if prevroot.value> element :
        prevroot.left=current.left 
      else:
        prevroot.right=current.left 
    elif current.left== None and current.right!=None:
      if prevroot.value> element :
        prevroot.left=current.right 
      else:
        prevroot.right=current.right 
    else:
      lastnode=current
      while lastnode.left!=None:
        prevlast=lastnode
        lastnode=lastnode.left
      if prevroot==None:
        current.value=lastnode.value
      elif prevroot!=None: 
        if prevroot.value> element :
          prevroot.left.value=lastnode.value 
        else:
          prevroot.right.value=lastnode.value 
      if lastnode.right==None:
          prevlast.left=None
      else :
        prevlast.left=lastnode.right
        
        
  def isBalanced(self, root=-1, isBal=True):
    """
    isBalanced
    Output:
      returns True if binary tree is balanced else returns false
    """
    if root==-1:
      root=self.head
    if root==None:
      return True
    if abs(BinaryTree.__findheight(root.left)-BinaryTree.__findheight(root.right))<=1 and isBal!=False:
      isBal=self.isBalanced(root.left, isBal)
      isBal=self.isBalanced(root.right, isBal)
    else :
      return False
    return isBal
        
  def balance(self):
    """
    balance: balances the binary tree
    """
    self.__balance(self.head, None, None)
    
  
  def __balance(self,root, parentroot,childside):
    if root==None:
      return
    self.__balance(root.left, root, "left")
    self.__balance(root.right, root, "right")
    if (BinaryTree.__findheight(root.left)-BinaryTree.__findheight(root.right)) >1:
      temp=root.left.right
      root.left.right=root
      root=root.left
      root.right.left=temp
    elif (BinaryTree.__findheight(root.right)-BinaryTree.__findheight(root.left))>1:
      temp=root.right.left
      root.right.left=root
      root=root.right
      root.left.right=temp
    if childside =="left":
      parentroot.left=root
    elif childside =="right":
      parentroot.right=root
    if parentroot==None:
      self.__head=root
   
  def BFS(self, root=-1):
    """
    BFS: Breadth First Search. Traverse the tree in BFS manner. 
    """
    l1,l2=[], []
    if self.head!=None and root==-1:
      root=self.head
      l1.append(root)
    while l1!=[]:
      if l1[0].left!=None:
        l1.append(l1[0].left)
      if l1[0].right!=None:
        l1.append(l1[0].right) 
      l2.append(l1[0])
      l1.pop(0)
    for i in l2:
      print(i.value)
      
  def DFS(self, root=-1):
    """
    DFS: Depth First Search. Traverse the tree in DFS manner.
    """
    l1=[]
    if self.head!=None and root==-1:
      root=self.head
      l1.append(root)
    while l1!=[]:
      a=l1.pop(-1)
      if a.right!=None:
        l1.append(a.right) 
      if a.left!=None:
        l1.append(a.left)
      
   
   

  
l=[10,2,1,0]
l1=[]
a=BinaryTree(l)
#a.insertelement(6)
print(a.isBalanced())

l1=a.traverse("PRE")
print("PRE",l1)
l1=a.traverse("IN")
print("IN",l1)
a.traverse("POST")
print("POST",l1)
a.balance()
l1=a.traverse("PRE")
print("PRE",l1)
    