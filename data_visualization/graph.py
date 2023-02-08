import seaborn
import pandas
import matplotlib.pyplot as plot
import pandas as pd 
import csv
import numpy as np

rows_list = []
with open("cannabis.csv", encoding="utf-8") as f:

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
df = pd.DataFrame(rows_list, columns=['effects','flavours'])  

sizeddf = df.groupby(df.columns.tolist(),as_index=False).size()
sizeddf.sort_values(by=['size'], inplace=True, ascending=False)
result = sizeddf.head(100)
result['size'] = result['size']/result['size'].abs().max()*100
min = result['size'].min()
data = result.pivot(index='flavours', columns='effects', values='size')
data = data.fillna(min)
g = seaborn.heatmap(data, cmap='RdPu')

plot.show()

