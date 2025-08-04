import reflex as rx

config = rx.Config(
    app_name="plazma_site",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)