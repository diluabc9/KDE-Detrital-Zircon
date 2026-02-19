import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# TRUE R-STYLE BANDWIDTH (Silverman)

def r_bandwidth(data):
    data = np.asarray(data)
    sd = np.std(data, ddof=1)
    iqr = np.subtract(*np.percentile(data, [75, 25]))
    return 0.9 * min(sd, iqr / 1.34) * (len(data) ** (-1 / 5))



# KDE WITH R-JAGGED SHARPNESS  (Silverman / 3)

def kde_r(data, xgrid):
    data = np.asarray(data)
    bw = r_bandwidth(data) / 3.0
    return np.sum(
        np.exp(-0.5 * ((xgrid[:, None] - data) / bw) ** 2),
        axis=1
    ) / (len(data) * bw * np.sqrt(2 * np.pi))



# USER INPUTS

csv_file = "input.csv"
output_path = "KDE_output.jpeg"

fig_width = 7
fig_height_per_plot = 3
kde_points = 500
hist_bin_size = 50



# READ CSV (2-ROW HEADER)

df = pd.read_csv(csv_file, header=[0, 1], encoding="latin1")
df.columns = pd.MultiIndex.from_tuples(
    [(str(c[0]).strip(), str(c[1]).strip()) for c in df.columns]
)
df = df.apply(pd.to_numeric, errors="coerce")



# GROUP COLUMNS

categories = {}
for cat, sub in df.columns:
    categories.setdefault(cat, []).append(sub)

n_plots = len(categories)



# GLOBAL X-LIMITS

data_max = np.nanmax(df.values)
global_min = 0

if data_max <= 100:
    base = 10
elif data_max <= 500:
    base = 50
elif data_max <= 1000:
    base = 100
elif data_max <= 5000:
    base = 500
else:
    base = 1000

global_max = int(np.ceil(data_max / base) * base)



# PLOTTING SETUP

fig, axes = plt.subplots(
    n_plots, 1,
    figsize=(fig_width, fig_height_per_plot * n_plots),
    sharex=True
)

if n_plots == 1:
    axes = [axes]

colors = plt.cm.tab10.colors



# LOOP THROUGH CATEGORIES

for ax, (category, subcats) in zip(axes, categories.items()):

    clean_subcats = [s.strip() for s in subcats]

    if len(clean_subcats) == 1:
        sublist = [(category, clean_subcats[0])]
    else:
        sublist = [
            (category, s) for s in clean_subcats
            if s != "" and not s.lower().startswith("unnamed")
        ]

    if len(sublist) == 0:
        sublist = [(category, s) for s in clean_subcats]

    plotted = False

    for i, (cat, subc) in enumerate(sublist):

        data = df[(cat, subc)].dropna().values
        if len(data) < 2:
            continue

        color = colors[i % len(colors)]

        bins = np.arange(global_min, global_max + hist_bin_size, hist_bin_size)
        ax.hist(
            data,
            bins=bins,
            density=True,
            histtype='step',
            color=color,
            linewidth=1.2
        )

        xgrid = np.linspace(global_min, global_max, kde_points)
        kde_vals = kde_r(data, xgrid)

        if len(sublist) == 1:
            label_name = category
        else:
            label_name = subc if subc else category

        label = f"{label_name} (n={len(data)})"

        ax.plot(
            xgrid, kde_vals,
            color=color,
            linewidth=1.4,
            label=label
        )

        plotted = True

    ax.set_xlim(global_min, global_max)
    ax.set_ylabel("Density")

    ax.set_xticks(np.arange(global_min, global_max + 1, 500))
    ax.set_xticks(np.arange(global_min, global_max + 1, 100), minor=True)

  
    # LEGEND + CONDITIONAL CENTERED TITLE
 
    if plotted:
        leg = ax.legend(
            loc="upper right",
            bbox_to_anchor=(0.98, 0.88),
            fontsize=9,
            frameon=True
        )

        # Only add title if category has subcategories
        if len(sublist) > 1:
            fig.canvas.draw()

            bbox = leg.get_window_extent()
            bbox_axes = bbox.transformed(ax.transAxes.inverted())

            x_center = (bbox_axes.x0 + bbox_axes.x1) / 2
            y_top = bbox_axes.y1

            ax.text(
                x_center,
                y_top + 0.02,
                category,
                transform=ax.transAxes,
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold"
            )


axes[-1].set_xlabel("Age (Ma)")

plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("KDE saved:", output_path)