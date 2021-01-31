import pandas as pd
data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

jj_counts = data["JJ"].value_counts()
magnet_counts = data["SCH_STATUS_MAGNET"].value_counts()
print("JJ Counts:",jj_counts)
print("Magnet Counts:", magnet_counts)

pivot_jj = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")

pivot_magnet = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index = "SCH_STATUS_MAGNET", aggfunc="sum")



print("JJ Pivot Table:", "\n", pivot_jj)
print("Magnet Pivot Table:", "\n", pivot_magnet)
