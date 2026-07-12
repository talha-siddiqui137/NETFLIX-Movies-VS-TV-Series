# step 1
import pandas as pd
import matplotlib.pyplot as plt


# step 2 data load
df = pd.read_csv('Netflix_Dataset.csv')


# step 3 remove duplicates

df = df.dropna(subset=['Category','Title','Director','Cast','Country','Release_Date','Rating','Duration','Type','Description'])

type_counts = df['Category'].value_counts()

plt.figure(figsize=(8,4))
plt.bar(type_counts.index, type_counts.values, color= ['skyblue', 'orange'])
plt.title('Number of Movies VS TV shows')
plt.xlabel('type')
plt.ylabel('count')
plt.grid(color='gray', linewidth= 1, linestyle =':', axis='y')

plt.tight_layout()
# plt.savefig('movies VS TV show.pdf')
plt.show()