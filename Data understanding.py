#%% read csv
import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from seaborn.utils import axlabel

df = pd.read_csv("2012.csv")
df.head()


# %% show stats
df.describe(include="all").to_csv("stats.csv")

# %% make sure number columns only contain numbers if
# a value can't be converted into number make it NaN
from tqdm import tqdm

cols = [
    "perobs",
    "perstop",
    "age",
    "weight",
    "ht_feet",
    "ht_inch",
    "datestop",
    "timestop",
    "xcoord",
    "ycoord",
]
for col in tqdm(cols, desc="convert to number"):
    df[col] = pd.to_numeric(df[col], errors="coerce")

#%%drop all rows with invalid numeric value
df = df.dropna()

# %% make datetime column
df["datestop"] = df["datestop"].astype(str).str.zfill(8)
df["timestop"] = df["timestop"].astype(str).str.zfill(4)
print(df["datestop"])
print(df["timestop"])

#%%
from datetime import datetime


def make_datetime(datestop, timestop):
    year = int(datestop[-4:])
    month = int(datestop[:2])
    day = int(datestop[2:4])

    hour = int(timestop[:2])
    minute = int(timestop[2:])

    return datetime(year, month, day, hour, minute)


df["datetime"] = df.apply(
    lambda row: make_datetime(row["datestop"], row["timestop"]), axis=1
)
print(df["datetime"])

# %% make height column
df["height"] = (df["ht_feet"] * 12 + df["ht_inch"]) * 2.54
print(df["height"])


# %% make lat/lon columns
import pyproj

srs = (
    "+proj=lcc +lat_1=41.03333333333333 "
    "+lat_2=40.66666666666666 +lat_0=40.16666666666666 +lon_0=-74 "
    "+x_0=300000.0000000001 +y_0=0 "
    "+ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs"
)

p = pyproj.Proj(srs)

coords = df.apply(lambda r: p(r["xcoord"], r["ycoord"], inverse=True), axis=1)
df["lat"] = [c[1] for c in coords]
df["lon"] = [c[0] for c in coords]


# %% read the spec file and replace values in df with the matching labels
import numpy as np

value_labels = pd.read_excel(
    "2012 SQF File Spec.xlsx", sheet_name="Value Labels", skiprows=range(4)
)
value_labels["Field Name"] = value_labels["Field Name"].fillna(method="ffill")
value_labels["Field Name"] = value_labels["Field Name"].str.lower()
value_labels["Value"] = value_labels["Value"].fillna(" ")
vl_mapping = value_labels.groupby("Field Name").apply(
    lambda x: dict([(row["Value"], row["Label"]) for row in x.to_dict("records")])
)

cols = [col for col in df.columns if col in vl_mapping]

for col in tqdm(cols):
    df[col] = df[col].apply(lambda val: vl_mapping[col].get(val, np.nan))


# %% plot height
import seaborn as sns

sns.distplot(df["height"])

# %%
sns.distplot(df["weight"])

# %% remove rows with invalid age/weight
df = df[(df["age"] <= 100) & (df["age"] >= 10)]
df = df[(df["weight"] <= 350) & (df["weight"] >= 50)]

# %% plot month
sns.countplot(df["datetime"].dt.month)


# %% plot day of week
ax = sns.countplot(df["datetime"].dt.weekday)
ax.set_xticklabels(["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"])
ax.set(xlabel="day of week", title="# of incidents by day of weeks")
ax.get_figure().savefig("test.png")

# %% export stats to excel
df.describe(include="all").to_excel("stats.xlsx")


# %% plot hour

ax = sns.countplot(df["datetime"].dt.hour)
ax.get_figure().savefig("break-down-by-hour.png")

# %% plot xcoord / ycoord
sns.scatterplot(data=df[:100], x="xcoord", y="ycoord")


# %%
import folium

m = folium.Map((40.7128, -74.0060))
m


# %% plot lat / lon of murder cases on an actual map
import folium

m = folium.Map((40.7128, -74.0060))

for r in df[["lat", "lon"]][df["detailcm"] == "MURDER"].to_dict("records"):
    folium.CircleMarker(location=(r["40.692528"], r["-73.991"]), radius=1).add_to(m)

m
#%%
import folium

m = folium.Map((40.7128, -74.0060))

for r in df[["lat", "lon"]][df["race"] == "BLACK"][df["city"]=="BROOKLYN"].to_dict("records"):
    folium.CircleMarker(location=(r["lat"], r["lon"]), radius=1).add_to(m)

m

# %% plot lat / lon of terrorism cases on an actual map

m = folium.Map((40.7128, -74.0060))

for r in df[["lat", "lon"]][df["detailcm"] == "TERRORISM"].to_dict("records"):
    folium.CircleMarker(location=(r["lat"], r["lon"]), radius=1).add_to(m)

m

# %% plot race
##sns.countplot(data=df, y="race")
##print(df["race"])
##race1 = df["race"].value_counts()
##a = df["race"].unique()
##print(race1)
##percent = df["race"].value_counts(normalize=True)
##percent100 = df["race"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%"
##print(percent100)
##percent
#%%
# import matplotlib.pyplot as plt

# plt.pie(percent, labels=a, autopct="%1.1f%%")


# %% plot race wrt city
sns.countplot(data=df, y="race", hue="sex")
#%%
sns.countplot(df["arstmade"])


# %% plot top crimes where physical forces used
pf_used = df[
    (df["pf_hands"] == "YES")
    | (df["pf_wall"] == "YES")
    | (df["pf_grnd"] == "YES")
    | (df["pf_drwep"] == "YES")
    | (df["pf_ptwep"] == "YES")
    | (df["pf_baton"] == "YES")
    | (df["pf_hcuff"] == "YES")
    | (df["pf_pepsp"] == "YES")
    | (df["pf_other"] == "YES")
]

sns.countplot(
    data=pf_used,
    y="detailcm",
    order=pf_used["detailcm"].value_counts(ascending=False).keys()[:10],
)


# %% plot percentage of each physical forces used
pfs = [col for col in df.columns if col.startswith("pf_")]
pf_counts = (df[pfs] == "YES").sum()
sns.barplot(y=pf_counts.index, x=pf_counts.values / df.shape[0])


# %% drop columns that are not used in analysis
df = df.drop(
    columns=[
        # processed columns
        "datestop",
        "timestop",
        "ht_feet",
        "ht_inch",
        "xcoord",
        "ycoord",
        # not useful
        "year",
        "recstat",
        "crimsusp",
        "dob",
        "ser_num",
        "arstoffn",
        "sumoffen",
        "compyear",
        "comppct",
        "othfeatr",
        "adtlrept",
        "dettypcm",
        "linecm",
        "repcmd",
        "revcmd",
        # location of stop
        # only use coord and city
        "addrtyp",
        "rescode",
        "premtype",
        "premname",
        "addrnum",
        "stname",
        "stinter",
        "crossst",
        "aptnum",
        "state",
        "zip",
        "addrpct",
        "sector",
        "beat",
        "post",
    ]
)

# %% modify one column
df["trhsloc"] = df["trhsloc"].fillna("NEITHER")
print(df["trhsloc"])
# %% remove all rows with NaN
df = df.dropna()

# %%
top10_pct = df["pct"].value_counts()[:10]
sns.scatterplot(
    data=df[df["pct"].isin(top10_pct.index)], x="perobs", y="race", hue="pct"
)

plt.title("Period of Observation, by Race and Precinct")


# %% save dataframe to a file
df.to_pickle("data.pkl")

# %%average age of people
import statistics
import matplotlib.pyplot as plt

# average_age = statistics.mean(df["age"])
# print(average_age)
sns.histplot(df["age"])


# %%calculate number of men and women stopped in SQF
df["sex"].value_counts()

# %%height
average_height = statistics.mean(df["height"])
print(average_height)

# %%Reason for stop clothing,CARRYING SUSPICIOUS OBJECT,FITS A RELEVANT DESCRIPTION,
##CASING A VICTIM OR LOCATION,SUSPECT ACTING AS A LOOKOUT,ACTIONS INDICATIVE OF A DRUG TRANSACTION,
##FURTIVE MOVEMENTS,ACTIONS OF ENGAGING IN A VIOLENT CRIME,SUSPICIOUS BULGE
##OTHER
df["cs_cloth"].value_counts()
#%%
df["cs_objcs"].value_counts()
#%%
df["cs_casng"].value_counts()
#%%
df["cs_casng"].value_counts()
#%%
df["cs_lkout"].value_counts()
#%%
df["cs_drgtr"].value_counts()
#%%
df["cs_furtv"].value_counts()
#%%
df["cs_vcrim"].value_counts()
#%%
df["cs_bulge"].value_counts()
#%%
df["cs_other"].value_counts()


# %%
sns.countplot(df["sex"])

# %%

# %%relationship between
pf_stops = df
[
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
]
sns.countplot(pf_stops)
##print(pf_stops)
##sns.(pf_stops)
##sns.countplot(
##  data=pf_stops,
## y="arstmade",
##order=pf_stops["arstmade"].value_counts(ascending=False).keys()[:10],
##)
#%%
df.groupby("sex").age.hist()

# %%
df.groupby("sex")
# %%
pf_weapon = [
    (df["pistol"] == "YES")
    | (df["riflshot"] == "YES")
    | (df["asltweap"] == "YES")
    | (df["knifcuti"] == "YES")
    | (df["machgun"] == "YES")
    | (df["othrweap"] == "YES")
]
sns.countplot(
    data=pf_weapon,
    y="detailcm",
    order=pf_weapon["detailcm"].value_counts(ascending=False).keys()[:10],
)
# %%
df.groupby("arstmade").race.hist()


# %%
pf_used = df[
    (df["pf_hands"] == "YES")
    | (df["pf_wall"] == "YES")
    | (df["pf_grnd"] == "YES")
    | (df["pf_drwep"] == "YES")
    | (df["pf_ptwep"] == "YES")
    | (df["pf_baton"] == "YES")
    | (df["pf_hcuff"] == "YES")
    | (df["pf_pepsp"] == "YES")
    | (df["pf_other"] == "YES")
]
pf_stops = df
[
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
]
pf_frisk = df
[
    (df["rf_attir"] == "YES")
    | (df["rf_vcact"] == "YES")
    | (df["rf_rfcmp"] == "YES")
    | (df["rf_knowl"] == "YES")
    | (df["rf_verbl"] == "YES")
    | (df["rf_furt"] == "YES")
    | (df["rf_bulg"] == "YES")
]
pf_reason = df["pf_stops"] == "YES"
(df["pf_frisk"] == "YES")

# %%

import seaborn as sns

sns.countplot(
    data=pf_stops,
    y=pf_used,
    order=pf_stops[pf_used].value_counts(ascending=False).keys()[:10],
)
# %%
sns.scatterplot()
