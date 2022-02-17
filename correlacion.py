import pandas as pd
import seaborn as sns; sns.set_theme(color_codes=True)
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

df = pd.read_excel('datos.xlsx')
print(df.describe())
df = df.drop('Fecha', axis=1)
df['DEWPOINT (°C)'] += 273.15

print(df.corr()['DEWPOINT (°C)'].sort_values())

# ax = sns.regplot(x="N-Pentano", y="DEWPOINT (°C)", data=df)
# plt.show()
corr = df.corr()
heatmap = sns.heatmap(corr, annot=True, cmap="Blues", fmt='.1g')

fig_reg, axes_reg = plt.subplots(nrows=2, ncols=5, figsize=(15, 8))
axes_reg = axes_reg.flat

fig_reg.suptitle('Correlaciones con DEWPOINT (K)', fontsize = 10, fontweight = "bold")
for i, column in enumerate(df):
  if column != 'DEWPOINT (°C)':
    print(i, column)
    sns.regplot(x=df[column], y=df["DEWPOINT (°C)"], ax=axes_reg[i])
    axes_reg[i].set_title(f"DEWPOINT vs {column}", fontsize = 7, fontweight = "bold")
    axes_reg[i].yaxis.set_major_formatter(ticker.EngFormatter())
    axes_reg[i].xaxis.set_major_formatter(ticker.EngFormatter())    
    axes_reg[i].tick_params(labelsize = 8)    
    axes_reg[i].set_ylabel('[K]', fontsize=8)
    axes_reg[i].set_xlabel(column, fontsize=8)    

# # Se eliminan los axes vacíos
# for i in [8]:
#     fig.delaxes(axes[i])

fig_reg.tight_layout()
plt.subplots_adjust(hspace=0.3, left=0.062, right=0.967, wspace=0.325)
plt.show()
