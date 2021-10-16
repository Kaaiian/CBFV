from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_dscr = (this_directory / "README.md").read_text()
setup(
    name='CBFV',
    version='1.0.1',
    description='Tool for quickly creating a composition-based feature vector',
    long_description=long_dscr,
    long_description_content_type='text/markdown',
    url='https://github.com/kaaiian/CBFV',
    author='Steven Kauwe, Andrew Falkowski, Anthony Wang',
    author_email='jkkauwe@gmail.com',
    packages=['CBFV'],
    package_data={"CBFV": ["element_properties/*.csv"]},
    install_requires=[
                      'numpy',
                      'pandas',
                      'tqdm',
                      'pytest',
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
