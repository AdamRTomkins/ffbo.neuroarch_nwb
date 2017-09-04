try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="neuroarch_nwp",
    version="0.1.1",
    description="",
    long_description=open('README.md').read(),
    author="Adam R. Tomkins",
    author_email="a.tomkins@sheffield.ac.uk",
    url="TBD",
    keywords=["NWB",
              "Neurodata Without Borders"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        ],
    install_requires = [
        'nwb'
    ],
    packages=["neuroarch_nwb"]
)
