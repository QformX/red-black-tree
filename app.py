from tree import RedBlackTree
from visualize import draw_tree
import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

empty_tree = RedBlackTree()

def insert_nodes(args):
    for item in args.split(','):
        empty_tree.insert(item)
    return draw_tree(empty_tree.root, 0, 0, 50)

def delete_nodes(args):
    for item in args.split(','):
        empty_tree.delete_node(item)
    return draw_tree(empty_tree.root, 0, 0, 50)
    
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            with gr.Column():
                args = gr.Textbox(label="Объекты заполняются через запятую")
            with gr.Row():
                with gr.Column():
                    btn1 = gr.Button("Добавить") 
                with gr.Column():
                    btn2 = gr.Button("Удалить")
        with gr.Column():
            out = gr.Plot()
    btn1.click(insert_nodes, inputs=args, outputs=out)
    btn2.click(delete_nodes, inputs=args, outputs=out)

if __name__ == "__main__":
    demo.launch()