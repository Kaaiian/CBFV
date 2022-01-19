# CBFV Package
Tool to quickly create a composition-based feature vectors from materials datafiles.

# Installation
The source code is currently hosted on GitHub at: https://github.com/kaaiian/CBFV

Binary installers for the latest released version are available at the <a href="https://pypi.org/project/cbfv/">Python Package Index (PyPI)</a>
```bash
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

```python
from CBFV import composition
X, y, formulae, skipped = composition.generate_features(df)
```

## Extended Functionality

The featurization scheme can be adjusted by calling the the `elem_prop` parameter. The following featurization schemes are included within CBFV:
- jarvis
- magpie
- mat2vec
- oliynyk (default)
- onehot
- random_200

Duplicate formula handeling is controlled by the `drop_duplicates` parameter. It is set to `False` by default to preserve datapoints containing variation outside of their formula. For example, heat capacity measurements performed for the same material at different temperatures.

The `extend_features` parameter is used to specify whether columns outside of `['formula', 'target']` should be considered during featurization. It is set to `False` by default to exclude nuisance information from consideration. Setting `extend_features=True` would allow additional information (i.e. `['temperature', 'pressure']`) to be preserved.

The `sum_feat` parameter specifies whether to calculate the sum features when generating the CBFVs for the chemical formulae. It is set to `False` by default.

Calling `generate_features` with these parameters can be implemented as follows:

formula | target | temp
---|---|---
Tc1V1 | 248.539 | 373
Tc1V1 | 66.8444 | 473
Cd3N2 | 91.5034 | 273

```python
from CBFV import composition
X, y, formulae, skipped = composition.generate_features(df,
                                                        elem_prop='magpie',
                                                        drop_duplicates=False,
                                                        extend_features=True,
                                                        sum_feat=True)
```
