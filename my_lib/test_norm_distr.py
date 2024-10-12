import pandas as pd
from pandas import DataFrame
from scipy.stats import shapiro, skew, kurtosis


def test_norm_distr(data: pd.Series) -> DataFrame | None:
    """Функция проверки признака на Нормальность распределения"""

    # Задание пороговов принятия решения
    SKEW_threshold = 0.3
    KURTOSIS_threshold = 0.3

    test_df = pd.DataFrame(columns=['score_value', 'condition', 'conclusion'])

    if isinstance(data, pd.Series):
        values = data.dropna().values
    else:
        print(f'Неверный тип данных на входе: {type(data)}')
        print('Необходимый тип данных: pd.Series')
        return

    shapiro_res = pd.DataFrame()
    shapiro_score = shapiro(values)
    shapiro_res['score_value'] = [shapiro_score[1]]
    shapiro_res['condition'] = ['p_value < 0.05']
    shapiro_res['conclusion'] = ['normal' if shapiro_score[1] < 0.05 else 'abnormal']

    skew_res = pd.DataFrame()
    skew_score = skew(values)
    skew_res['score_value'] = [skew_score]
    skew_res['condition'] = ['abs(score_value) < 0.3']
    skew_res['conclusion'] = ['normal' if abs(skew_score) < SKEW_threshold else 'abnormal']

    kurtosis_res = pd.DataFrame()
    kurtosis_score = kurtosis(values)
    kurtosis_res['score_value'] = [kurtosis_score]
    kurtosis_res['condition'] = ['score_value < 0.3']
    kurtosis_res['conclusion'] = ['normal' if kurtosis_score < KURTOSIS_threshold else 'abnormal']

    test_df = pd.concat([test_df, shapiro_res, skew_res, kurtosis_res])
    test_df.index = ['shapiro', 'skew', 'kurtosis']

    return test_df
