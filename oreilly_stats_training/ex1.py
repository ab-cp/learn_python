from numpy.random import default_rng
from pandas import period_range, DataFrame
from pathlib import Path

data_dir = Path('data')

rng = default_rng(0)

df = DataFrame(
    index=(idx := period_range('2024-01', freq='M', periods=12)),
    data={
        'MCDW': rng.normal(loc=10_000_000, scale=2_000_000, size=len(idx)), # McDowells
        'HAMB': rng.normal(loc=10_000_000, scale=5_000_000, size=len(idx)), # Out-and-About Burger
        'BGQN': rng.normal(loc=10_500_000, scale=2_000_000, size=len(idx)), # Burger Queen
    },
).clip(0, 1e12).round(-2).astype(int)
df.loc['2024-02', 'MCDW'] *= .15
df.loc['2024-06', 'BGQN'] *= 10

data_dir.mkdir(exist_ok=True, parents=True)
filename = data_dir / 'revenue.pkl'
df.to_pickle(filename)

print(
    df,

    # df.agg([
    #     'mean',
    #     'median',
    # ]).map('{:.2f}'.format),
    sep='\n',
)