'''
VMP 2022-06-13: scoring

'''

import pandas as pd 
import pickle
from sklearn.linear_model import LogisticRegression

# loads (our data)
dat_full = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/bot-detection/curated_data/df_total.csv")
dat_early = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/bot-detection/curated_data/df_early.csv")
dat_late = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/bot-detection/curated_data/df_late.csv")

## loads (baseline)
dat_vacc = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/bot-detection/baseline_data/vaccination_all_tweets.csv")
dat_vacc = dat_vacc[["user_name", "user_followers", "user_friends", "date"]].rename(
    columns = {
        'user_name': 'mentioner',
        'user_followers': 'followers_mentioner',
        'user_friends': 'following_mentioner',
        'date': 'created_at'
    }
)

# only based on last tweet from mentioner
dat_vacc = dat_vacc.sort_values("created_at", ascending=False).groupby("mentioner", as_index=False).first()

## load model 
filename = "/work/cn-some/china-twiplomacy-2020-2022/bot-detection/mdl/bot_detect_mdl.sav"
clf = pickle.load(open(filename, 'rb'))

## get overall stuff (NB: 0 = human, 1 = bot)
def score_record(d, clf):
    # prepare prediction
    d["followers_mentioner"] = d['followers_mentioner'].astype(str).astype(float)
    d["following_mentioner"] = d['following_mentioner'].astype(str).astype(float)
    d = d.assign(fofo = lambda x: (x['following_mentioner']+1)/(x['followers_mentioner']+1))
    fofo = d['fofo'].values
    account = d['mentioner'].values
    fofo_shaped = fofo.reshape(-1, 1)

    # predict stuff 
    y_pred = clf.predict(fofo_shaped)
    y_val = clf.predict_proba(fofo_shaped)

    # create dataframe
    d_probability = pd.DataFrame(y_val, columns = ['proba_human', 'proba_bot'])
    d_prediction = pd.DataFrame(y_pred, columns = ['prediction'])
    d_handle = pd.DataFrame(account, columns = ['handle'])
    d_foforatio = pd.DataFrame(fofo, columns = ['fofo_ratio'])
    d_total = pd.concat([d_probability, d_prediction, d_handle, d_foforatio], axis=1)

    return d_total

# use the function
d_full = score_record(dat_full, clf)
d_early = score_record(dat_early, clf)
d_late = score_record(dat_late, clf)
d_vacc = score_record(dat_vacc, clf)

# write stuff
outpath = "/work/cn-some/china-twiplomacy-2020-2022/bot-detection/res"
d_full.to_csv(f"{outpath}/results_full_period.csv", index = False)
d_early.to_csv(f"{outpath}/results_early_period.csv", index = False)
d_late.to_csv(f"{outpath}/results_late_period.csv", index = False)
d_vacc.to_csv(f"{outpath}/results_vaccine_baseline.csv", index = False)