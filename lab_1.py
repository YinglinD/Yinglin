# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pandas as pd

nyc = pd.read_csv('ny.csv',index_col=False)

nyc.head(2)
nyc.shape
nyc.columns
nyc.dtypes

nyc['cand_nm']
nyc['cand_nm'].value_counts()
nyc['cand_nm'].value_counts(normalize=True)
nyc['cand_nm'].isnull().value_counts()

nyc.contbr_employer.isnull().value_counts()

s=pd.Series([.25 ,.5 ,.75 ,1])
s.values
#array([0.25, 0.5 , 0.75, 1.  ])
s.index

s[0:2]
#0    0.25
#1    0.50
#dtype: float64
s[1:3]
s1 =pd.Series( [.25 ,.5 ,.75 ,1], index = ['a','b','c','d'] )
s2 =pd.Series( [.5 ,.75 ,.1 ,1.25],index = ['a','b','c','d'])
df = pd.DataFrame({'s1':s1,'s2':s2})
s3 =pd.Series( [.5 ,.75 ,.1 ,1.25],index = ['b','c','d','e'])
df2 = pd.DataFrame({'s1':s1,'s3':s3})

price = pd.Series({'cherry':2,'berry':1,'orange':3,'apple':4})
qty = pd.Series({'cherry':12,'berry':7,'orange':8,'apple':31})
fruit = pd.DataFrame({'price':price,'qty':qty})
fruit
fruit['price']
fruit.price
fruit[1:3]
fruit[1:3,0] #will be error
fruit[1:3]['price']
fruit.iloc[1:3]
fruit.iloc[1:3]['price']
fruit.iloc[1:3,0]
fruit.iloc[2]
#price    3
#qty      8
#Name: orange, dtype: int64

fruit.iloc[1:3,'price'] #will be error
fruit.loc['cherry':'orange']
waj = pd.DataFrame({'x':[1,2,3],'y':[4,5,6]})
waj.iloc[0:2]
waj.loc[0:2]
fruit.loc['cherry':'orange','price']
fruit.loc['cherry':'orange',0] #will be an error

nyc2 = nyc.iloc[0]
cndu=nyc['cand_nm'].unique()
nycdf = pd.DataFrame({'cand_nm':cndu})

nycdf.loc[0,'party']='Democrat'
nycdf.loc[1,'party']='Democrat'
nycdf
nycdf.loc[[0,1,3,13,22],'party']='Democrat'
nycdf.loc[10,'party']='Green'
nycdf.loc[11,'party']='Libertarian'
nycdf.loc[24,'party']='Independent'
nycdf.loc[nycdf['party'].isnull(),'party']='Republican'
nycdf

##############  second way according slides ########
nycdf2=nyc['cand_nm'].value_counts()
type(nycdf2)

nycdf2 = nycdf2.reset_index()
del nycdf2['cand_nm']
nycdf2.columns =['cand_nm']

################ third way according slides ###########
dfc=nyc['cand_nm'].value_counts()
dfc.values
ucm=dfc.index.values
nycdf3 = pd.DataFrame({'cand_nm':ucm})

x_dict = {'a':3,'b':10,'c':20}
x_dict['b']

z=zip(nycdf['cand_nm'],nycdf['party'])
cand_dict=dict(z)
cand_dict

nyc['Party']=nyc['cand_nm'].map(cand_dict)
nyc.loc[nyc['cand_nm']=='Clinton, Hillary Rodham','Party']='Democrat'

nyc[['cand_nm','Party']].head(10)

#2
nyc.dtypes
nyc['Date']=pd.to_datetime(nyc['contb_receipt_dt'])
nyc[['contb_receipt_dt','Date']].head(10)

#3
A = pd.Series(['red','blue','yellow','orange','red','blue','yellow','orange'])
B=pd.Series([1 ,1 ,1 ,1 ,2 ,2 ,2 ,2])
Price = pd.Series(np.arange(1,9))
dfexmp=pd.DataFrame({'A':A,'B':B,'Price':Price})
d=dfexmp.groupby('A')['Price'].sum()
type(d)

nyc.groupby('Party')['contb_receipt_amt'].count()
nyc['Party'].value_counts()

#4
d=nyc.groupby(['Party','Date'])['contb_receipt_amt'].count()
type(d)
d.values
d.index
nyc.groupby(['Party','contb_receipt_dt'])['contb_receipt_amt'].count()
nyc.groupby(['Date','Party'])['contb_receipt_amt'].count()

#5
nyc.groupby('Party')['contb_receipt_amt'].sum()
pd.options.display.float_format='{:,.2f}'.format

#6
nyc.groupby(['Party','Date'])['contb_receipt_amt'].sum()
nyc.groupby(['Date','Party'])['contb_receipt_amt'].sum()

#7
nyc.dtypes
df7=nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df7.sort_values(ascending=False,inplace=True)
df7.head(5)
    #or
df7=nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df7 = df7.reset_index()
df7.head(10)
df7.sort_values('contb_receipt_amt',ascending=False,inplace=True)
df7.head(5)
    #or
df7=nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df7 = df7.reset_index()
df7.nlargest(5,'contb_receipt_amt')

#8
df7=nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df7 = df7.reset_index()
df7.sort_values('contb_receipt_amt',inplace=True)
df7.head(5)
    #or
df7=nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df7 = df7.reset_index()
df7.nsmallest(5,'contb_receipt_amt')

df7[df7['contb_receipt_amt']>0].nsmallest(5,'contb_receipt_amt')
df7.loc[df7['contb_receipt_amt']>0].nsmallest(5,'contb_receipt_amt')

#9
nyc.dtypes
df9=nyc.groupby('contbr_employer')['contb_receipt_amt'].sum()
df9 = df9.reset_index()
df9.nlargest(5,'contb_receipt_amt')

#10
df10=nyc.groupby(['cand_nm','contbr_occupation'])['contb_receipt_amt'].sum()
df10 = df10.reset_index()
df10.sort_values(['cand_nm','contb_receipt_amt'],ascending=[True,False],inplace=True)
df10s = df10.groupby('cand_nm').head(5)












