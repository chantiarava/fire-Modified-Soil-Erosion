import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------
# GLOBAL STYLE
# -----------------------------------------------------
plt.rcParams.update({
    "font.family": "Times New Roman",
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11
})

file_path = r"E:\DOWNLOADS\erosion_data_spreadsheet.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()
df = df[df["RUSLE Class"] != "Total"]

classes = df["RUSLE Class"].values
x = np.arange(len(classes))
width = 0.35

pre_color  = "#35B60F"
post_color = "#D54949FF"

fig_width = 18.5 / 2.54
fig_height = 14 / 2.54

fig, axes = plt.subplots(2,2,figsize=(fig_width,fig_height))
axes = axes.flatten()

basins = [
    ("Sub Basin 1", "Sub Basin_1 Pre-fire (ha)", "Sub Basin_1 Post-fire (ha)"),
    ("Sub Basin 2", "Sub Basin_2 Pre-fire (ha)", "Sub Basin_2 Post-fire (ha)"),
    ("Sub Basin 3", "Sub Basin_3 Pre-fire (ha)", "Sub Basin_3 Post-fire (ha)"),
    ("Sub Basin 4", "Sub Basin_4 Pre-fire (ha)", "Sub Basin_4 Post-fire (ha)")
]

for i, (title, pre_col, post_col) in enumerate(basins):

    ax = axes[i]

    pre  = df[pre_col].values
    post = df[post_col].values

    ax.bar(x - width/2, pre,  width,
           label="Pre-fire",
           color=pre_color,
           edgecolor="black",
           linewidth=0.8)

    ax.bar(x + width/2, post, width,
           label="Post-fire",
           color=post_color,
           edgecolor="black",
           linewidth=0.8)

    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(classes)

    ax.set_ylabel("Hectares (ha)", fontsize=13)

    ax.grid(axis="y", linestyle="--", alpha=0.3)

    ax.legend(frameon=False, fontsize=10)

# -----------------------------------------------------
# SINGLE COMMON X LABEL
# -----------------------------------------------------
fig.text(
    0.5, 0.04,
    "RUSLE Class (Mg ha⁻¹ yr⁻¹)",
    ha="center",
    fontsize=14,
    fontfamily="Times New Roman"
)

plt.subplots_adjust(
    left=0.08,
    right=0.98,
    top=0.93,
    bottom=0.15,
    wspace=0.25,
    hspace=0.35
)

plt.savefig(
    r"E:\DOWNLOADS\Erosion_Distribution_Final.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()