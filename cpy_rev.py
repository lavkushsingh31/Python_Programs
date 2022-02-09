'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(file, revfile):

    with open(file) as f:
        data = f.read()

    with open(revfile, 'w') as rf:
        rf.write(data[::-1])



copy_and_reverse('cf1.txt', 'cf3.txt')
