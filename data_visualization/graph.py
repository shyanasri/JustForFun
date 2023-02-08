import seaborn
import pandas
import matplotlib.pyplot as plot
import pandas as pd 
import csv
import numpy as np

rows_list = []
with open("data_visualization/cannabis.csv", encoding="utf-8") as f:

    reader_obj = csv.reader(f) 
    row1 = next(reader_obj)
    for row in reader_obj:
        effects = [x.strip() for x in row[3].split(',')]
        flavours = [x.strip() for x in row[4].split(',')]
        for effect in effects:
            if effect != "None":
                for flavour in flavours:
                    if flavour != "None": 
                        rows_list.append([effect, flavour])

f.close()

df = pd.DataFrame(rows_list, columns=['Effects','Flavours'])

#First Graph
df2 = df['Effects'].value_counts().rename_axis('Effects').reset_index(name='Frequency')
df2.drop(df2.tail(2).index,
        inplace = True)
print(df2)
rel = seaborn.scatterplot(x = "Effects", y = "Frequency", data=df2, s=200, color='xkcd:baby pink').set(title='What are the most common effects of cannabis strains?')
plot.show()

#Second Graph  
sizeddf = df.groupby(df.columns.tolist(),as_index=False).size()
sizeddf.sort_values(by=['size'], inplace=True, ascending=False)
result = sizeddf.head(100)
result['size'] = result['size']/result['size'].abs().max()*100
min = result['size'].min()
data = result.pivot(index='Flavours', columns='Effects', values='size')
data = data.fillna(min)
g = seaborn.heatmap(data, cmap='RdPu',cbar_kws={'label': 'Commonality'}).set(title="What are the common combinations of effects and flavours of cannabis strains?")
plot.show()

