from setuptools import setup, find_packages

setup(
    name='ReprTraceback',
    version='1.0.2',
    description='Improve stack traces with the values associated with each argument in each frame.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='NateRiz',
    author_email='natezriz@gmail.com',
    url='https://github.com/NateRiz/ReprTraceback',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
)
