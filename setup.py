import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sqlacodegen


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='flask-sqlacodegen',
    description='Automatic model code generator for SQLAlchemy with Flask support',
    long_description=open('README.rst').read(),
    version=sqlacodegen.version,
    author='Kamil Sindi',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Topic :: Database',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['sqlalchemy', 'sqlacodegen', 'flask'],
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=(
        'SQLAlchemy >= 1.2.0',
        'inflect >= 0.2.0'
    ),
    tests_require=['pytest', 'pytest-pep8'],
    cmdclass={'test': PyTest},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'flask-sqlacodegen=sqlacodegen.main:main'
        ]
    }
)
