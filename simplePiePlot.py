import matplotlib.pyplot as plt

# Data 
population = 'Olders', 'Alduts', 'Children', 'Babies'
persons = [20, 40, 25, 15]

# plot pie 
explode = (0, 0, 0, 0.1)  # "explode" the 4th slice (i.e. 'Babies')

plt.pie(persons, explode=explode, labels=population, autopct='%1.1f%%',
        shadow=True, startangle=90)  # textprops={'color':"w"} to change text color
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()