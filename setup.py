from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.readlines()

setup(
    name="messenger_schemas",
    version="0.0.1",
    author="Aidan Fu",
    author_email="aidan.fu000@gmail.com",
    description="Contains all the schemas for the messenger database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRaizer/Messenger-Utils",
    project_urls={
        "Bug Tracker": "https://github.com/TheRaizer/Messenger-Utils/issues"
    },
    license="MIT",
    packages=["messenger_schemas", "messenger_schemas.schema"],
    install_requires=required,
    python_requires=">=3.9",
)
