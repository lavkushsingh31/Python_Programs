

def statistics(file):

    with open(file) as fh:
        data = fh.read()

        num_lines = len(data.split('\n'))
        num_words = 0
        num_char = len(data) #- data.count('\n')

        for line in data.split('\n'):
            words = line.split()
            num_words = num_words + len(words)

    stats =  {'lines': num_lines , 'words': num_words, 'characters': num_char}
    return stats

print(statistics('cf1.txt'))


# Optimized code
# def statistics(file_name):
#     with open(file_name) as file:
#         lines = file.readlines()
#
#     return { "lines": len(lines),
#              "words": sum(len(line.split(" ")) for line in lines),
#              "characters": sum(len(line) for line in lines) }
#

# def statistics(file):
#
#     with open(file) as fh:
#         data = fh.readlines()
#         num_lines = len(data)
#
#         num_words = 0
#         num_char = 0
#         for line in data:
#             words = line.split()
#             num_words = num_words + len(words)
#             for word in words:
#                 num_char = num_char + len(word)
#
#     stats =  {'lines': num_lines , 'words': num_words, 'characters': num_char}
#     return stats
