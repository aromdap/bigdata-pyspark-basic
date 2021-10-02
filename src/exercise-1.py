
# coding: utf-8

# # First project
# 
# ## La Celestina: word patterns search
# 
# Find in "La Celestina" book the following words and count the matches:
# - Celestina
# - Calisto
# - Melibea
# 

# In[7]:

from pyspark import SparkContext


# In[9]:

#get: spark intance
sc = SparkContext() 

#notes:
    #do not run this command more than once or you'll get an error
    #only one instance of SparkContext() is allowed per jupyter notebook
    #even with the error, you will be able to use intance sc after generated, do not worry


# In[10]:

#read: the file text that holds the book information
book = sc.textFile('La+Celestina.txt')


# In[54]:

#show: the last 10 lines of the book to verify
book.top(10)


# ### My solution (different result from teacher's one)

# In[143]:

#set: the pattern words
patterns = ['Celestina', 'Calisto', 'Melibea']
#pull: lines of the book where the words appear
count = [ book.filter(lambda x: word in x).map(lambda x: re.sub(r'[^\w\s]','',x)).count() for word in patterns]
#show: the lines for verification
print(count)


# ### Teacher's solution

# In[140]:

#pull: lines of the book where the words appear
words = book.flatMap(lambda x: x.split()).map(lambda x: x.strip(".,-_:;!¡¿?\'\(\)\"")).countByValue()
#set: the pattern words
patterns = ['Celestina', 'Calisto', 'Melibea']
count = [words[pattern] for pattern in patterns]
print(count)



