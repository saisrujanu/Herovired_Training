#!/usr/bin/env python
# coding: utf-8

# In[64]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
True_news = pd.read_csv('True.csv')
Fake_news = pd.read_csv('Fake.csv')


# In[65]:


True_news['label'] = 0
Fake_news['label'] = 1
True_news.head()


# In[66]:


Fake_news.head()


# In[67]:


dataset1 = True_news[['text','label']]
dataset2 = Fake_news[['text','label']]


# In[68]:


dataset = pd.concat([dataset1 , dataset2])


# In[69]:


dataset.head(10)


# In[70]:


dataset.isnull().sum()


# In[71]:


dataset = dataset.sample(frac = 1)


# In[72]:


dataset.head()


# In[73]:


import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# In[74]:


ps = WordNetLemmatizer()
stopwords = stopwords.words('english')
nltk.download('wordnet')


# In[75]:


def cleaning_data(row):
    
    # convert text to into lower case
    row = row.lower() 
    
    # this line of code only take words from text and remove number and special character using RegX
    row = re.sub('[^a-zA-Z]' , ' ' , row)
    
    # split the data and make token.
    token = row.split() 
    
    # lemmatize the word and remove stop words like a, an , the , is ,are ...
    news = [ps.lemmatize(word) for word in token if not word in stopwords]  
    
    # finaly join all the token with space
    cleanned_news = ' '.join(news) 
    
    # return cleanned data
    return cleanned_news 


# In[76]:


dataset['text'] = dataset['text'].apply(lambda x : cleaning_data(x))


# In[77]:


dataset.isnull().sum()


# In[78]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[79]:


vectorizer = TfidfVectorizer(max_features = 50000 , lowercase=False , ngram_range=(1,2))


# In[80]:


dataset.head()


# In[81]:


X = dataset.iloc[:35000,0]
y = dataset.iloc[:35000,1]


# In[82]:


from sklearn.model_selection import train_test_split
train_data , test_data , train_label , test_label = train_test_split(X , y , test_size = 0.2 ,random_state = 0)


# In[83]:


vec_train_data = vectorizer.fit_transform(train_data)


# In[84]:


vec_train_data = vec_train_data.toarray()


# In[25]:


train_data.shape , test_data.shape


# In[26]:


vec_test_data = vectorizer.transform(test_data).toarray()


# In[27]:


vec_train_data.shape , vec_test_data.shape


# In[28]:


train_label.value_counts()


# In[29]:


test_label.value_counts() 


# In[31]:


training_data = pd.DataFrame(vec_train_data , columns=vectorizer.get_feature_names_out())
testing_data = pd.DataFrame(vec_test_data , columns= vectorizer.get_feature_names_out())


# In[32]:


from sklearn.naive_bayes import MultinomialNB


# In[33]:


from sklearn.metrics import accuracy_score,classification_report


# In[34]:


clf = MultinomialNB()


# In[35]:


clf.fit(training_data, train_label)
y_pred  = clf.predict(testing_data)


# In[36]:


pd.Series(y_pred).value_counts()


# In[37]:


test_label.value_counts()


# In[38]:


print(classification_report(test_label , y_pred))


# In[39]:


y_pred_train = clf.predict(training_data)
print(classification_report(train_label , y_pred_train))


# In[40]:


accuracy_score(train_label , y_pred_train)


# In[41]:


accuracy_score(test_label , y_pred)


# In[134]:


news = cleaning_data(str("Gnanesh is a male"))


# In[135]:


single_prediction = clf.predict(vectorizer.transform([news]).toarray())
single_prediction


# In[136]:


a=single_prediction


# In[137]:


if(a==1):
    print("Fake")
else:
    print("Real")


# In[ ]:




