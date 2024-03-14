from pathlib import Path
from numpy.random import default_rng
from pandas import DataFrame, date_range, to_timedelta, Series
from string import ascii_lowercase

rng = default_rng(0)

data_dir = Path('data')
data_dir.mkdir(exist_ok=True, parents=True)

index = date_range('2020-01-01', freq='T', periods=24 * 31 * 60)
index += to_timedelta(rng.integers(60, size=len(index)), unit='s')

pop = Series(
    data=rng.normal(loc=10, scale=7.5, size=len(index)),
    index=index,
).clip(1.35, 100).sample(frac=.95, random_state=rng.bit_generator).round(2)

samp = pop.sample(frac=0.10, random_state=rng.bit_generator)

filename = data_dir / 'avg-sale.population.pkl'
pop.to_pickle(filename)

filename = data_dir / 'avg-sale.sample.pkl'
samp.to_pickle(filename)

print(
    pop.head(),
    samp.head(),
    sep='\n{}\n'.format('\N{box drawings light horizontal}' * 40),
)