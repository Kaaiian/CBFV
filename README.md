# CBFV Package
Tool to quickly create a composition-based feature vectors from materials datafiles.

# Installation
The source code is currently hosted on GitHub at: https://github.com/kaaiian/CBFV

Binary installers for the latest released version are available at the <a href="https://pypi.org/project/cbfv/">Python Package Index (PyPI)</a>
```
# PyPI
pip install CBFV
```

## Making the composition-based feature vector
The CBFV package assumes your data is stored in a pandas dataframe of the following structure:

formula | target
---|---
Tc1V1 | 248.539
Cu1Dy1 | 66.8444
Cd3N2 | 91.5034

To featurize this data, the `generate_features` function can be called as follows:

```
from CBFV import composition
X, y, formulae, skipped = composition.generate_features(df, elem_prop='oliynyk')
```

The featurization scheme can be adjusted using the `elem_prop` variable. The following featurization schemes are included within CBFV:
- jarvis
- magpie
- mat2vec
- oliynyk
- onehot
- random_200
