import pandas as pd
from scipy.stats import spearmanr


def ABtest_spearmanr_score(a: pd.Series, b: pd.Series) -> pd.DataFrame:
    """
    Расчет коэффициента корреляции Спирмана
    a - cont. target
    b - cont. feature
    """

    feature = b
    target = a

    scores_list = []
    p_value_list = []
    scores = pd.DataFrame()

    local_df = pd.concat([feature, target], axis=1).dropna()
    local_df.columns = ['feature', 'target']

    test_results = spearmanr(local_df['feature'].values, local_df['target'].values)

    scores_list.append(test_results[0])
    p_value_list.append(test_results[1])

    scores['spearmanr_score'] = scores_list
    scores['p_value'] = p_value_list
    scores['feature'] = [feature.name]
    scores['target'] = [target.name]

    return scores
