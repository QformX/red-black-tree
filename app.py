from tree import RedBlackTree
from visualize import draw_tree

if __name__ == "__main__":
    bst = RedBlackTree()
 
    bst.insert(70)
    bst.insert(60)
    bst.insert(85)
    bst.insert(80)
    bst.insert(95)
    bst.insert(65)
    
    dx = 50  # горизонтальное расстояние между узлами
    dy = 1  # вертикальное расстояние между уровнями

    draw_tree(bst.root, 0, 0, dx)
    print("\nAfter deleting an element")
    bst.delete_node(60)
    draw_tree(bst.root, 0, 0, dx)