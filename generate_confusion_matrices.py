import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

labels = ["Left Turn", "Right Turn", "Left LC", "Right LC"]

# Zekany et al. - counts from their Table VII
zekany = np.array([
    [161, 0, 15, 0],
    [0, 133, 21, 0],
    [14, 2, 5, 53],
    [0, 0, 1, 62],
])

# Ours - counts from our matched events
ours = np.array([
    [19, 4, 0, 0],
    [1, 16, 0, 0],
    [0, 0, 19, 1],
    [0, 0, 1, 23],
])

# Compute row percentages
zekany_pct = zekany / zekany.sum(axis=1, keepdims=True) * 100
ours_pct = ours / ours.sum(axis=1, keepdims=True) * 100

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

for ax, data, pct, title in [
    (axes[0], zekany, zekany_pct, "Zekany et al."),
    (axes[1], ours, ours_pct, "Ours"),
]:
    # Determine which diagonal entries beat the other system
    if title == "Zekany et al.":
        other_pct = ours_pct
    else:
        other_pct = zekany_pct

    ax.imshow(pct, cmap="Blues", vmin=0, vmax=100)
    for i in range(4):
        for j in range(4):
            color = "white" if pct[i, j] > 60 else "black"
            bold = (i == j and pct[i, j] > other_pct[i, j])
            weight = "bold" if bold else "normal"
            ax.text(j, i, f"{data[i, j]}\n({pct[i, j]:.0f}%)",
                    ha="center", va="center", fontsize=10, color=color,
                    fontweight=weight)

    ax.set_xticks(range(4))
    ax.set_yticks(range(4))
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Predicted", fontsize=11)
    ax.set_ylabel("Actual", fontsize=11)
    ax.set_title(title, fontsize=12, fontweight="bold")

plt.tight_layout()
plt.savefig("results_images/confusion_matrices.png", dpi=200, bbox_inches="tight")
print("Saved to results_images/confusion_matrices.png")
