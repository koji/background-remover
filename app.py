from rembg import remove
import gradio as gr

def remove_bg(input_image):
    output = remove(input_image)
    return output

demo = gr.Interface(
    remove_bg,
    gr.Image(type="pil"),
    "image",
)

if __name__ == "__main__":
    demo.launch()
