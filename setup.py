from os import path
import setuptools

this = path.abspath(path.dirname(__file__))
setuptools.setup(
    name="pydoc-markdown-tqdm",
    url="https://github.com/tqdm/tqdm.github.io",
    long_description="Driver for https://tqdm.github.io documentation",
    long_description_content_type="text/x-rst",
    version="0.0.0",
    author="Casper da Costa-Luis",
    author_email="tqdm@caspersci.uk.to",
    packages=setuptools.find_packages(this),
    license="MPL-2.0",
    install_requires=["pydoc-markdown>=3,<4"],
    entry_points={
        "pydoc_markdown.interfaces.Processor": [
            "custom = pydoc_markdown_tqdm:TqdmProcessor"
        ]
    },
)
