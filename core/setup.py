from setuptools import setup, find_packages

__version__ = '1.0'

setup(name="APTF", packages=find_packages())

EPS = {
    'console_scripts': [
        'aptf-runner = aptf.lib.runner:main'
    ]
}


setup(
        name='aptf-core',
        version=__version__,
        description='APT Test Framework',
        long_description='TBD...',
        keywords='testing',
        author='Denys Omelchuk',
        author_email='dionisom@gmail.com',
        license='All Yours',
        zip_safe=False,
        packages=find_packages(exclude=['data']),
        include_package_data=True,
        entry_points=EPS,
        dependency_links=["https://github.com/denysom/APTF"],
        install_requires=[
                'pytest',
                'pyyaml',
                ],
        namespace_packages=['aptf'])
