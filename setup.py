import setuptools


setuptools.setup(
    name='gtfs-parser',
    version='0.0.1',
    description='Access the API MTA through Python bindings',
    url='http://github.com/jwoos/python_gtfs-parser',
    author='Jun Woo Shin',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'uvloop',
        'aiohttp',
        'protobuf',
        'requests',
        'SQLAlchemy',
        'gtfs-realtime-bindings',
        'aiofiles',
    ],
    tests_requires=[
        'pytest',
        'ipython',
    ],
)
