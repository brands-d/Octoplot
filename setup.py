from setuptools import setup

DESCRIPTION = 'Standard data represensetion routines for the ab-initio'\
    'code Octopus.'

with open('README.rst', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='helloworld',
    version='0.0.1-dev',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    url='https://github.com/brands-d/Octoplot',
    author='Dominik Brandstetter',
    author_email='dominik.brandstetter@edu.uni-graz.at',
    py_modules=['octoplot'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'dev': ['bump2version==1.0.1', 'pytest==6.2.5','tox==3.24.3'],
        'maintainer': ['sphinx==4.1.2', 'check-manifest==0.46',
                       'twine==3.4.2']},
    classifiers=['Development Status :: 1 - Planning',
                 'Topic :: Documentation :: Sphinx',
                 'Natural Language :: English',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Topic :: Communications :: Email',
                 'Topic :: Scientific/Engineering :: Physics',
                 'Topic :: Software Development :: Version Control :: Git',
                 'Topic :: Text Processing :: Markup :: reStructuredText',
                 'License :: OSI Approved :: MIT License'
                 ]
)
