from setuptools import setup, find_packages


with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="docker-utils",
    version="0.1.0",
    description="Additional Docker helper method",
    long_description=readme,
    author='Ayoub ED-DAFALI',
    author_email='ayoubensalem@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    setup_requires=[],
    install_requires=["docker"],
    entry_points={
        'console_scripts': [
            'hybrd=docker-utils.cli:main'],
    }
)

