# china-twiplomacy-2020-2022

### Tables

#### Table 6: Foreign influencers mentioning Chinese diplomats and media
| @handle           | User                              |
| ----------------- | --------------------------------- |
| @AndyBxxx         | Andy Boreham (Reports On China)   |
| @BarrettYouTube   | Lee and Oli Barrett               |
| @BeehiveChina     | Barrie Jones (Best China Info)    |
| @ChinaTeacher1    | Fernando Munoz Bernal (FerMuBe)   |
| @DanielDumbrill   | Daniel Dumbrill                   |
| @JaYoeLife        | Matthew Galat                     |  
| @Jingjing_Li      | Li Jingjing                       |
| @LivingChina      | Jason Lightfoot (Living in China) |
| @Noel_Calibre     | Noel Lee                          |
| @thecyrusjanssen  | Cyrus Janssen                     |

Influencers identified by ASPI: https://www.aspi.org.au/report/borrowing-mouths-speak-xinjiang

### Figures 

#### Figure 1a: Top mentionees (in-degree) and mentioners (out-degree) - full period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/stats_full/summary_focus_degree.png)

#### Figure 1b: Top mentionees (in-degree) and mentioners (out-degree) - early period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/stats_early/summary_focus_degree.png)

#### Figure 1c: Top mentionees (in-degree) and mentioners (out-degree) - late period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/stats_late/summary_focus_degree.png)

#### Figure 2a: Total mentions to handles in network from all Twitter users - full period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_full/network_focus_mentions_seed11_k1.8.png)

#### Figure 2b: Total mentions to handles in network from all Twitter users - early period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_early/network_focus_mentions_seed11_k1.8.png)

#### Figure 2c: Total mentions to handles in network from all Twitter users - late period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_late/network_focus_mentions_seed11_k1.8.png)

#### Figure 3a: Total mentions between handles in network - full period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_full/network_focus_weighted_degree_seed11_k1.8.png)

#### Figure 3b: Total mentions between handles in network - early period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_early/network_focus_weighted_degree_seed11_k1.8.png)

#### Figure 3c: Total mentions between handles in network - late period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_late/network_focus_weighted_degree_seed11_k1.8.png)

#### Figure 4a: Mentionees in network (in-degree) - full period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_full/network_focus_in_degree_seed11_k1.8.png)

#### Figure 4b: Mentionees in network (in-degree) - early period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_early/network_focus_in_degree_seed11_k1.8.png)

#### Figure 4c: Mentionees in network (in-degree) - late period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_late/network_focus_in_degree_seed11_k1.8.png)

#### Figure 5a: Mentioners in network (out-degree) - full period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_full/network_focus_out_degree_seed11_k1.8.png)

#### Figure 5b: Mentioners in network (out-degree) - early period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_early/network_focus_out_degree_seed11_k1.8.png)

#### Figure 5c: Mentioners in network (out-degree) - late period
![alt text](https://github.com/centre-for-humanities-computing/china-twiplomacy-2020-2022/blob/main/networks/fig/network_late/network_focus_out_degree_seed11_k1.8.png)

## Network Analysis (NB: needs modification)
Network analysis performed using the networkx package in python (https://networkx.org/) and the network visualizations are generated from the file ```network_main.py``` (see usage below). 
Nodes in the networks are Twitter handles, and edges (connections) are weighted by the number of mentions between the Twitter handles that are displayed. 
The network visualizations only plot Twitter handles that are either flagged as (i) Chinese diplomats or (ii) Chinese media outlets. 
The *edgewidth* (strength of connections) is determined by the number of mentions between Twitter handles of Chinese diplomats and media outlets (see below). 
The *nodesize* (size of handle) is determined by various attributes, such as: 
* *total mentions* (**Figure 2**): number of total mentions to the Twitter handle in question from all users (also non-diplomats and non-media that are not shown as nodes in the plot). This shows how "popular" the Chinese diplomats and media outlets are on Twitter broadly, rather than just their popularity/activity within the diplomat/media sub-network. 
* *weighted degree* (**Figure 3**): node-size scaled by number of total number of connections between Twitter handle in question and other Chinese diplomats and media outlets (both directions counted, and each mention counted). The weighted degree plot corresponds to *in-degree* + *out-degree* (i.e. we count both directions). 
* *in-degree* (**Figure 4**): number of mentions from other Chinese diplomats and media outlets to the Twitter handle in question (only one direction counted). 
* *out-degree* (**Figure 5**): number of mentions from the Twitter handle in question to other Chinese diplomats and media outlets (only one direction counted). 

In addition to the network visualizations, we also show the top 10 handles (based on *weighted degree*) in **Figure 1**. The plot is generated in ```summary_stats_focus.py``` (see usage below). Clearly, some handles are primarily mentionees and have high *in-degree* (e.g. CHNews) while others are primarily mentioners and have high *out-degree* (e.g. zlj517) within the diplomat/media sub-network. 

### Usage:
1. Activate environment

```
source cnenv/bin/activate
```

2. Navigate to the network code folder
```
cd networks/src
```

3. Run bash script

```
bash main.sh
```

in ```main.sh``` set: <br/>
PRE=true <br/>
NET=true <br/>
SUM=true <br/>

This ensures that the bash script calls (runs) 
1. preprocessing (```concat_files.py```)
2. network visualizations (```network_main.py```) 
3. summary data analysis (```summary_stats_focus.py```)

## Bot Detection
We train a logistic classifier on the cresci-2017 (Cresci et al., 2017) data set (available: https://botometer.osome.iu.edu/bot-repository/datasets.html) to classify Twitter handles as genuine or spam/bot/fake. We use the widely used fofo metric (e.g. Yang et al., 2013; Tavazoee et al., 2020) which is (following/followers) of an account. We use (following+1/followers+1) to avoid division with zero, and when an account appears more than once in a data set we use only the last appearance (i.e. the number of following and followers for the handle at that time). The intuition behind the metric is that bot-accounts tend to follow many other accounts (following) but they tend to have few followers. This means that they will generally have a high fofo-ratio (i.e. high following, low followers). Using the trained model, we estimate the fraction of genuine accounts vs. spam/bot/fake accounts in our own data set, as well as in a baseline data set consisting of vaccine-related tweets from 2020-2021 (https://www.kaggle.com/datasets/gpreda/all-covid19-vaccines-tweets). We estimate 27.22% of the accounts in the baseline (vaccine) data set to be non-genuine accounts and 44.84% of accounts in our data set of Chinese state media and diplomats to be non-genuine accounts. There is considerable uncertainty around this estimate since (1) our data set might differ in other respects than the amount of bot-activity from the baseline data set and (2) while the fofo-metric is widely used (Yang et al., 2013) it is not universally found to be accurate in detecting bots. 