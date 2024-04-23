import matplotlib.pyplot as plt

# Функция для рисования красно-чёрного дерева
def render_red_black_tree(node, x, y, dx):
    dy = 1
    if node is not None:
        # Рисуем левое поддерево
        render_red_black_tree(node.left, x - dx, y - dy, dx/2)
        
        # Рисуем узел
        color = "black" if node.color == 0 else "red"
        plt.text(x, y, str(node.item), color=color, fontweight='bold', ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.2'))
        
        # Рисуем связи с левым и правым дочерними узлами
        if node.left is not None:
            plt.plot([x, x-dx], [y+dy/30, y-dy], color=color)
        if node.right is not None:
            plt.plot([x, x+dx], [y+dy/30, y-dy], color=color)
        
        # Рисуем правое поддерево
        render_red_black_tree(node.right, x + dx, y - dy, dx/2)


def draw_tree(node, x, y, dx, pic_name):
    plt.figure(figsize=(10, 10))
    plt.axis('off')
    render_red_black_tree(node, x, y, dx)
    plt.savefig(pic_name)
    plt.show()

