import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Plazma", font_weight="bold", font_size="lg"),
            rx.spacer(),
            rx.link("Home", href="/"),
            rx.link("Projects", href='/projects'),
            rx.link("About", href="/about"),
            rx.link("Contact", href="/contact"),
            spacing="4"
        ),
        position="sticky",  # or use "fixed"
        top="0",
        width="100%",
        padding="1em",
        bg=rx.color_mode_cond(light="lightgrey", dark="rgb(30, 30, 30)"),
        box_shadow="md",
        z_index="1000",
        border="1px solid",
        border_color="grey"
    )