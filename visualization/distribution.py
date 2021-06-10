import random
import plotly.express as px
import plotly.figure_factory as ff 
count = []
dice = []
for i in range (0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1+dice2)
    count.append(i)
graph = px.bar(x = dice,y = count)
graph2 = ff.create_distplot([dice],["dice results"])
graph.show()
graph2.show()
print("done")