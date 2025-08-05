import reflex as rx

from plazma_site.navbar import navbar

def about() -> rx.Component:
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("About me!", size="9"),
            rx.text(
                "My name is Joshua Hall and I am 16 years old. I live in Western Australia. I am currently attending high school and when I graduate school I intend to study Computer Science at University. I have been making cool ", rx.link("projects", href="projects"), " since 2022.",
                size="5",
            ),
            rx.text(
                rx.el.span("I am interested in farming systems and aviation. One of my goals is to eventually get my private pilots license. I enjoy programming for fun. My favorite programming language is "), rx.el.span("Python 🐍", color="green"), rx.el.span(". I know basic web syntax (HTML, CSS, JS) and a bit of C++ but I would like to properly learn C and C++ soon. I can also write basic C#."),
                size="5"
            ),
            rx.link(
                rx.button("Contact me!"),
                href="/contact"
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )
