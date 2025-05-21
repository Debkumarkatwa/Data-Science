import seaborn as sns
import matplotlib.pyplot as plt

'''Seaborn practice datasets '''
# print(sns.get_dataset_names())
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 'flights'] 
# ['fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']

tips = sns.load_dataset('tips')
# print(tips.info())

''' Line Plot using Seaborn'''
# sns.lineplot(x="total_bill", y="tip", data=tips)
# plt.title('Line Plot Example')

''' Scatter Plot using Seaborn'''
# sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time")
# plt.title('Scatter Plot with Color by Time')

''' Bar Plot using Seaborn'''
# sns.barplot(x="day", y="total_bill", data=tips)
# plt.title('Average Bill per Day')

''' Box Plot using Seaborn'''
# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.title('Boxplot of Total Bill per Day')

''' Heatmap (Correlation Matrix) using Seaborn'''
flights = sns.load_dataset('flights')
pivot_table = flights.pivot(index = "month", columns= "year", values= "passengers")
 
# sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
# plt.title('Heatmap of Passengers')


plt.show()