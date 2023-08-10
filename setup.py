from setuptools import find_packages, setup


if __name__ == "__main__":
    setup(
        packages=find_packages(exclude=["docs", "test", "scripts", "examples"]),
        include_package_data=True
    )
