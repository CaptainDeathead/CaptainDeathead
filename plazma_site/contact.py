import reflex as rx

from plazma_site.navbar import navbar

def contact() -> rx.Component:
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Contact me!", size="9"),
            rx.text(
                "Name: Joshua Hall",
                size="5"
            ),
            rx.text(
                "Email: ", rx.link("unstableplazma@gmail.com", href="mailto:unstableplazma@gmail.com", is_external=True),
                size="5",
            ),
            rx.text(
                "GitHub: ", rx.link("https://github.com/CaptainDeathead", href="https://github.com/CaptainDeathead", is_external=True),
                size="5"
            ),
            #rx.link(
            #    rx.button("View my resume!"),
            #    href="/contact"
            #),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )