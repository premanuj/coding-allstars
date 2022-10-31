import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Coding All Stars",
    version="0.0.1",
    author="@premsubedi",
    author_email="mesubedianuj@gmail.com",
    description="Scraping Coursera",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPT",
    python_requires=">=3.9",
    install_requires=[
        "django==3.2.5",
        "gunicorn==20.0.4",
        "redis==3.5.3",
        "requests==2.27.1",
        "python-dotenv==0.21.0"
    ],
)
