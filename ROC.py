import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# FILE PATH
base_path = r"C:\Users\ssc39\Downloads\\"

files = [
    "Erosion_Points_B1.csv",
    "Erosion_Points_B2.csv",
    "Erosion_Points_B3.csv",
    "Erosion_Points_B4.csv"
]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, file in enumerate(files):

    df = pd.read_csv(base_path + file)

    df = df[['Class', 'RASTERVALU']].dropna()

    df['Class'] = pd.to_numeric(df['Class'], errors='coerce')
    df['RASTERVALU'] = pd.to_numeric(df['RASTERVALU'], errors='coerce')

    df = df.dropna()

    y_true = df['Class']
    y_scores = df['RASTERVALU']

    if len(y_true.unique()) < 2:
        print(f"Sub-basin {i+1} skipped (only one class)")
        continue

#roc
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    auc = roc_auc_score(y_true, y_scores)

    ax = axes[i]

    ax.plot(fpr, tpr, linewidth=2)
    ax.plot([0,1], [0,1], linestyle='--', linewidth=1)

    ax.set_title(f'Sub-basin {i+1}', fontsize=11)
    ax.set_xlabel('False Positive Rate', fontsize=9)
    ax.set_ylabel('True Positive Rate', fontsize=9)

    # AUC box
    ax.text(0.55, 0.1, f'AUC = {auc:.3f}',
            transform=ax.transAxes,
            bbox=dict(facecolor='white', edgecolor='black'))

    ax.grid(True, linestyle='--', alpha=0.5)

# --------------------------------------------------
# FINAL OUTPUT
# --------------------------------------------------
plt.tight_layout()
plt.savefig("ROC_Subbasins_Final.png", dpi=300)
plt.show()