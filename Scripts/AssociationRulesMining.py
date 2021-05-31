import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# desired_width = 320
#
# pd.set_option('display.width', desired_width)
#
# np.set_printoption(linewidth=desired_width)
#
# pd.set_option('display.max_columns', 10)

df = pd.read_csv('/Users/bessghaiernarjess/Documents/PhD_ETS/Contrib3-Configuration/NewClassification/FinalClassification/Coupling/RQ3CommitsCoupling.csv', sep=',',header=None, low_memory=False)
#print(df.head(50))
#print (pd.options.display.max_columns)
#items = (df.iloc[0].unique()) extesnions
items = (df.iloc[0].unique())
print(items)
itemset = set(items)
encoded_vals = []
for index, row in df.iterrows():
    rowset = set(row)
    labels = {}
    uncommons = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
encoded_vals[0]
ohe_df = pd.DataFrame(encoded_vals)
print(ohe_df)

#filesCoupling = suport=0.001 / conf=0.01, 0.1 and 0.2
freq_items = apriori(ohe_df, min_support=0.002, use_colnames=True, verbose=1)
print(freq_items.head(30))
rules = association_rules(freq_items, metric="confidence", min_threshold=0.1)
#print(rules.head(30))
print(rules.head(30).to_string())


####Supp/Conf
# plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
# plt.xlabel('support')
# plt.ylabel('confidence')
# plt.title('Support (>0.05) vs Confidence (>0.2)')
# plt.show()


####Supp/Lift

# plt.scatter(rules['support'], rules['lift'], alpha=0.5)
# plt.xlabel('support')
# plt.ylabel('lift')
# plt.title('Support vs Lift')
# plt.show()


####Lift/Conf

# fit = np.polyfit(rules['lift'], rules['confidence'], 1)
# fit_fn = np.poly1d(fit)
# plt.plot(rules['lift'], rules['confidence'], 'yo', rules['lift'],
# fit_fn(rules['lift']))
# plt.xlabel('lift')
# plt.ylabel('confidence')
# plt.title('Lift vs Confidence (>0.1)')
# plt.show()

