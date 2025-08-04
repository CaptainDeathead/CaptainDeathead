import reflex as rx
import json

from plazma_site.navbar import navbar

class Project(rx.Base):
    title: str
    description: str
    demo: str
    github: str

def load_projects() -> list[Project]:
    with open("projects.json", "r") as f:
        dict_data = json.loads(f.read())

    return [Project(
                title=dict_data[project]["title"],
                description=dict_data[project]["description"],
                demo=dict_data[project]["demo"],
                github=dict_data[project]["github"]) for project in dict_data]

class State(rx.Base):
    projects: list[Project]

def show_project(project: Project) -> rx.Component:
    return rx.container(
        rx.box(
            rx.text(
                project.title, size="7", align="center"
            ),
            rx.text(
                project.description, size="5", align="center"
            ),
            rx.hstack(
                rx.cond(
                    project.demo != "",
                    rx.link(rx.button("Demo"), href=project.demo, is_external=True),
                    None
                ),
                rx.cond(
                    project.github != "",
                    rx.link(rx.button("GitHub"), href=project.github, is_external=True),
                    None
                ),
                justify="center",
                align="end",
                padding_top="10px",
            ),
            border="1px solid grey",
            padding="10px",
        ),
        width="100%"
    )

def projects() -> rx.Component:
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("My Projects!", size="9"),

            rx.foreach(State.projects, show_project),

            padding_top=20,
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )

State.projects = load_projects()