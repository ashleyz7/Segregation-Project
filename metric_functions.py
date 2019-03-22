#!/usr/bin/env python
# coding: utf-8

# In[10]:





# In[1]:


def dissimilarity (all_city):
    """calculate the dissimilarity index of all the cities
    """
    diss_index = []
    for i in list(all_city.groupby('city').groups.keys()):
        p = all_city[all_city.city == i].pop_not_white.sum()/all_city[all_city.city == i].total_pop.sum()
        addition = sum(all_city[all_city.city == i].total_pop * abs(all_city[all_city.city == i].pct_not_white - p))
        result = addition/(2 * all_city[all_city.city == i].total_pop.sum() * p * (1 - p))
        diss_index.append(result)
    return diss_index

def interaction (all_city):
    """calculate the interaction index of certain place
    """
    inter_index = []
    for i in list(all_city.groupby('city').groups.keys()):
        x = all_city[all_city.city == i].pop_not_white.sum()
        result = sum((all_city[all_city.city == i].pop_not_white/x) * (all_city[all_city.city == i].pop_white/all_city[all_city.city == i].total_pop))
        inter_index.append(result)
    return inter_index

def isolation (all_city):
    """calculate the isolation index of certain place
    """
    iso_index = []
    for i in list(all_city.groupby('city').groups.keys()):
        x = all_city[all_city.city == i].pop_not_white.sum()
        result = sum((all_city[all_city.city == i].pop_not_white/x) * (all_city[all_city.city == i].pop_not_white/all_city[all_city.city == i].total_pop))
        iso_index.append(result)
    return iso_index

def newSeg (all_city):
    """calculate a new segregation index that combines isolation and dissimilarity of certain place
    """
    this_index = []
    for i in list(all_city.groupby('city').groups.keys()):
        x = all_city[all_city.city == i].pop_not_white.sum()
        result_first = sum((all_city[all_city.city == i].pop_not_white/x) * (all_city[all_city.city == i].pop_not_white/all_city[all_city.city == i].total_pop))
        result_second = sum((all_city[all_city.city == i].pop_not_white/x) * (all_city[all_city.city == i].pop_not_white/all_city[all_city.city == i].total_pop))
        result = result_first + result_second
        this_index.append(result)
    return this_index


# In[ ]:




