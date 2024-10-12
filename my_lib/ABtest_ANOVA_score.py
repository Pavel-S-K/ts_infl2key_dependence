import pandas as pd
from sklearn.feature_selection import f_classif


def ABtest_ANOVA_score(a: pd.Series, b: pd.Series) -> pd.DataFrame:
    """
    Функция проведения ANOVA теста
    a - categoric target
    b - cont. feature
    """

    feature = b
    target = a

    scores_list = []
    p_value_list = []
    scores = pd.DataFrame()

    local_df = pd.concat([feature, target], axis=1).dropna()
    local_df.columns = ['feature', 'target']

    test_results = f_classif(local_df[['feature']], local_df[['target']])

    scores_list.append(test_results[0][0])
    p_value_list.append(test_results[1][0])

    scores['ANOVA_score'] = scores_list
    scores['p_value'] = p_value_list
    scores['feature'] = [feature.name]
    scores['target'] = [target.name]

    return scores
