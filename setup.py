from setuptools import setup

setup(
    name='cbfv',
    version='1.0.1',
    description='Tool for quickly creating a composition-based feature vector',
    url='https://github.com/kaaiian/CBFV',
    author='Steven Kauwe, Andrew Falkowski, Anthony Wang',
    author_email='jkkauwe@gmail.com',
    packages=['cbfv'],
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
