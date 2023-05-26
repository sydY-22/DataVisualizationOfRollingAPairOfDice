import plotly.express as px
from die import Die

# Creates two D6 
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_results +1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling Two D6 5,000 Times"
labels = {'x': 'Results', 'y': 'Frequencies of each Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

# Update the layout
fig.update_layout(xaxis_dtick=1)

# Display the bar graph
fig.show()
