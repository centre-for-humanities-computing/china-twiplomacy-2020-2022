import pandas as pd 
import re

# main data
d = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean/full_clean.csv")

# influencers
with open('/work/cn-some/china-twiplomacy-2020-2022/networks/data/reference/influencers.txt') as f:
    lines = f.readlines()

lines = [re.sub(r'\n', '', x) for x in lines]
d_influencers = pd.DataFrame({'mentioner': lines})

# join 
d_merged = d.merge(d_influencers, on = "mentioner", how = "inner")
len(d_merged)
len(list(d_merged["mentioner"].unique()))
len(d_influencers)

# make a basic plot 