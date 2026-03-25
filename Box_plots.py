import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------------------------
# GLOBAL STYLE (same look)
# -----------------------------------------------------
plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 10,
    "axes.titlesize": 14,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9
})

# -----------------------------------------------------
# FILE LOCATION
# -----------------------------------------------------
folder = r"E:\Downloads"

files = [
    "BoxPlot_CSV_B1.csv",
    "BoxPlot_CSV_B2.csv",
    "BoxPlot_CSV_B3.csv",
    "BoxPlot_CSV_B4.csv"
]

titles = ["Sub Basin 1","Sub Basin 2","Sub Basin 3","Sub Basin 4"]

# -----------------------------------------------------
# FIGURE SIZE (same)
# -----------------------------------------------------
fig_width = 18/2.54
fig_height = 11/2.54

fig, axes = plt.subplots(3,4,figsize=(fig_width,fig_height))

# -----------------------------------------------------
# SAME BLUE STYLE
# -----------------------------------------------------
style = dict(
    widths=0.20,
    patch_artist=True,
    whis=1.5,
    flierprops=dict(marker='o',markersize=1.5),
    medianprops=dict(color='orange',linewidth=0.5),
    boxprops=dict(facecolor='#1f77b4',linewidth=1.0),
    whiskerprops=dict(linewidth=1.0),
    capprops=dict(linewidth=1.0)
)

for i,file in enumerate(files):

    path = os.path.join(folder,file)
    df = pd.read_csv(path)

    df = df.drop(columns=['.geo'], errors='ignore')
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.dropna()

    pos = [1,1.35]

    # ---------------- ROW 1 → C FACTOR ----------------
    axes[0,i].boxplot(
        [df['C_pre'],df['C_post']],
        positions=pos,
        **style
    )

    axes[0,i].set_title(titles[i])
    axes[0,i].set_xticks(pos)
    axes[0,i].set_xticklabels(['pre','post'])
    axes[0,i].set_ylim(0,1)

    if i == 0:
        axes[0,i].set_ylabel("C Factor", fontsize=13)

    # ---------------- ROW 2 → K FACTOR ----------------
    axes[1,i].boxplot(
        [df['K_pre'],df['K_post']],
        positions=pos,
        **style
    )

    axes[1,i].set_xticks(pos)
    axes[1,i].set_xticklabels(['pre','post'])
    axes[1,i].set_ylim(0.03,0.06)

    if i == 0:
        axes[1,i].set_ylabel("K Factor", fontsize=13)

    # ---------------- ROW 3 → RUSLE A ----------------
    axes[2,i].boxplot(
        [df['A_pre'],df['A_post']],
        positions=pos,
        **style
    )

    axes[2,i].set_xticks(pos)
    axes[2,i].set_xticklabels(['pre','post'])
    axes[2,i].set_ylim(0,150)

    if i == 0:
        axes[2,i].set_ylabel("RUSLE A\n(Mg ha⁻¹ yr⁻¹)", fontsize=13)

# -----------------------------------------------------
# SPACING (unchanged)
# -----------------------------------------------------
plt.subplots_adjust(
    left=0.10,
    right=0.99,
    top=0.94,
    bottom=0.12,
    wspace=0.30,
    hspace=0.60
)

plt.savefig(
    r"E:\Downloads\FINAL_RUSLE_BOXPLOT_UPDATED.png",
    dpi=300
)

plt.show()