# LISTS
# Tech Em Studios
# WEMS Spring ASE

# We all know that Python can do many different things with numbers, let's take a look!

# Make sure you double check your code before hitting run! I might have snuck in my some syntax errors!

sports = "baseball, football, basketball, soccer, tennis, golf, gymnastics"

sports = ['baseball', 'football', 'basketball',
          'soccer', 'tennis', 'golf', 'gymnastics']

print(type(sports))

print(sports)

# We can also look at a certain spot in our lists!

print(sports[2])

print(sports[5])

# And we can change what something is in our list as well. Let's remove baseball, and add cricket!

sports[0] = 'cricket'

# We can also add items to our list instead of replacing something

sports.append('baseball')

print(sports)

# And of course remove items from out list

del sports[4]

print(sports)

# Multiple your lists for max excitment!

print(sports * 100)

print(sports[3] * 29393)
