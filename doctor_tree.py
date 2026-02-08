# doctor_tree.py

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    # Helper to find a node by name (recursive)
    def find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        
        left = self.find(node.left, name)
        if left:
            return left
        
        return self.find(node.right, name)

    # Insert a doctor under a parent on left or right
    def insert(self, parent_name, new_name, side):
        if self.root is None:
            print("Tree is empty. Set the root first.")
            return
        
        parent = self.find(self.root, parent_name)
        if not parent:
            print(f"Parent {parent_name} not found.")
            return

        new_node = DoctorNode(new_name)

        if side == "left":
            if parent.left is None:
                parent.left = new_node
            else:
                print(f"{parent_name} already has a left child.")
        elif side == "right":
            if parent.right is None:
                parent.right = new_node
            else:
                print(f"{parent_name} already has a right child.")
        else:
            print("Side must be 'left' or 'right'.")

    # Traversals
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    # Insert doctors
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Test traversals
    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

