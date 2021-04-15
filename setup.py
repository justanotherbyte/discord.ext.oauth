from setuptools import setup, find_packages
import os







DESCRIPTION = 'An async wrapper for the Discord Oauth2 API'

# Setting up
setup(
    name="discord-web",
    version="0.0.1a",
    author="quiktea",
    author_email="wishymovies@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=['discord.py', 'aiohttp'],
    keywords=['python', 'discord.py', 'dashboard', 'discord', 'api', 'discord api', 'web dashboard', 'website', 'web'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={
        "GitHub" : "https://github.com/quiktea/discord-web"
    }
)