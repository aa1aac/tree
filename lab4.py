class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)
    
    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:

                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False
    

class TwoFourNode:
    def __init__(self):
        self.order = 4
        self.numItems = 0
        self.parent = None
        self.childArray = [None] * self.order
        self.nodeValuesArray = []
    

class TwoFourTree():
    def __init__(self):
        self.root = TwoFourNode()
    
    def insert(self, dValue):
        curNode = self.root
        tempItem = dValue

        while True:
            if len(curNode.nodeValuesArray) == 3:
                if curNode.nodeValuesArray[0] < tempItem:
                    if curNode.childArray[0]:
                        curNode.childArray[0].nodeValuesArray.append(dValue)
                        curNode.childArray[0].nodeValuesArray.sort()
                    else:
                        curNode.childArray[0] = TwoFourNode()
                        curNode.childArray[0].nodeValuesArray.append(dValue)
                        curNode.childArray[0].nodeValuesArray.sort()
                    
                    break
                elif curNode.nodeValuesArray[1] < tempItem and tempItem > curNode.nodeValuesArray[0]:
                    if curNode.childArray[1]:
                        curNode.childArray[1].nodeValuesArray.append(dValue)
                        curNode.childArray[1].nodeValuesArray.sort()
                    else:
                        curNode.childArray[1] = TwoFourNode()
                        curNode.childArray[1].nodeValuesArray.append(dValue)
                        curNode.childArray[1].nodeValuesArray.sort()
                    break
                elif tempItem > curNode.nodeValuesArray[2]:
                    if curNode.childArray[3]:
                        curNode.childArray[3].nodeValuesArray.append(dValue)
                        curNode.childArray[3].nodeValuesArray.sort()
                    else:
                        curNode.childArray[3] = TwoFourNode()
                        curNode.childArray[3].nodeValuesArray.append(dValue)
                        curNode.childArray[3].nodeValuesArray.sort()
                    break
                elif tempItem < curNode.nodeValuesArray[2] and tempItem > curNode.nodeValuesArray[1]:
                    if curNode.childArray[2]:
                        curNode.childArray[2].nodeValuesArray.append(dValue)
                        curNode.childArray[2].nodeValuesArray.sort()
                    else:
                        curNode.childArray[2] = TwoFourNode()
                        curNode.childArray[2].append(dValue)
                        curNode.childArray[2].sort()
                    break

            else:
                curNode.nodeValuesArray.append(tempItem)
                curNode.nodeValuesArray.sort()
                break

        
    
    def displayLevels(self):
        h = self.height(self.root)

        for i in range(1, h):
            self.printLevel(self.root, i)
            print('')
        
    
    def printLevel(self, node, level):
        if node == None:
            return
        
        if level == 1:
            node.displayNode()
        elif level > 1:
            for i in range(len(node.getChildArray())):
                self.printLevel(node.getChild(i), self.height(node.getChild(0)))

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.getChild(0)), self.height(node.getChild(0)) )

    def getNextChild(self, theNode, theValue):
        numItems = theNode.getNumItems()
        for j in range(numItems):
            if theValue < theNode.getItem(j):
                return theNode.getChild(j)
        
        return theNode.getChild(j)
    

    def split(self, thisNode):
        parent = None
        itemC = thisNode.removeItem()
        itemB = thisNode.removeItem()
        child2 = thisNode.disconnectChild(2)
        child3 = thisNode.disconnectChild(3)

        newRight  = TwoFourNode()

        if thisNode == self.root:
            self.root = TwoFourNode()
            parent = self.root
            self.root.connectChild(0, thisNode)
        else:
            parent = thisNode.getParent()
        
        itemIndex = parent.insertItem(itemB)
        n = parent.getNumItems()

        for j in range(n - 1, -1, -1):
            temp = parent.disconnectChild(j)
            parent.connectChild(j + 1, temp)
        
        parent.connectChild(itemIndex + 1, newRight)

        newRight.insertItem(itemC)
        newRight.connectChild(0, child2)
        newRight.connectChild(1, child3)

class TwoFourTreeToRB:
    def __init__(self):
        self.newRBTree = RBTree()
    
    def converter(self, two_four_tree):
        curNode = two_four_tree.root

        self.converter_helper(curNode.nodeValuesArray)

        if curNode.childArray[0]:
            self.converter_helper(curNode.childArray[0].nodeValuesArray)
        if curNode.childArray[1]:
            self.converter_helper(curNode.childArray[1].nodeValuesArray)
        if curNode.childArray[2]:
            self.converter_helper(curNode.childArray[2].nodeValuesArray)
        if curNode.childArray[3]:
            self.converter_helper(curNode.childArray[3].nodeValuesArray)
        
        return self.newRBTree
    
    def converter_helper(self, values):
        for value in values:
            self.newRBTree.insert(value)
    


class RBTreeToTwoFour:
    def __init__(self):
        self.new_two_four_tree = TwoFourTree()

    def converter(self, red_black_tree):
        cur = red_black_tree.root
        if cur.val:
            self.new_two_four_tree.insert(cur.val)
        else:
            return self.new_two_four_tree

        self.two_four_helper(cur.left)
        self.two_four_helper(cur.right)

        return self.new_two_four_tree
    
    def two_four_helper(self, node):
        if node.val:
            self.new_two_four_tree.insert(node.val)
            self.two_four_helper(node.left)
            self.two_four_helper(node.right)
        else:
            return

        


rb_tree = RBTree()
vals = [1, 5, 7, 10, 11]
for val in vals:
    rb_tree.insert(val)

print("RB tree values")
print(rb_tree.root.val)
print(rb_tree.root.left.val)
print(rb_tree.root.right.val)
print(rb_tree.root.right.right.val)

to_two_four = RBTreeToTwoFour()
converted = to_two_four.converter(rb_tree)
print("converted to two four")
print(converted.root.nodeValuesArray[0])
print(converted.root.nodeValuesArray[1])
print(converted.root.nodeValuesArray[2])
print(converted.root.childArray[0].nodeValuesArray[0])
print(converted.root.childArray[0].nodeValuesArray[1])


two_four_tree = TwoFourTree()
vals = [1, 5, 7, 10, 11]

for val in vals:
    two_four_tree.insert(val)

print("Two Four tree ")
print(two_four_tree.root.nodeValuesArray[1])
print(two_four_tree.root.nodeValuesArray[0])
print(two_four_tree.root.nodeValuesArray[2])
print(two_four_tree.root.childArray[0].nodeValuesArray[0])
print(two_four_tree.root.childArray[0].nodeValuesArray[1])

two_four_converter = TwoFourTreeToRB()
two_four_converted = two_four_converter.converter(two_four_tree)
print('converted red black')
print(two_four_converted.root.val)
print(two_four_converted.root.left.val)
print(two_four_converted.root.right.val)
print(two_four_converted.root.right.left.val)
print(two_four_converted.root.right.right.val)

