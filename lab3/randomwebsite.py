import random
import webbrowser

websites = ["https://www.google.com", "https://www.facebook.com", "https://www.amazon.com"]

random_website = random.choice(websites)

webbrowser.open(random_website)
