class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None  #parent node
        self.left = None   # left node
        self.right = None  # right node
        self.color = 1     #1=red , 0 = black