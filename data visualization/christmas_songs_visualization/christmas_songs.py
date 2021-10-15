
import csv
import matplotlib.pyplot as plt
import matplotlib as mlp
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image

sns.set_theme(style="darkgrid")
from wordcloud import WordCloud
from mpl_toolkits.axes_grid1 import make_axes_locatable
from wordcloud import WordCloud, STOPWORDS

songdata = pd.read_csv('christmas_songs.csv')
year_count = songdata.groupby(['year']).size().reset_index(name='counts')
#print(year_count)

year_bins = {1950: 0, 1960: 0, 1970: 0, 1980: 0, 1990: 0, 2000: 0, 2010: 0}
for index, row in year_count.iterrows():
    yrs = row['year']
    song_count = row['counts']

    if yrs < 1960:
        year_bins[1950]+=song_count
    elif yrs < 1970:
        year_bins[1960] += song_count
    elif yrs < 1980:
        year_bins[1970]+=song_count
    elif yrs < 1990:
        year_bins[1980]+=song_count
    elif yrs < 2000:
        year_bins[1990]+=song_count
    elif yrs < 2010:
        year_bins[2000]+=song_count
    else:
        year_bins[2010]+=song_count

print(year_bins)

#total no of songs of each decade
keys = list(year_bins.keys())
# get values in the same order as keys, and parse percentage values
vals = [int(year_bins[k]) for k in keys]

sqcol = ["#D5B1C8", "#4A2F27", "#996668", "#B27B82", "#CA929F", "#7E5350", "#64403A"]
sns.barplot(x=keys, y=vals, palette = sns.color_palette(sqcol), saturation=1)

plt.xlabel('Years')
plt.ylabel('Number of Songs')
plt.title('Release Year of Songs in Decades')
plt.show()

#singers and how many songs they have
singer_tablo = songdata.groupby(['year', 'performer']).agg({'songid':'size', 'peak_position':'mean'}) \
       .rename(columns={'songid':'counts','peak_position':'avg_position'}) \
       .reset_index()

singer_tablo['year'] = singer_tablo['year'].apply(lambda x:(x//10)*10)
#print(singer_tablo)
labels, levels = pd.factorize(singer_tablo['performer'])

#violin plot
sns.catplot(x="year", y="counts",
            kind="violin", data=singer_tablo)
plt.xlabel('Years')
plt.ylabel('Number of Songs')
plt.title('No. of Songs for each Singer by Decades')
plt.show()

#better2 = songdata['peak_position']<50
#print(better2)
charts_tablo = songdata.groupby(['performer']).agg({'songid':'size', 'peak_position':'mean', 'weeks_on_chart':'mean'}) \
       .rename(columns={'songid':'counts','peak_position':'avg_position', 'weeks_on_chart':'avg_weeks'}) \
       .reset_index().sort_values(by=['avg_position'], ascending=False)

better2 = charts_tablo['counts']>2
charts_tablo = charts_tablo[better2]
#print(charts_tablo[better2])
charts_tablo['counts'] = charts_tablo['counts'].apply(lambda x:x*30)

labels, levels = pd.factorize(charts_tablo['performer'])

plt.scatter(charts_tablo['avg_weeks'], charts_tablo['avg_position'], c=labels, s=charts_tablo['counts'], alpha=0.3, cmap='viridis')
cbar = plt.colorbar();  # show color scale
cbar.ax.set_ylabel('Singer Color ordered by Success', rotation=270, labelpad=15)
cbar.set_ticks([])

plt.yticks(np.arange(0, 100, 10))
plt.xticks(np.arange(0, 22, 2))
plt.gca().invert_yaxis()
plt.xlabel('Avg weeks')
plt.ylabel('Avg peak position')
plt.title('Singer Success Graph on Chart')

plt.show()

#wordcloud
cs_lyrics = pd.read_csv("christmas_lyrics.tsv.txt", delimiter="\t")
#print(cs_lyrics)

best_songs = songdata['peak_position']<15
top10 = songdata[best_songs]
#print(top10)
#
cs_lyrics = top10.join(cs_lyrics, lsuffix='songid', rsuffix='songid')
#print(cs_lyrics)

lyrics = cs_lyrics['lyric']

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in lyrics:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens) + " "

wave_mask = np.array(Image.open("c3.jpg"))

wordcloud = WordCloud(width=800, height=800,
                      background_color='#ededed',
                      colormap='tab10',
                      contour_color='lightgreen',
                      contour_width= 0.2,
                      mask=wave_mask,
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()