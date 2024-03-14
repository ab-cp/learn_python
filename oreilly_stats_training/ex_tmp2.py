from pandas import read_pickle, DataFrame
from pathlib import Path
from numpy import sqrt, newaxis
from scipy.stats import f, f_oneway

data_dir = Path('data')

population = read_pickle(data_dir / 'monthly-revenue.population.pkl')
sample = read_pickle(data_dir / 'monthly-revenue.sample.pkl')

row_means = sample.mean(axis=1).var(ddof=1) * sample.shape[1]
row_vars  = sample.var(axis=1, ddof=1).mean()

col_means = sample.mean(axis=0).var(ddof=1) * sample.shape[0]
col_vars  = sample.var(axis=0, ddof=1).mean()

print(
    # population,
    # sample,
    row_means / row_vars,
    col_means / col_vars,

    f_oneway(*sample.to_numpy()),   # H₀: there was no row effect
    f_oneway(*sample.to_numpy().T), # H₀: there was no col effect

    sep='\n{}\n'.format('\N{box drawings light horizontal}' * 40)
)