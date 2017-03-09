import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr

# load data
train = pd.read_csv("../../description/1/train.csv", header=None, names=['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
train.head()

# plot
for i in range(1,7):
    gi = train['G'+str(i)]
    g7 = train['G7']
    plt.plot(gi, g7, 'bo')
    plt.ylabel("G7")
    plt.xlabel("G"+str(i))
    # Calculates a Pearson correlation coefficient and the p-value for testing non-correlation
    print(pearsonr(gi, g7))
    plt.show()

