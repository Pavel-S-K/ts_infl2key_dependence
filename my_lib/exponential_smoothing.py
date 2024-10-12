import pandas as pd


def exponential_smoothing(series: pd.Series, alpha: float) -> pd.Series:
    """
        Функция экспоненциального сглаживания
        series - временной ряд
        alpha - float [0.0, 1.0], пареметр сглаживания
    """
    result = [series[0]]  # Первое значение без изменений
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])

    result = pd.Series(result, name=f'{series.name}_exp_sm')
    result.index = series.index

    return result
