"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_image_zoom import image_zoom

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Test your custom component by editing ", rx.code(filename)),
            image_zoom(
                rx.image(src="https://picsum.photos/800/500", width="400px"),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
