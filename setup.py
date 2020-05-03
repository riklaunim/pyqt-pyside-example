from setuptools import setup, find_packages

setup(
    name='pyqt-pyside-example',
    version='0.1',
    description='sentiment-analysis-example.',
    author='Piotr Malinski',
    author_email='riklaunim@gmail.com',
    url='https://github.com/riklaunim/pyqt-pyside-example',
    setup_requires=['pytest-runner'],
    package_dir={'': 'app'},
    packages=find_packages(where='app'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
    ],
)
