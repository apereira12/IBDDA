import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Saber quem pagou mais por idade
df = sns.load_dataset('titanic')
print(df)
sns.jointplot(x = 'fare', y ='age', data=df)

sns.barplot()





plt.show()