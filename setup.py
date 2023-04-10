from setuptools import setup

setup(
    name="comp0034-week7",
    packages=["paralympic_app", "flask_app", "flask_bp", "iris_app"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["flask"],
)
