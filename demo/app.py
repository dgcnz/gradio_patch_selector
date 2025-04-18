import gradio as gr
from gradio_patch_selection import PatchSelector


example_annotation = {
    "image": "https://gradio-builds.s3.amazonaws.com/demo-files/base.png",
    "patchIndex": 42  # Example patch index
}

examples = [
    {
        "image": "https://raw.githubusercontent.com/gradio-app/gradio/main/guides/assets/logo.png",
        "patchIndex": 10,  # Example patch index
    },
    {
        "image": "https://gradio-builds.s3.amazonaws.com/demo-files/base.png",
        "patchIndex": 42,  # Example patch index
    },
]


def get_patch_index(annotations):
    return f"Selected Patch Index: {annotations['patchIndex']}"


with gr.Blocks() as demo:
    with gr.Tab("Patch Selector", id="tab_patch_selector"):
        gr.Markdown("# Patch Selector Demo")
        gr.Markdown("Select a patch by clicking on the grid overlaid on the image.")
        
        with gr.Row():
            with gr.Column(scale=2):
                annotator = PatchSelector(
                    example_annotation,
                    img_size=224,  # Fixed image size for ViT models
                    patch_size=16,  # Standard patch size for ViT
                    show_grid=True,
                    grid_color="rgba(200, 200, 200, 0.5)"
                )
            
            with gr.Column(scale=1):
                output = gr.Textbox(label="Selected Patch")
                gr.Markdown("### How it works")
                gr.Markdown("The image is divided into a grid of patches based on the patch size.")
                gr.Markdown("For a 224x224 image with patch size 16, there will be a 14x14 grid (196 patches).")
                gr.Markdown("Click on any patch to select it and get its index.")
        
        # Handle the patch selection event
        annotator.patch_select(lambda event: f"Patch Index: {event['patchIndex']}", annotator, output)
        
        gr.Examples(examples, annotator)

if __name__ == "__main__":
    demo.launch()
