


def find_and_replace(file, find, replace):

    with open(file,'r+') as f:
        data = f.readlines()

        for line in data:
            for word in line:
                if word == find:
                    word = replace
