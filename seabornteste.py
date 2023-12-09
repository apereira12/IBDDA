import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('tips')
print(df.head())


#Histograma
sns.histplot(df['total_bill'], kde= True, bins = 30)


#Gráficos de comparação
sns.jointplot(x = 'total_bill', y ='tip', data=df, hue='sex')
sns.jointplot(x = 'total_bill', y ='tip', color='blue', data=df, kind='hex')
sns.jointplot(x = 'total_bill', y ='tip', color='black', data=df, kind='reg')


#gráfico com todos as váriaveis númericas relacionadas e filtra
sns.pairplot(df, hue="sex")

#Plotagem por categoria
sns.barplot(x = 'sex', y='total_bill', data=df)

plt.show()