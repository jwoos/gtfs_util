import setuptools
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip


pfile = Project(chdir=False).parsed_pipfile


setuptools.setup(
    name='gtfs-parser',
    version='0.0.1',
    description='Access the API MTA through Python bindings',
    url='http://github.com/jwoos/python_gtfs-parser',
    author='Jun Woo Shin',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=convert_deps_to_pip(pfile['packages'], r=False),
    tests_requires=convert_deps_to_pip(pfile['dev-packages'], r=False),
)
