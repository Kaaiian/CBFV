from setuptools import setup

setup(
    name='cbfv',
    version='0.1.0',
    description='Tool for quickly creating a composition-based feature vector',
    url='https://github.com/kaaiian/CBFV',
    author='Steven Kauwe, Andrew Falkowski, Anthony Wang',
    author_email='jkkauwe@gmail.com',
    packages=['CBFV'],
    install_requires=[
                      'numpy',
                      'pandas',
                      'tqdm',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
