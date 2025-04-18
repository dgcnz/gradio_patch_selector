
# `gradio_patch_selection`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.2.5%20-%20orange">  

A Gradio component that allows users to select patches from images by overlaying a customizable grid.

This component is based on [gradio_image_annotator](https://github.com/edgarGracia/gradio_image_annotator) by Edgar Gracia.

## Installation

```bash
pip install gradio_patch_selection
```

## Usage

```python
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

```

## `PatchSelector`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
dict | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">A dict or None. The dictionary must contain a key 'image' with either an URL to an image, a numpy image or a PIL image. It may also contain a key 'patchIndex' with the index of the selected patch.</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The height of the displayed image, specified in pixels if a number is passed, or in CSS units if a string is passed.</td>
</tr>

<tr>
<td align="left"><code>width</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The width of the displayed image, specified in pixels if a number is passed, or in CSS units if a string is passed.</td>
</tr>

<tr>
<td align="left"><code>img_size</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If provided, will resize the displayed image to this fixed dimension (img_size × img_size). This takes precedence over height and width parameters. Recommended for ViT models, which typically use square images of fixed dimensions (e.g., 224x224).</td>
</tr>

<tr>
<td align="left"><code>patch_size</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>16</code></td>
<td align="left">The size of each patch in pixels. For a 224x224 image with patch_size=16, there will be a 14x14 grid (196 patches).</td>
</tr>

<tr>
<td align="left"><code>show_grid</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will display the grid overlay on the image.</td>
</tr>

<tr>
<td align="left"><code>grid_color</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"rgba(200, 200, 200, 0.5)"</code></td>
<td align="left">The color of the grid overlay lines, specified as a CSS color string.</td>
</tr>

<tr>
<td align="left"><code>image_mode</code></td>
<td align="left" style="width: 25%;">

```python
"1"
    | "L"
    | "P"
    | "RGB"
    | "RGBA"
    | "CMYK"
    | "YCbCr"
    | "LAB"
    | "HSV"
    | "I"
    | "F"
```

</td>
<td align="left"><code>"RGB"</code></td>
<td align="left">"RGB" if color, or "L" if black and white. See https://pillow.readthedocs.io/en/stable/handbook/concepts.html for other supported image modes and their meaning.</td>
</tr>

<tr>
<td align="left"><code>sources</code></td>
<td align="left" style="width: 25%;">

```python
list["upload" | "webcam" | "clipboard"] | None
```

</td>
<td align="left"><code>["upload", "webcam", "clipboard"]</code></td>
<td align="left">List of sources for the image. "upload" creates a box where user can drop an image file, "webcam" allows user to take snapshot from their webcam, "clipboard" allows users to paste an image from the clipboard. If None, defaults to ["upload", "webcam", "clipboard"].</td>
</tr>

<tr>
<td align="left"><code>image_type</code></td>
<td align="left" style="width: 25%;">

```python
"numpy" | "pil" | "filepath"
```

</td>
<td align="left"><code>"numpy"</code></td>
<td align="left">The format the image is converted before being passed into the prediction function. "numpy" converts the image to a numpy array with shape (height, width, 3) and values from 0 to 255, "pil" converts the image to a PIL image object, "filepath" passes a str path to a temporary file containing the image. If the image is SVG, the `type` is ignored and the filepath of the SVG is returned.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>True</code></td>
<td align="left">if True, will allow users to upload and annotate an image; if False, can only be used to display annotated images.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>show_download_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will show a button to download the image.</td>
</tr>

<tr>
<td align="left"><code>show_share_button</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.</td>
</tr>

<tr>
<td align="left"><code>show_clear_button</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will show a button to clear the current image.</td>
</tr>

<tr>
<td align="left"><code>show_remove_button</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, will show a button to remove the selected bounding box.</td>
</tr>

<tr>
<td align="left"><code>handles_cursor</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, the cursor will change when hovering over box handles in drag mode. Can be CPU-intensive.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `clear` | This listener is triggered when the user clears the PatchSelector using the clear button for the component. |
| `change` | Triggered when the value of the PatchSelector changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `upload` | This listener is triggered when the user uploads a file into the PatchSelector. |
| `patch_select` | Triggered when a patch is selected by the user. Returns the patch index. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, a dict with the image and patchIndex or None.
- **As input:** Should return, a dict with an image and an optional patchIndex or None.

 ```python
 def predict(
     value: dict | None
 ) -> dict | None:
     return value
 ```
 
