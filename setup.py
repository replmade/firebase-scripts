from setuptools import setup, find_packages

setup(
    name='firebase-spells-py',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
        'requests',
    ],
    author='ochsec',
    description='Firebase spells for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ochsec/firebase-spells-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)