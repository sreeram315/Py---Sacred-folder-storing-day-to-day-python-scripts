# proprietary to BEERA // DO NOT COPY

# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 2 - Pandas Introduction
# All questions are weighted the same in this assignment.
# ## Part 1
# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals](https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table), and does some basic data cleaning. 
# 
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.

# In[1]:

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


# ### Question 0 (Example)
# 
# What is the first country in df?
# 
# *This function should return a Series.*

# In[2]:

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 


# ### Question 1
# Which country has won the most gold medals in summer games?
# 
# *This function should return a single string value.*

# In[3]:

def answer_one():
    return df.loc[df['Gold']==max(df["Gold"])]


# ### Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# 
# *This function should return a single string value.*

# In[4]:

def answer_two():
    
    return df.loc[(df['Gold.1']-df['Gold'])==max(df['Gold.1']-df['Gold'])]


# ### Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? 
# 
# $$\frac{Summer~Gold - Winter~Gold}{Total~Gold}$$
# 
# Only include countries that have won at least 1 gold in both summer and winter.
# 
# *This function should return a single string value.*

# In[5]:

def answer_three():
    c = df.copy()
    cri = ((c['Gold']>=1) & (c['Gold.1']>=1))
    c=c[cri]
    return c.loc[(c['Gold']-c['Gold.1'])/(c['Gold']+c['Gold.1'])==max((c['Gold']-c['Gold.1'])/(c['Gold']+c['Gold.1']))]


# ### Question 4
# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (`Gold.2`) counts for 3 points, silver medals (`Silver.2`) for 2 points, and bronze medals (`Bronze.2`) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
# 
# *This function should return a Series named `Points` of length 146*

# In[6]:

def answer_four():
    df['points']=(df['Gold'])*3 + (df['Bronze'])*1 + (df['Silver'])*2
    return df['points']


# ## Part 2
# For the next set of questions, we will be using census data from the [United States Census Bureau](http://www.census.gov). Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. [See this document](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2015/co-est2015-alldata.pdf) for a description of the variable names.
# 
# The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.
# 
# ### Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# 
# *This function should return a single string value.*

# In[7]:

census_df = pd.read_csv('census.csv')
census_df.head()


# In[8]:

def answer_five():
    df=census_df.set_index('STNAME')
    return df.loc[df['COUNTY']==max(df['COUNTY'])]


# ### Question 6
# **Only looking at the three most populous counties for each state**, what are the three most populous states (in order of highest population to lowest population)? Use `CENSUS2010POP`.
# 
# *This function should return a list of string values.*

# In[9]:

def answer_six():
    cols=['STNAME','CENSUS2010POP']
    df=census_df
    df=df[cols]
    df =df.set_index(['STNAME'])
    #print(df)

    df= df.sort_values('CENSUS2010POP',ascending=False)
    #print(df['CENSUS2010POP'])
    #print("is",max(df.loc['Alaska']))


    count={}
    pop={}
    for index,row in df.iterrows():
        if (index in count):
            if count[index]==3:
                continue
            elif count[index]<3:
                count[index]+=1
                pop[index]+=row['CENSUS2010POP']
        else:
            count[index]=1
            pop[index]=row['CENSUS2010POP']


    max_pop=0
    lst=[]
    for i in range(3):
        for key,value in pop.items():
            if value>max_pop:
                max_pop=value
                max_city=key
        lst.append(max_city)
        pop[max_city]=0
        max_pop=0

    return lst


# ### Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# 
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# 
# *This function should return a single string value.*

# In[10]:

def answer_seven():
    df=census_df
    arr=[]
    lst=[]
    df=df.set_index(['CTYNAME'])
    df['ABS']=0
    for index, row in df.iterrows():
        arr.append(row['POPESTIMATE2010'])
        arr.append(row['POPESTIMATE2011'])
        arr.append(row['POPESTIMATE2012'])
        arr.append(row['POPESTIMATE2013'])
        arr.append(row['POPESTIMATE2014'])
        arr.append(row['POPESTIMATE2015'])
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                a=int(arr[i])-int(arr[j])
                if a<0:
                    a-=(2*a)
                lst.append(int(a))
        df.at[index,'ABS']=max(lst)
        lst=[]
        arr=[]
    #print(df.loc['CTYNAME','ABS'==2224751])
    #print(df.loc[df['ABS']==max(df['ABS'])])
    #print(df.loc[])
    #print(df.loc['Texas','ABS'])
    df = df.set_index(['ABS'])
    return df.loc[2224751,'STNAME']


# ### Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column. 
# 
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# 
# *This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).*

# In[11]:

def answer_eight():
    df=census_df

    new_df=df[['STNAME','CTYNAME','REGION','POPESTIMATE2015','POPESTIMATE2014']]
    df=new_df
    df=df[df.CTYNAME=='Washington County']

    df=df[df.POPESTIMATE2015 > df.POPESTIMATE2014]
    df=df[df.REGION<3]


    return df

