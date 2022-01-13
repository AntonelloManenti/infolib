from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name="infolib",
        version="0.1.3",
        packages=find_packages(),
        description="A small, simple and sturdy library to overview our PandasDataframe",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/AntonelloManenti/infolib",
        author="Antonello Manenti",
        author_email="antonellomanenti@gmail.com",
        license="MIT",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.10",
        ],
        install_requires=[
            "numpy",
            "pandas",
            "ipython",
            "more-itertools",
            "psutil",
            "regex",
            ],
        python_requires='>=3.6, <3.10',
        entry_points="""
        [console_scripts]
        contacts=app:cli
        """,
        )
