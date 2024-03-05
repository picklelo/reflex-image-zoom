# Image Zoom Component

A Reflex custom component image-zoom - based on [react-medium-image-zoom](https://www.npmjs.com/package/react-medium-image-zoom).

Check out the [live demo](https://image-zoom.reflex.run).

## Installation

```bash
pip install reflex-image-zoom
```

## Usage

![image-zoom](image-zoom.gif)

I've currently wrapped no props, simply pass the image as a child of the component.

```python
import reflex as rx
from reflex_image_zoom import image_zoom

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            image_zoom(
                rx.image(src="https://picsum.photos/800/500", width="400px"),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
```