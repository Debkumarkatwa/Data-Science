import matplotlib.pyplot as plt
import numpy as np

'''Create a list of values for the x-axis and y-axis'''
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
sachin_run = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

''' Line Chat figure and axis-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
# plt.plot(years, sachin_run)
# plt.title('Sachin Tendulkar"s Yearly Runs')
# plt.xlabel('Year')
# plt.ylabel('Runs')
# plt.grid(True)

''' Multiple Plots in single Figure '''
# plt.plot(years, kohli, label="Virat Kohli")
# plt.plot(years, sehwag, label="Virender Sehwag")
# plt.xlabel("Year")
# plt.ylabel("Runs Scored")
# plt.title("Performance Comparison")
# plt.legend()

''' Bar Chat For Sachin Tendulkar -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
# plt.bar(years, sachin_run, color='blue', label='Sachin Tendulkar')
# plt.xlabel('Year')   
# plt.ylabel('Runs')
# plt.title('Sachin Tendulkar Yearly Runs')

''' Setting Bar Width & Side-by-Side Bar Charts'''
x = np.arange(len(years))  # the label locations
width = 0.25  # the width of the bars

# plt.bar(x - width, sachin_run, width=width, label="Sachin")     # bar location 0.25 left to exact location
# plt.bar(x, sehwag, width=width, label="Sehwag")                 # bar location is the exact location
# plt.bar(x + width, kohli, width=width, label="Kohli")           # bar location 0.25 right to exact location

# plt.xlabel("Year")
# plt.ylabel("Runs")
# plt.title("Run Comparison")
# plt.xticks(x, years)  # Show actual year instead of 0,1,2,...
# plt.legend()
# plt.tight_layout()

''' Horizontal Bar Charts with barh()'''
players = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs_5yrs = [500+700+1100+1500+1800, 0+200+900+1400+1600, 0+0+500+800+1100, 300+600+800+1100+900]
  
# plt.barh(players, runs_5yrs, color="skyblue")
# plt.xlabel("Total Runs in First 5 Years")
# plt.title("First 5-Year Performance of Indian Batsmen")
# plt.tight_layout()

''' Adding Value Labels with plt.text() ''' 
# plt.bar(players, runs_5yrs, color="skyblue", width=0.4)
# for i in range(len(players)):   # Add labels on top of bars
#     plt.text(i, runs_5yrs[i]+28, str(runs_5yrs[i]), ha='center', fontsize=10, color='black', fontweight='bold')

# plt.ylabel("Runs")
# plt.title("Runs Scored by Players in First 5 Years")
# plt.tight_layout()

''' Pie Chart with plt.pie()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
# plt.style.use("ggplot")  # Choose any style you like
# plt.title("Career Runs of Indian Batsmen")
# plt.pie(
#     runs_5yrs,
#     labels=players,
#     colors=["red", "blue", "green", "yellow"],
#     wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': 'solid'},
#     startangle=90,
#     autopct='%1.1f%%',
# )

''' Highlight a Slice Using explode'''
explode = [0.1, 0, 0, 0]  # highlight Sachin's slice 0.1 units away from the center

# plt.pie(runs_5yrs, labels=players, explode=explode, colors=["red", "blue", "green", "yellow"], shadow=True)
# plt.title("Exploded Pie Example")

''' Stack Plot with plt.stackplot()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
days = [1, 2, 3, 4, 5, 6, 7]  # Days of the week
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]
labels = ['Studying', 'Playing', 'Watching TV', 'Sleeping']
colors = ['skyblue', 'lightgreen', 'gold', 'lightcoral']

# plt.stackplot(days, studying, playing, watching_tv, sleeping,
#               labels=labels, colors=colors, alpha=0.8)

# plt.legend(loc='upper left')  # Location of the legend
# plt.title('Weekly Activity Tracker')
# plt.xlabel('Day')
# plt.ylabel('Hours')
# plt.grid(True)

# # Annotate the maximum value of studying
# max_studying = max(studying)
# max_studying_index = studying.index(max_studying)
# plt.annotate(f'Max: {max_studying} hrs',
#              xy=(days[max_studying_index], max_studying),
#              xytext=(days[max_studying_index] + 0.5, max_studying + 1),
#              arrowprops=dict(facecolor='black', arrowstyle='->'),
#              fontsize=10,
#              color='black'
#             )

''' Histograms with plt.hist()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
ages = [
    34, 28, 36, 45, 27, 27, 45, 37, 25, 35,
    25, 25, 32, 10, 12, 24, 19, 33, 20, 15,
    44, 27, 30, 15, 24, 31, 18, 33, 23, 27,
    23, 48, 29, 19, 38, 17, 32, 10, 16, 31,
    37, 31, 28, 26, 15, 22, 25, 4, 33, 12,
    33, 26, 23, 36, 40, 39, 21, 26, 33, 39,
    25, 28, 18, 18, 38, 43, 29, 40, 33, 23,
    33, 45, 29, 45, 3, 38, 30, 27, 30, 10,
    27, 33, 44, 24, 21, 2, 39, 33, 24, 35,
    30, 39, 22, 26, 26, 15, 32, 32, 30, 27
]
bins = [10, 20, 30, 40, 50, 60, 70]

# plt.hist(ages, bins=bins, edgecolor='black')
# plt.title('Age Distribution of YouTube Viewers')
# plt.xlabel('Age Group')
# plt.ylabel('Number of Viewers')
# plt.grid(True, linestyle='-', alpha=1)

''' Scatter Plots with plt.Scatter()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
# Sample data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores = [40, 58, 52, 68, 65, 72, 85, 82, 78]
sizes = [score * 2 for score in exam_scores]
colors = ['gold' if score < 60 else 'lightgreen' for score in exam_scores]

# plt.scatter(study_hours, exam_scores, s=sizes, c=colors)
# # plt.scatter(study_hours, exam_scores, c=exam_scores, cmap='viridis')
# # plt.colorbar(label='Score')
# for i in range(len(study_hours)):   # Add labels on top of points
#     plt.annotate(f'S {i+1}', (study_hours[i] + 0.25, exam_scores[i]))
# plt.title('Colored & Sized Scatter Plot')
# plt.xlabel('Study Hours')
# plt.ylabel('Exam Score')
# plt.grid(True, linestyle='-', alpha=0.5)

# Assume two groups: Class A and Class B
class_a_hours = [2, 4, 6, 8]
class_a_scores = [45, 55, 65, 85]

class_b_hours = [1, 3, 5, 7, 9]
class_b_scores = [40, 50, 60, 70, 90]

# plt.scatter(class_a_hours, class_a_scores, label='Class A', color='blue')
# plt.scatter(class_b_hours, class_b_scores, label='Class B', color='orange')

# plt.title('Scatter Plot: Class A vs Class B')
# plt.xlabel('Study Hours')
# plt.ylabel('Exam Score')
# plt.legend()
# plt.grid(True)

''' Subplots with plt.subplot()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
x = [1, 2, 3, 4, 5]
y1 = [i * 2 for i in x]
y2 = [i ** 2 for i in x]
 
# Create a figure with 1 row and 2 columns
# plt.subplot(1, 2, 1)  # (rows, cols, plot_no)
# plt.plot(x, y1)
# plt.title('Double of x')
 
# plt.subplot(1, 2, 2)
# plt.plot(x, y2)
# plt.title('Square of x')
# plt.tight_layout()

#  2×2 Grid of Subplots
y3 = [i ** 0.5 for i in x]
y4 = [10 - i for i in x]
 
# plt.figure(figsize=(8, 6))  # Optional: make it bigger
# plt.subplot(2, 2, 1)
# plt.plot(x, y1)
# plt.title('x * 2')
 
# plt.subplot(2, 2, 2)
# plt.plot(x, y2)
# plt.title('x squared')
 
# plt.subplot(2, 2, 3)
# plt.plot(x, y3)
# plt.title('sqrt(x)')
 
# plt.subplot(2, 2, 4)
# plt.plot(x, y4)
# plt.title('10 - x')

# plt.tight_layout()













# Show the plot
plt.show()