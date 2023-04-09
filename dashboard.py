# importing libraries
#import streamlit as st
#import numpy as np 
#import pandas as pd
#import matplotlib.pyplot as plt 
#import seaborn as sns 
#import plotly.express as px

                          
st.set_page_config(layout='wide')
st.title('Amazon sales EDA')
st.text('Developed By: @MuhamedMedhat')

# importing data
df = pd.read_csv('cleaned data.csv')  
df.drop('Unnamed: 0',axis=1,inplace=True)
st.dataframe(df)
st.markdown('---')

# How many product in each category ?
st.subheader('How many product in each category ?')
fig = px.bar(data_frame=df,x='main category',color='quality of product')
fig2 = px.pie(data_frame=df,
             names=df['main category'].value_counts().index,
             values=df['main category'].value_counts().values,
             hole=0.5)
st.plotly_chart(fig)
st.plotly_chart(fig2)
st.markdown('---')

# Top 10 sub categories have products ?
st.subheader('Top 10 sub categories have products ?')
fig = px.bar(data_frame=df,x=df['sub category'].value_counts().nlargest(10).index,
                           y=df['sub category'].value_counts().nlargest(10).values,
                            title='Top 10 sub categories have products')
fig2 = px.pie(data_frame=df,
             names=df['sub category'].value_counts().nlargest(10).index,
             values=df['sub category'].value_counts().nlargest(10).values,
             hole=0.5)   
st.plotly_chart(fig)
st.plotly_chart(fig2)
st.markdown('---')     

# Distribution of discount percentge 
st.subheader('Distribution of discount percentge')
fig = px.histogram(df['discount_percentage %'])
st.plotly_chart(fig)
st.markdown('---') 

# Distribution of discounted price
st.subheader('Distribution of discounted price')
fig = px.histogram(df['discounted_price'])
st.plotly_chart(fig)
st.markdown('---') 

# Distribution of actual price
st.subheader('Distribution of actual price')
fig = px.histogram(df['actual_price'])
st.plotly_chart(fig)
st.markdown('---') 

# Distribution of rating
st.subheader('Distribution of rating')
fig = px.histogram(df['rating'])
st.plotly_chart(fig)
st.markdown('---') 

# the main categories that have highest discount price ?
st.subheader('the main categories that have highest discount price ?')
fig = px.box(data_frame=df,
       x=df['main category'],
       y=df['discounted_price'])
st.plotly_chart(fig)
st.markdown('---')        

# top 10 sub categories have highest dicounted price
st.subheader('top 10 sub categories have highest dicounted price')
fig = px.bar(df['discounted_price'].groupby(df['sub category']).max().nlargest(10),
            title="Top 10 sub categories have highest dicounted price ")
fig.update_layout(yaxis_title='discounted price')
st.plotly_chart(fig)
st.markdown('---') 

# Top 5 expensive products after discount
st.subheader('Top 5 expensive products after discount')
fig = px.bar(data_frame=df.sort_values('discounted_price',ascending=False).head(5),
      x='discounted_price',
      y='product_name')
st.plotly_chart(fig)
st.markdown('---') 

# top 5 cheapest product after discount 
st.subheader('top 5 cheapest product after discount')
fig = px.bar(data_frame=df.sort_values('discounted_price',ascending=False).tail(5),
      x='discounted_price',
      y='product_name')
st.plotly_chart(fig)
st.markdown('---') 

# discounted price range by main category 
st.subheader('discounted price range by main category')
fig = px.scatter(data_frame=df,
          x='discounted_price',
          y='main category')
st.plotly_chart(fig)
st.markdown('---') 

# discounted price range by sub category 
st.subheader('discounted price range by sub category')
fig = px.scatter(data_frame=df,
          x='discounted_price',
          y='sub category')
st.plotly_chart(fig)
st.markdown('---')           

# actual price range by main category 
st.subheader('actual price range by main category')
fig = px.scatter(data_frame=df,
          x='actual_price',
          y='main category')
st.plotly_chart(fig)
st.markdown('---')           

# actual price range by sub category 
st.subheader('actual price range by sub category')
fig = px.scatter(data_frame=df,
          x='actual_price',
          y='sub category')
st.plotly_chart(fig)
st.markdown('---')           

# How many very good and excellent product in each main category 
st.subheader('How many very good and excellent product in each main category')
fig = px.bar(data_frame=df,x=df['main category'],color=df['quality of product'])
st.plotly_chart(fig)
st.markdown('---')

# How many very good and excellent product in each sub category 
st.subheader('How many very good and excellent product in each sub category')
fig = px.bar(data_frame=df,x=df['sub category'],color=df['quality of product'])
st.plotly_chart(fig)
st.markdown('---')

# correlation between actual price and discounted price 
st.subheader('correlation between actual price and discounted price ')
fig = px.scatter(data_frame=df,
           x='discounted_price',
          y='actual_price')
st.plotly_chart(fig)
st.markdown('---')

# correlation
st.subheader("Correlation")
fig = px.imshow(df.corr(),text_auto =True)
st.plotly_chart(fig)
