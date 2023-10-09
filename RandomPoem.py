import random

# Define a list of words
words = ["love", "hate", "joy", "sadness", "peace", "war", "life", "death", "light", "dark", "dream", "reality"]

# Generate a random poem
def generate_poem():
  poem = ""
  for i in range(4):
    line = ""
    for j in range(5):
      word = random.choice(words)
      line += word + " "
    poem += line + "\n"
  return poem

# Print the poem
print(generate_poem())
