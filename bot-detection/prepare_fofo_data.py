'''
VMP 2022-06-13: 
scoring of our data set 
'''

# packages
import pandas as pd 
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# load data 
inpath = "/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean"
d_raw = pd.read_csv(f"{inpath}/df_raw.csv")

# select cols 
d_sub = d_raw[["created_at", "followers_mentioner", "following_mentioner", "mentioner", "category"]]

# periods
total_start, total_end = "2019-11-01", "2022-04-30"
early_start, early_end = "2019-11-01", "2021-02-28"
late_start, late_end = "2021-03-01", "2022-04-30"

# filter dates
def filter_dates(df, start, end): 
    df_filtered = df[
        (df["created_at"] >= start) & 
        (df["created_at"] <= end)
    ]
    return df_filtered

df_total = filter_dates(d_sub, total_start, total_end) 
df_early = filter_dates(d_sub, early_start, early_end)
df_late = filter_dates(d_sub, late_start, late_end)

# other preprocessing 

## only last appearance 
df_total_last = df_total.sort_values("created_at", ascending=False).groupby("mentioner", as_index=False).first()
df_early_last = df_early.sort_values("created_at", ascending=False).groupby("mentioner", as_index=False).first()
df_late_last = df_late.sort_values("created_at", ascending=False).groupby("mentioner", as_index=False).first()

## drop duplicates
df_total_last = df_total_last.drop_duplicates()
df_early_last = df_early_last.drop_duplicates()
df_late_last = df_late_last.drop_duplicates()

## handle problematic cases
df_total_last = df_total_last[df_total_last["followers_mentioner"] != "retweeted"]
df_late_last = df_late_last[df_late_last["followers_mentioner"] != "retweeted"] 

## save 
outpath = "/work/cn-some/china-twiplomacy-2020-2022/bot-detection/curated_data"
df_total_last.to_csv(f"{outpath}/df_total.csv", index = False)
df_early_last.to_csv(f"{outpath}/df_early.csv", index = False)
df_late_last.to_csv(f"{outpath}/df_late.csv", index = False)
