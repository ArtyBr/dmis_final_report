"""Generate pie charts for the questionnaire appendix."""

import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.rcParams.update({
    'font.size': 12,
    'figure.facecolor': 'white',
})

OUTPUT_DIR = 'results_images'

def make_pie(labels, sizes, title, filename, colors=None, use_legend=False):
    fig, ax = plt.subplots(figsize=(6, 5.5) if use_legend else (6, 5))
    if colors is None:
        colors = plt.cm.Set2.colors[:len(labels)]

    def autopct_with_count(pct):
        count = int(round(pct * sum(sizes) / 100))
        return f'{count}\n({pct:.0f}%)'

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=None if use_legend else labels,
        autopct=autopct_with_count,
        colors=colors, startangle=90, textprops={'fontsize': 11},
        pctdistance=0.65,
        radius=1.0,
    )
    for t in autotexts:
        t.set_fontsize(10)
    ax.set_title(title, fontsize=13, fontweight='bold', pad=15)
    if use_legend:
        ax.legend(wedges, labels, loc='lower center', bbox_to_anchor=(0.5, -0.08),
                  ncol=2, fontsize=10, frameon=False)
        fig.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.13)
    else:
        fig.subplots_adjust(left=0.05, right=0.95, top=0.88, bottom=0.05)
    fig.savefig(os.path.join(OUTPUT_DIR, filename), dpi=200)
    plt.close(fig)
    print(f'  Saved {filename}')


# Q1: Driver type
make_pie(
    ['Fully licensed\ndriver', 'Current/prospective\nlearner driver'],
    [20, 3],
    'Q1: Driver Type',
    'q1_driver_type.png',
)

# Q2: Dash-cam ownership
make_pie(
    ['Yes', 'No'],
    [7, 16],
    'Q2: Dash-cam Ownership',
    'q2_dashcam.png',
)

# Q3: Would purchase (non-owners only)
make_pie(
    ['Yes', 'No'],
    [9, 7],
    'Q3: Would Purchase a Dash-cam\nfor This Application (n=16)',
    'q3_purchase.png',
)

# Q4: Preferred recording setup
make_pie(
    ['Dedicated 2-in-1 dashcam system', 'Smartphone with holder', 'Would not use a dual system'],
    [16, 6, 1],
    'Q4: Preferred Recording Setup',
    'q4_setup.png',
    use_legend=True,
)

# Q5: Likelihood of use (bar chart)
fig, ax = plt.subplots(figsize=(6, 4))
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counts = [1, 0, 1, 0, 4, 4, 4, 5, 1, 3]
bars = ax.bar(scores, counts, color=plt.cm.Set2.colors[0], edgecolor='white', width=0.8)
for bar, count in zip(bars, counts):
    if count > 0:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
                str(count), ha='center', va='bottom', fontsize=10)
ax.set_xlabel('Likelihood Score', fontsize=11)
ax.set_ylabel('Number of Respondents', fontsize=11)
ax.set_title('Q5: Likelihood of Using the System', fontsize=13, fontweight='bold')
ax.set_xticks(scores)
ax.set_ylim(0, max(counts) + 1.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'q5_likelihood.png'), dpi=200)
plt.close(fig)
print('  Saved q5_likelihood.png')

# Q8: Willingness to pay
make_pie(
    ['Free (ad-supported)', 'Up to £1.99/mo', 'Up to £4.99/mo', 'Up to £9.99/mo'],
    [10, 3, 6, 4],
    'Q8: Maximum Willingness to Pay (Monthly)',
    'q8_willingness_to_pay.png',
    use_legend=True,
)

print('All charts generated.')
