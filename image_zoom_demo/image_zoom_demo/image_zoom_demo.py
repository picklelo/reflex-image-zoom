import reflex as rx
from reflex_image_zoom import image_zoom

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            image_zoom(
                rx.image(src="https://random.imagecdn.app/800/500", width="400px"),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)