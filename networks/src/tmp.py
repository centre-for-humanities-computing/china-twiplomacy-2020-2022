import pandas as pd 

# load data
d_early = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean/early_clean.csv") 
d_late = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean/late_clean.csv")
d_full = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean/full_clean.csv")

# check new handles
focus_handles_early = [
    "zlj517", 
    "MFA_China",
    "SpokespersonCHN", 
    "XHNews",
    "Chinamission2un", 
    "CGTNOfficial",
    "ChinaDaily",
    "AmbLiuXiaoMing" 
]

focus_handles = [
    "zlj517", 
    "MFA_China",
    "SpokespersonCHN", 
    "XHNews",
    "CGTNOfficial",
    "ChinaDaily", 
    "xuejianosaka",
    "CGMeifangZhang" 
]

