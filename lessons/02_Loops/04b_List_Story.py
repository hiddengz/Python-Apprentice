"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []

#the story
story.append(words[0])
story.append(words[2])
story.append(words[9])
story.append(words[7])
story.append(words[1])
story.append(words[5])
story.append(words[6])
story.append(words[3])
story.append(words[14])
story.append(words[12])
story.append(words[19])
story.append(words[15])
story.append(words[10])
story.append(words[4])
story.append(words[17])
story.append(words[18])

#i tried to do the [1:3] thing the text mentioned but it wouldnt let me so i just did [1]

# Display the story
print(' '.join(story))