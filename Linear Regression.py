import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import statsmodels.api as sm

# -----------------------------------------------------
# Folder path (UNCHANGED)
# -----------------------------------------------------
folder = r"E:\Downloads"

files = [
    "Regression_CSV_B1.csv",
    "Regression_CSV_B2.csv",
    "Regression_CSV_B3.csv",
    "Regression_CSV_B4.csv"
]

titles = ["SUB BASIN 1","SUB BASIN 2","SUB BASIN 3","SUB BASIN 4"]

# YOUR PROVIDED R² VALUES
r2_values = [0.41, 0.69, 0.32, 0.09]

# -----------------------------------------------------
# GLOBAL STYLE (Match Your Image)
# -----------------------------------------------------
plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 12,
    "axes.titlesize": 15,
    "axes.labelsize": 13
})

# -----------------------------------------------------
# FIGURE SIZE
# -----------------------------------------------------
fig_width = 18/2.54
fig_height = 13/2.54

fig, axes = plt.subplots(2,2,figsize=(fig_width,fig_height))
axes = axes.flatten()

for i,file in enumerate(files):

    path = os.path.join(folder,file)
    df = pd.read_csv(path)
    df = df.apply(pd.to_numeric,errors='coerce').dropna()

    # -------------------------------------------------
    # MASK NON-FIRE PIXELS
    # -------------------------------------------------
    df = df[df['dNBR'] >= 0.1]

    # FULL DATA FOR REGRESSION
    X_full = df['dNBR'].values
    Y_full = df['dRUSLE'].values

    # -------------------------------------------------
    # REGRESSION (FULL DATA)
    # -------------------------------------------------
    X_sm = sm.add_constant(X_full)
    model = sm.OLS(Y_full, X_sm).fit()

    m = model.params[1]
    c = model.params[0]

    # -------------------------------------------------
    # REDUCE PIXELS FOR VISUAL CLARITY (30%)
    # -------------------------------------------------
    np.random.seed(42)

    sample_fraction = 0.20

    sample_indices = np.random.choice(
        len(X_full),
        size=int(len(X_full)*sample_fraction),
        replace=False
    )

    X = X_full[sample_indices]
    Y = Y_full[sample_indices]

    x_line = np.linspace(0,1,200)
    y_line = m*x_line + c

    ax = axes[i]

    # SCATTER
    ax.scatter(
        X, Y,
        s=8,
        color='blue',
        alpha=0.30
    )

    # REGRESSION LINE
    ax.plot(
        x_line, y_line,
        color='black',
        linewidth=1.8
    )

    # AXIS LIMITS
    ax.set_xlim(0,1)
    ax.set_ylim(0,150)

    ax.set_title(titles[i], pad=6)

    # AXIS LABELS
    if i in [2,3]:
        ax.set_xlabel("dNBR")

    if i in [0,2]:
        ax.set_ylabel("dRUSLE")

    # EQUATION + YOUR R² VALUES
    ax.text(
        0.05,
        0.92,
        f"y = {m:.2f}x + {c:.2f}\nR² = {r2_values[i]:.2f}",
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment='top'
    )

# -----------------------------------------------------
# SPACING
# -----------------------------------------------------
plt.subplots_adjust(
    left=0.09,
    right=0.98,
    bottom=0.09,
    top=0.94,
    wspace=0.18,
    hspace=0.30
)

# SAVE
plt.savefig(
    r"E:\Downloads\Fire_dNBR_dRUSLE_Final.png",
    dpi=300
)

plt.show()