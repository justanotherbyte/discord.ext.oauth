from setuptools import setup

with open('requirements.txt',  'r') as f:
    requirements = f.read().splitlines()


with open('README.md', encoding='utf-8') as f:
    readme = f.read()

# speedups for aiohttp
extras_require = {
    'speedups': 'aiohttp[speedups]',
}

setup(
    name='discord-ext-oauth',
    author='moanie',
    python_requires='>=3.7.0',
    url='https://github.com/moanie/discord.ext.oauth',
    version="0.2.4",
    packages=[
        "discord/ext/oauth",
        "discord/ext/oauth/no_async"
    ],
    license='MIT',
    description='An asynchronous OAuth2 extension for discord.py.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)