class Node():
    def __init__(self,left,right,data) -> None:
        self.left = left
        self.right = right
        self.data = data 


class BST():
    def __init__(self) -> None:
        self.root = None
    
    
    def add_node(self,root,data) -> Node:
        # first element
        if root is None:
            root=Node(None, None,data)
        else:
            if root.data >= data:
                root.left  = self.add_node(root.left,data)
            else:
                root.right  = self.add_node(root.right,data)
        return root 
    
    def in_order(self,root) -> None:
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def print_leaf(self,root) -> None:
        if root:
            self.print_leaf(root.left)
            if root.left == None and root.right == None:
                print(root.data)
            self.print_leaf(root.right)
    
    def print_left(self,root) -> None:
        if root:
            if root.left:
                print(root.data)
                self.print_left(root.left)
            elif root.right:
                print(root.data)
                self.print_left(root.left)

    def print_right(self,root) -> None:
        if root:
            if root.right:
                print(root.data)
                self.print_right(root.right)
            elif root.left:
                print(root.data)
                self.print_right(root.right)
                                 
if __name__ == '__main__':
    b = BST()
    b.root = b.add_node(None,20)
    b.add_node(b.root,8)
    b.add_node(b.root,4)
    b.add_node(b.root,12)
    b.add_node(b.root,10)
    b.add_node(b.root,14)
    b.add_node(b.root,22)
    b.add_node(b.root,25)
    b.in_order(b.root)
    print("------------ Leafs------------")
    b.print_leaf(b.root)
    print("-----------Left----------")
    b.print_left(b.root)
    print("-----------Right----------")
    b.print_right(b.root)
    print("Boundary")
    b.print_left(b.root)
    b.print_leaf(b.root)
    b.print_right(b.root.right)
    
    