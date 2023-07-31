from setuptools import setup, find_packages

setup(
    name="fast_api_crud_python",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi[all]",
        "uvicorn[standard]",
        "sqlalchemy",
        "pydantic",
        "databases"
    ],
)
