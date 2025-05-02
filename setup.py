from setuptools import setup, find_packages

setup(
    name='sedna_sdk',
    version='0.1.0',
    packages=find_packages(),
    description='Sedna Python SDK for communicating with Sedna API',
    author='Stage3 Systems',
    install_requires=[
        "requests>=2.28.0",
    ],
    python_requires='>=3.9',
)
