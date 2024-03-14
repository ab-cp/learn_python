from scipy.stats import f
from numpy import linspace
from matplotlib.pyplot import subplots, show, rc


for ddof_num, ddof_den in [(1, 1), (2, 1), (5, 1), (10, 1)]:
    fig, ax = subplots(dpi=180)
    ax.set_title(f'{ddof_num = }; {ddof_den = }')
    ax.plot(
        sp := linspace(0, 5, 100),
        f(dfn=ddof_num, dfd=ddof_den).pdf(sp),
    )
    show()