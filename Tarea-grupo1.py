# Python program to demonstrate searching operation
# in binary search tree without recursion
class newNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to check the given
# key exist or not
def iterativeSearch(root, key):
    path = []
    while root != None:
        if key > root.data:
            root = root.right
            path.append('right')
        elif key < root.data:
            root = root.left
            path.append('left')
        else:
            return True, path
    return False, None

# A utility function to insert a
# new Node with given key in BST
def insert(Node, data):
	
	# If the tree is empty, return
	# a new Node
	if Node == None:
		return newNode(data)

	# Otherwise, recur down the tree
	if data < Node.data:
		Node.left = insert(Node.left, data)
	elif data > Node.data:
		Node.right = insert(Node.right, data)

	# return the (unchanged) Node pointer
	return Node

class tree:
    def __init__(self):
        self.root = None

    def set_root (self, data):
        self.root = insert(self.root, data)

    def insert (self, data):
        if(self.root == None):
            print('set root before')
        else:
            insert(self.root, data)

    def search(self, key):
        return iterativeSearch(self.root, key)

# Driver Code
if __name__ == '__main__':
	
	# Let us create following BST
	# 50
	# 30  70
	# / \ / \
	# 20 40 60 80
    arbol = tree()
    n = int(input('Cantidad de nodos para la generación del arbol binario: '))

    root = int(input('Ingrese el valor raiz para la generación del arbol binario: '))
    arbol.set_root(root)

    for i in range(n-1):
        data = int(input('Ingrese el valor ({}): '.format(i+1)))    
        arbol.insert(data)

    key = int(input('Digite cual valor desea buscar en el arbol: '))
    busqueda = arbol.search(key)
    if busqueda[0]:
        print('La ruta del valor buscado es:')
        print(' '.join(i for i in busqueda[1]))
    else:
        print('El valor buscado no se encuentra en el arbol')

# This code is contributed by PranchalK
