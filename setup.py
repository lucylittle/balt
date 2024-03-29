#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.1'

setup(
    name="balt",
    version=version,
    packages=find_packages(),
    zip_safe=False,
    description="balt is sample code for interviews",
    long_description="""\
""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    dependency_links=[
    ],
    url='',
    license='BSD',
    include_package_data=True,
    install_requires=[
        'Django>=1.5.3,<1.6',
        'py-bcrypt',
        'lxml>=3.2.0',
        'html5lib',
        'cssselect',

        'django-nose',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
