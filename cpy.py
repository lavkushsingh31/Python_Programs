'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(file, cpy_file):
    with open(file) as filehandle:
        data = filehandle.read()

    with open(cpy_file, 'w') as copyfile:
        copyfile.write(data)


copy('cf1.txt', 'cf2.txt')
