import os
import numpy as np
import pandas as pd

from cbfv import composition as cmp


# %% dummy tests
def test_answer1():
    assert True == True

def test_answer2():
    assert 1 == True


# %%
# test for presence of all element properties
ELEM_PROPS = ['jarvis','magpie','mat2vec','oliynyk','onehot','random_200']
ELEM_PROP_FILES = [f'{ep}.csv' for ep in ELEM_PROPS]

def get_elem_props():
    ep_dir = os.path.join('cbfv', 'element_properties')
    return os.listdir(ep_dir)

def test_avail_elem_props():
    elem_props = get_elem_props()
    assert set(ELEM_PROP_FILES) == set(elem_props)


# %%
# test 'NaN' as chemical formula
def test_nans():
    cols = ['formula', 'target']
    formulae = ['NaN']

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = range(len(formulae))

    output = cmp.generate_features(df)
    out0, out1, out2, out3 = output
    assert out0.shape[0] != 0 and out0.shape[1] != 0


# %%
# test returned variables are correct
def test_outputs():
    cols = ['formula', 'target']
    formulae = ['NaCl', 'Al2O3', 'NaCl', 'EsNo', 'BaTiO3', 'GaN', 'Am']
    targets = np.random.randn((len(formulae)))

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = targets

    output = cmp.generate_features(df)
    out0, out1, out2, out3 = output

    # check returns are the correct variable type
    assert (isinstance(out0, pd.core.frame.DataFrame)
            and isinstance(out1, pd.core.series.Series)
            and isinstance(out2, pd.core.series.Series)
            and isinstance(out3, list))

    # check returned targets are equal to originally specified
    assert np.allclose(out1, targets, rtol=1e-6, atol=1e-10)

    # check returned formulae are equal to originally specified
    assert np.all(out2.values == formulae)

    # check exotic elements are skipped
    assert set(out3) == set(['EsNo', 'Am'])


# %%
# test drop_duplicates drop duplicate chemical formulae
def test_drop_duplicates():
    cols = ['formula', 'target']
    formulae = ['NaCl', 'Al2O3', 'NaCl']

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = range(len(formulae))

    output = cmp.generate_features(df)
    out0, out1, out2, out3 = output
    assert out0.shape[0] == len(formulae)

    output = cmp.generate_features(df, drop_duplicates=True)
    out0, out1, out2, out3 = output
    assert out0.shape[0] == len(formulae) - 1


# %%
# test extend_features generation of extended features
def test_extend_features():
    cols = ['formula', 'target', 'extra_feature1', 'extra_feature2']
    formulae = ['NaCl', 'Al2O3', 'SiO2']

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = range(len(formulae))
    df['extra_feature1'] = df['target'] + 0.5
    df['extra_feature2'] = df['target'] + 1.5

    output = cmp.generate_features(df, extend_features=True)
    out0, out1, out2, out3 = output
    assert 'extra_feature1' in out0.columns and 'extra_feature2' in out0.columns


# %%
# test sum_feat including sum-based features to CBFV
def test_sum_feat():
    cols = ['formula', 'target']
    formulae = ['NaCl', 'Al2O3', 'SiO2']

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = range(len(formulae))

    output = cmp.generate_features(df, elem_prop='oliynyk', sum_feat=False)
    out0, out1, out2, out3 = output
    assert out0.shape[1] == 264

    output = cmp.generate_features(df, elem_prop='oliynyk', sum_feat=True)
    out0, out1, out2, out3 = output
    assert out0.shape[1] == 308


# %%
# test mini which selects random features to generate a mini CBFV (dev testing)
def test_mini():
    cols = ['formula', 'target']
    formulae = ['NaCl', 'Al2O3', 'SiO2']

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = range(len(formulae))

    output = cmp.generate_features(df, elem_prop='oliynyk', mini=False)
    out0, out1, out2, out3 = output
    orig_feats = out0.shape[-1]

    output = cmp.generate_features(df, elem_prop='oliynyk', mini=True)
    out0, out1, out2, out3 = output
    new_feats = out0.shape[-1]

    assert new_feats < orig_feats


# %%
# test generation of features
def test_all_elem_props():
    cols = ['formula', 'target', 'extra_feature1', 'extra_feature2']
    formulae = ['C', 'B', 'F', 'V', 'NaCl', 'Al2O3', 'SiO2']

    df = pd.DataFrame(columns=cols)
    df['formula'] = formulae
    df['target'] = range(len(formulae))
    df['extra_feature1'] = df['target'] + 0.5
    df['extra_feature2'] = df['target'] + 1.5

    for elem_prop in ELEM_PROPS:
        output = cmp.generate_features(df, elem_prop=elem_prop)
        out0, out1, out2, out3 = output
