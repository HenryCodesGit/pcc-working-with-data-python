from dice import Die
from plotly import express as px

numSides = 6
numSides_2 = 10
NUM_ROLLS = 10000
d6 = Die(numSides)
d6_2 = Die(numSides_2)

rolls = []

frequencies = [0] * (numSides + numSides_2)
for i in range(NUM_ROLLS):
    # Make roll
    roll = d6.roll() + d6_2.roll()

    # Add to array
    rolls.append(roll)

    # Increase the histogram
    frequencies[roll-1] += 1

# Visualizing

figure = px.bar(
    x = range(1,numSides+numSides_2+1),
    y = frequencies, 
    title = f'Results of rolling a D{numSides} and a D{numSides_2}, {NUM_ROLLS} times',
    labels = {
        'x': 'Result',
        'y': 'Frequency of Results'
    }
)
figure.update_layout(xaxis_dtick=1) # Distance between tick marks set to equal to 1
figure.show()