from setuptools import setup, find_namespace_packages


setup(
    name="zycelium.dataconfig",
    version="0.0.1",
    description="App Configuration Library",
    packages=find_namespace_packages(include=["zycelium.*"]),
    package_dir={"": "src"},
    zip_safe=False,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "click>=8.0",
        "configobj>=5.0",
    ],
    extras_require={
        "devel": [
            "bump2version>=1.0",
            "pytest>=6.2",
        ],
    },
)
