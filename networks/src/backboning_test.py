# imports 
import backboning # michele backboning module 
import networkx as nx 
import pandas as pd 
import time
import numpy as np
import argparse 
import random
from community import community_louvain
import pickle 

# get records 
concat = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean/early_clean.csv")
concat = concat[concat["mentionee"] != concat['mentioner']] # remove self-mentions
concat_sub = concat[(concat["category"] == "Media") | (concat['category'] == 'Diplomat')] # only cited by media or diplomat
weighted_mention = concat_sub.groupby(['mentionee', 'mentioner', 'category', 'category_mentionee']).size().to_frame('weight').reset_index()




## below goes from directed to undirected: 
lesser = weighted_mention[weighted_mention['mentionee'] > weighted_mention['mentioner']]
greater = weighted_mention[weighted_mention['mentionee'] < weighted_mention['mentioner']]
greater = greater.rename(columns = {
    'mentionee': 'mentioner',
    'mentioner': 'mentionee',
    'category': 'category_mentionee',
    'category_mentionee': 'category'})
total = pd.concat([lesser, greater])
weighted_mention = total.groupby(['mentionee', 'mentioner', 'category', 'category_mentionee'])['weight'].sum().to_frame('weight').reset_index()
weighted_mention = weighted_mention[weighted_mention["weight"] > x]

G = nx.from_pandas_edgelist(weighted_mention,source='mentioner',target='mentionee', edge_attr='weight', create_using=nx.DiGraph()) # create network

## naive backboning 
def degree_information(G, method, metric):
    '''
    G: <networkx.classes.digraph.DiGraph
    method: G.degree() or variants 
    metric: <str> e.g. "weighted_degree" 
    '''

    degree = {node:val for (node, val) in method}
    nx.set_node_attributes(G, degree, metric)

degree_information(G, G.degree(weight='weight'), "weighted_degree")

## find the nodes that we keep in the end: 

G.subgraph([0, 1, 2])




# clean up
df_renamed = weighted_mention.rename(columns = {
    'mentionee': 'src',
    'mentioner': 'trg',
    'weight': 'nij'
})

## backboning disparity filter (DF)
df_threshold = 0.95
table_df = backboning.disparity_filter(df_renamed, undirected = False)
bb_df = backboning.thresholding(table_df, df_threshold) 

##### log information #####
print(f"number of edges: {len(bb_df)}")
print(f"number of in-degree: {len(bb_df['trg'].unique())}")

## convert back 
bb_df_renamed = bb_df.rename(columns = {
    'src': 'mentionee',
    'trg': 'mentioner',
    'nij': 'weight'
})


weighted_mention = bb_df_renamed.merge(weighted_mention, on = ['mentionee', 'mentioner', 'weight'], how = 'inner')
weighted_mention.head(5)


nodelst = ['Amb_ChenXu', 'AmbcuiTiankai']
dct = {'ChinaEUMission': {'category': 'x', 'weighted_degree': '506'}, 'Amb_ChenXu': {'test'}}
dct_pruned = filtered_dict = {key: value for key, value in dct.items() if key in nodelst}
dct_pruned


above_threshold = weighted_mention[weighted_mention['weight'] > 500]
above_threshold


def edgelist_to_authors(d, from_col, to_col):
    df_src_authors = d[[from_col]]
    df_trg_authors = d[[to_col]].rename(columns = {to_col: from_col})
    df_concat_authors = pd.concat([df_src_authors, df_trg_authors])
    df_authors_edgelist = df_concat_authors.drop_duplicates()
    authorlst = list(df_authors_edgelist["mentionee"])
    return authorlst

tst = edgelist_to_authors(above_threshold, "mentionee", "mentioner")
tst

above_threshold

## sanity check
weighted_mention
zlj_in = weighted_mention[weighted_mention['mentionee'] == 'zlj517']
zlj_in['weight'].sum()

zlj_out = weighted_mention[weighted_mention['mentioner'] == 'zlj517']
zlj_out['weight'].sum()