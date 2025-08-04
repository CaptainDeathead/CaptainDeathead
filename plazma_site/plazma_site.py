"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from plazma_site.navbar import navbar

from plazma_site.projects import projects
from plazma_site.about import about
from plazma_site.contact import contact

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Plazma!", size="9"),
            rx.text(
                "Plazma is the homepage for all of my personal projects!",
                size="5",
            ),
            rx.link(
                rx.button("See more about me!"),
                href="/about"
            ),
            rx.text(
                "Currently working on: ",
                rx.link(rx.code("Farm CEO"), href="/farmCEO"),
                ", ",
                rx.link(rx.code("Plaching"), href="/plaching"),
                ", ",
                rx.link(rx.code("Molten"), href="/molten"),
                "."
            ),
            rx.link(
                rx.button("View all projects!"),
                href="/projects"
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )


app = rx.App()

description = "The home for Plazma projects and information about me."
image = "https://plazmasoftware.com/assets/banner.png"

meta = [
    {"property": "og:title", "content": "Plazma Software"},
    {"property": "og:description", "content": description},
    {"property": "og:image", "content": image},
    {"property": "og:url", "content": "https://plazmasoftware.com/"},
    {"name": "twitter:card", "content": image},
    {"name": "twitter:title", "content": "Plazma Software"},
    {"name": "twitter:description", "content": description},
    {"name": "twitter:image", "content": image},
]

app.add_page(index, title="Plazma Software", description=description, meta=meta)
app.add_page(projects, title="Plazma Software - Projects", description=description, meta=meta)
app.add_page(about, title="Plazma Software - About", description=description, meta=meta)
app.add_page(contact, title="Plazma Software - Contact", description=description, meta=meta)