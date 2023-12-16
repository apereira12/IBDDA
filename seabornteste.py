import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

'''

df = sns.load_dataset('tips')
print(df.head())
'''

'''#Histograma
sns.histplot(df['total_bill'], kde= True, bins = 30)


#Gráficos de comparação
sns.jointplot(x = 'total_bill', y ='tip', data=df, hue='sex')
sns.jointplot(x = 'total_bill', y ='tip', color='blue', data=df, kind='hex')
sns.jointplot(x = 'total_bill', y ='tip', color='black', data=df, kind='reg')


#gráfico com todos as váriaveis númericas relacionadas e filtra
sns.pairplot(df, hue="sex")

#Plotagem por categoria
sns.barplot(x = 'sex', y='total_bill', data=df)'''


'''#Plotagem BoxPlot para analisar quartil, mediana e outliers
sns.boxplot(x = 'day', y = 'total_bill',data=df)'''

#Plotagem BoxPlot para analisar quartil, mediana e outliers por filtragem de fumante

'''sns.boxplot(x = 'day', y = 'total_bill',data=df, hue='smoker')'''
'''
#Gráfico de violino 
#Utilizar Split para juntar
sns.violinplot(x = 'day', y='total_bill', data=df, hue='sex', split=True)'''

'''
#Gráfico de Enxame
sns.swarmplot(x='day', y='total_bill', data=df)


#Gráfico coringa
sns.catplot(x='day', y='total_bill', data=df, kind='bar')'''
'''
#mapa de calor
voos = sns.load_dataset('flights')

print(voos)

#Primeiro precisa pivotear o mês
vp = voos.pivot_table(index='month', columns='year', values='passengers')

#Mapa de calor
sns.heatmap(vp, cmap='magma')

#necessita da biblioteca scipy
#Mapa de cluster
sns.clustermap(vp, cmap='coolwarm', standard_scale=1)
plt.show()'''