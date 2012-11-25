from setuptools import setup
import sys
import pypeline

setup(
    name = "Pypeline",
    version = pypeline.version,
    url = 'http://github.com/squioc/Pypeline',
    author = 'Sebastien Quioc',
    author_email = 'sebastien.quioc@yahoo.com',
    description = "",
    long_description=open('README.md').read(),
    packages = ['pypeline'],
    include_package_data = True,
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: ',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
)
