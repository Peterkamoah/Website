import openai
import matplotlib.pyplot as plt

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define the prompt for the ChartGPT model
prompt = """
Please create a bar chart with the following data:
X-axis labels: Apples, Oranges, Bananas, Grapes
Y-axis values: 25, 18, 30, 15
Title: Fruit Inventory
Please make the chart colorful and visually appealing.
Thank you!
"""

# Generate the chart using ChartGPT
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the chart image from the response
chart_image = response.choices[0].text

# Display the chart image using Matplotlib
with open("chart.png", "wb") as f:
    f.write(chart_image)
img = plt.imread("chart.png")
plt.imshow(img)
plt.axis("off")
plt.show()
