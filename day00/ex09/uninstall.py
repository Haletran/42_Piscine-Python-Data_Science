import os


def uninstall_package():
    os.system("pip uninstall -y ft_package")
    os.system("rm -rf build dist ft_package.egg-info")


if __name__ == "__main__":
    uninstall_package()
