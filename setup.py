from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    description = readme.read()
    
setup(
    name="AirPy",
    version="1.0.1",
    license="Apache-2.0",
    author="Paul Bayfield",
    keywords="AirPy, Air France, KLM, API, Wrapper",
    description="AirPy, un wrapper pour l'API d'Air France KML. Permet de récupérer les vols au départ et à destinations de CDG.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/AirFranceCDGStats/AirPy"
    project_urls={
        "Documentation": "https://github.com/AirFranceCDGStats/AirPy",
        "Issue tracker": "https://github.com/AirFranceCDGStats/AirPy/issues",
      },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "aiohttp>=3.9.5",
    ]
)