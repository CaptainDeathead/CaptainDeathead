import reflex as rx

config = rx.Config(
    app_name="plazma_site",
    api_url="http://plazmasoftware.com:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
