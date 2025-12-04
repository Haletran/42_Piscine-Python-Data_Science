import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="ft_package",
    version="0.0.1",
    author="Haletran",
    author_email="bapasqui@student.42angouleme.fr",
    packages=["ft_package"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
