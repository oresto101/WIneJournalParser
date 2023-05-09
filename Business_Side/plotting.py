import matplotlib.pyplot as plt


def get_pie_chart_by_country(counts_by_country: dict):
    labels = counts_by_country.keys()
    counts = counts_by_country.values()
    fig, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels)
    ax1.axis('equal')
    plt.savefig('plot.png')