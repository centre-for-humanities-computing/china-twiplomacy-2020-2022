import pandas as pd 
import networkx as nx

concat = pd.read_csv("/work/cn-some/china-twiplomacy-2020-2022/networks/data/clean/early_clean.csv")

concat = concat[concat["mentionee"] != concat['mentioner']] # remove self-mentions
concat_sub = concat[(concat["category"] == "Media") | (concat['category'] == 'Diplomat')] # only cited by media or diplomat

weighted_mention = concat_sub.groupby(['mentionee', 'mentioner', 'category', 'category_mentionee']).size().to_frame('weight').reset_index() # weighted
G = nx.from_pandas_edgelist(weighted_mention,source='mentioner',target='mentionee', edge_attr='weight', create_using=nx.DiGraph()) # create network

len(G.nodes())

concat_mentionee = list(concat["mentionee"].unique())
network_handles = list(G.nodes.keys())
mentionee_not_network = list(set(concat_mentionee) - set(network_handles)) # mentionee, but not in network (i.e. not mentioned by any diplomat/media)
network_not_mentionee = list(set(network_handles) - set(concat_mentionee))
mentionee_not_network 
network_not_mentionee # these five are the problem 

concat[concat["mentionee"] == "Cao_Li_CHN"]

''' 3. create and set node attributes '''
# mentions for color 
mentioners = weighted_mention[["mentioner", "category"]].drop_duplicates().rename(columns = {'mentioner': 'node'})
mentionees = weighted_mention[["mentionee", "category_mentionee"]].drop_duplicates().rename(columns = {'mentionee': 'node', 'category_mentionee': 'category'})
mentions_category = pd.concat([mentioners, mentionees])
mentions_category = mentions_category.drop_duplicates()
mentions_category = dict(zip(mentions_category.node, mentions_category.category))
nx.set_node_attributes(G, mentions_category, "category")

# size: based on mentions in total dataset
G_nodes = list(G.nodes())
size_frame = concat.groupby('mentionee').size().to_frame('mentions').reset_index()
mentionee_size = size_frame[size_frame["mentionee"].isin(G_nodes)]

lst = []
len(lst)

if len(network_not_mentionee) > 0: 
    not_mentioned = pd.DataFrame({
        'mentionee': network_not_mentionee,
        'mentions': 0
    })
    mentionee_size = pd.concat([mentionee_size, not_mentioned])

mentionee_size_dct = dict(zip(mentionee_size.mentionee, mentionee_size.mentions))
nx.set_node_attributes(G, mentionee_size_dct, "mentions")

# size based on various kinds of degree 
def degree_information(G, method, metric):
    '''
    G: <networkx.classes.digraph.DiGraph
    method: G.degree() or variants 
    metric: <str> e.g. "weighted_degree" 
    '''

    degree = {node:val for (node, val) in method}
    nx.set_node_attributes(G, degree, metric)

degree_information(G, G.degree(weight=None), "unweighted_degree")
print(G.nodes(data=True))
degree_information(G, G.degree(weight='weight'), "weighted_degree")
degree_information(G, G.in_degree(weight='weight'), "in_degree")
degree_information(G, G.out_degree(weight='weight'), "out_degree")

def sort_dictionary(d, sort_val): 
    '''
    d: <dict> 
    sort_val: <str>
    '''
    d_sort = dict(sorted(d.items(), key = lambda x: x[1][sort_val], reverse=True))
    return d_sort

dct_node = dict(G.nodes(data=True))

dct_node # ChinainVan, ChinaCG_HH, Li_Yang_China, CGMeifangZhang, Cao_Li_CHN


dct_mention = sort_dictionary(dct_node, 'mentions')