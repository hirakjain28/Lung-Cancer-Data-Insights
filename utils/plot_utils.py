# utils/plot_utils.py

import matplotlib.pyplot as plt

def set_plot_style():
    plt.style.use('seaborn-whitegrid')
    plt.rcParams.update({
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10
    })
