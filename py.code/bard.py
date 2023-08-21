import matplotlib.pyplot as plt

# Data for the chart
x_values = ["Apples", "Oranges", "Bananas", "Grapes"]
y_values = [25, 18, 30, 15]

# Create the bar chart
plt.bar(x_values, y_values)

# Add labels and title
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.title("Fruit Inventory")

# Display the chart
plt.show()

# AI system to answer questions based on the chart
while True:
    question = input("What would you like to know about the fruit inventory? ")
    if "highest" in question:
        max_value = max(y_values)
        max_index = y_values.index(max_value)
        print(f"The fruit with the highest quantity is {x_values[max_index]} with {max_value} units.")
    elif "lowest" in question:
        min_value = min(y_values)
        min_index = y_values.index(min_value)
        print(f"The fruit with the lowest quantity is {x_values[min_index]} with {min_value} units.")
    elif "total" in question:
        total = sum(y_values)
        print(f"The total quantity of all fruits is {total} units.")
    elif "quit" in question:
        break
    else:
        print("I'm sorry, I don't understand your question.")
