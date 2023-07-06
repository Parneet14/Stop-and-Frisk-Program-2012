# %% read dataframe
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


df = pd.read_pickle("data.pkl")


# %% convert physical forces used columns to booleans
pfs = [col for col in df.columns if col.startswith("pf_")]
for col in pfs:
    df[col] = df[col] == "YES"


# %% manual one hot encoding for race / city
for val in df["race"].unique():
    df[f"race_{val}"] = df["race"] == val

for val in df["city"].unique():
    df[f"city_{val}"] = df["city"] == val
    for val in df["detailcm"].unique():
        df[f"detailcm_{val}"] = df["detailcm"] == val

# %% convert inout to boolean
df["Male"] = df["sex"] == "MALE"


# %% create armed column
##df["armed"] = (
##    (df["contrabn"] == "YES")
##    | (df["pistol"] == "YES")
##    | (df["riflshot"] == "YES")
##    | (df["asltweap"] == "YES")
##| (df["knifcuti"] == "YES")
##  | (df["machgun"] == "YES")
##   | (df["othrweap"] == "YES")
# )
df["Reason"] = (
    (df["cs_other"] == "YES")
    | (df["cs_bulge"] == "YES")
    | (df["cs_vcrim"] == "YES")
    | (df["cs_furtv"] == "YES")
    | (df["cs_drgtr"] == "YES")
    | (df["cs_lkout"] == "YES")
    | (df["cs_lkout"] == "YES")
    | (df["cs_casng"] == "YES")
    | (df["cs_objcs"] == "YES")
    | (df["cs_cloth"] == "YES")
)

# %% select columns for association rules mining
cols = [
    col
    for col in df.columns
    if col.startswith("detailcm_") or col.startswith("race_") or col.startswith("city_")
] + ["Male", "Reason"]

# %% apply frequent itemset mining
frequent_itemsets = apriori(df[cols], min_support=0.10, use_colnames=True)
frequent_itemsets
frequent_itemsets.to_csv("frequent_itemsets.csv")
#%%
# %%
import sklearn.datasets as datasets
from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# check for the sklearn version, it has to be 0.21
import sklearn
print(sklearn.__version__)
#%%
breast_cancer = pd.read_csv('rules.csv')
#%%
clf = DecisionTreeClassifier()
clf.fit(breast_cancer.confidence
, breast_cancer.support
)
pred_train = clf.predict(breast_cancer.confidence)
pred_test = clf.predict(breast_cancer.support)
#%%
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

enc = OneHotEncoder(handle_unknown="ignore")
ct = ColumnTransformer(
    [
        ("ohe", enc, breast_cancer.antecedents,breast_cancer.consequents

),
    ],
    remainder="passthrough",
)

x_train = ct.fit_transform(breast_cancer.confidence)
x_test = ct.transform( breast_cancer.support)
from sklearn.tree import plot_tree

plot_tree(clf, filled=True, max_depth=6, feature_names=ct.get_feature_names())
# %% apply association rules mining
rules = association_rules(frequent_itemsets, min_threshold=0.8)
rules

# %% sort rules by confidence
rules.sort_values("confidence", ascending=False)
rules.to_csv("rules.csv")
#%%
rules.sort_values("support", ascending=False).head(10)
# %%
import matplotlib.pyplot as plt

plt.scatter(rules["support"], rules["confidence"], alpha=0.5)
plt.xlabel("support")
plt.ylabel("confidence")
plt.title("Support vs Confidence")
plt.show()
#%%plt.scatter(rules[‘support’], rules[‘lift’], alpha=0.5)
plt.xlabel("support")
plt.ylabel("lift")
plt.title("Support vs Lift")
plt.show()
#%%fit = np.polyfit(rules[‘lift’], rules[‘confidence’], 1)
import numpy as np

fit = np.polyfit(rules["lift"], rules["confidence"], 1)
fit_fn = np.poly1d(fit)

plt.plot(rules["lift"], rules["confidence"]), "yo", rules["lift"], fit_fn(rules["lift"]))

# %%
