from pathlib import Path
from setuptools import find_namespace_packages, setup


# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

setup(
    name='src',
    version=0.1,
    description='A machine learning service for calculating the price and recommend real estate',
    author_email="contato@fernandofilho.com",
    author='Fernando Filho',
    license='MIT',
    python_requires=">=3.7",
    install_requires=[required_packages],
)
