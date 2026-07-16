
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


## barh
rating_counts = df['Rating'].value_counts()
plt.figure(figsize=(8,4))
plt.barh(rating_counts.index, rating_counts.values)

plt.title('percentage of content rating')

plt.tight_layout()
# plt.savefig('content_rating_pie.pdf')
plt.show()


## movies duration histogram 

movie_df = df[df['Category'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['Duration'].str.replace(' min','').astype(int)

plt.figure(figsize=(8,4))
plt.hist(movie_df['duration_int'].values, bins = 30 ,color= 'purple', edgecolor= 'black')
plt.title('distribution movie duration')
plt.xlabel('duration (minutes)')
plt.ylabel('No. of movies')
plt.grid(color='gray', linewidth= 1, linestyle =':', axis='y')

plt.tight_layout()
# plt.savefig('movie_duration_histogram.pdf')
plt.show()



##release year vs shows 

df['Release_Date'] = df['Release_Date'].str.strip()
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
df['Release_Year'] = df['Release_Date'].dt.year
release_counts = df['Release_Year'].value_counts().sort_index()
plt.figure(figsize=(8,4))
plt.scatter(release_counts.index, release_counts.values, color= 'purple')
plt.title('relase year vS no. of shows')
plt.xlabel('release date')
plt.ylabel('no. of shows')
plt.grid(color='gray', linewidth= 1, linestyle =':')

plt.tight_layout()
# plt.savefig('release_years_scatter.pdf')
plt.show()



##  country  count 


country_counts = df['Country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color= 'teal')
plt.title('top 10 country by no. of shows')
plt.xlabel('no. of shows')
plt.ylabel('country name')
plt.grid(color='gray', linewidth= 1, linestyle =':', axis='x')

plt.tight_layout()
# plt.savefig('top_10_countrie_barh.pdf')
plt.show()




content_by_year = df.groupby(['Release_Year', 'Category']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize = (12,5))

# first subplot for movie
ax[0].plot(content_by_year.index,content_by_year['Movie'], color = 'blue')
ax[0].set_title('movies released per year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('no. of movies')
ax[0].grid(color = 'gray', linestyle = ':', linewidth = 1)


# second subplot for movie
ax[1].plot(content_by_year.index,content_by_year['TV Show'], color = 'blue')
ax[1].set_title('TV Show released per year')
ax[1].set_xlabel('year')
ax[1].set_ylabel('no. of TV Show')
ax[1].grid(color = 'gray', linestyle = ':', linewidth = 1)

fig.suptitle('comparision of movies and Tv shows per year')

plt.tight_layout()
# plt.savefig('movie_tvshow_comparision.pdf')
plt.show()