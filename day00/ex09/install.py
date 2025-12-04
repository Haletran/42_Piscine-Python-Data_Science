import os

def install_package():
    os.system("pip install setuptools wheel")
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("pip install ./dist/ft_package-0.0.1.tar.gz")

def show_package():
    os.system("pip show -v ft_package")

if __name__ == "__main__":
    install_package()
    show_package()
