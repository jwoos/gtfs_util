def camel_to_snake(name):
    indices = [0]

    for i in range(1, len(name)):
        if name[i].isupper():
            indices.append(i)

    split_name = []
    for i in range(1, len(indices)):
        start = indices[i - 1]
        end = indices[i]
        split_name.append(name[start:end].lower())

    split_name.append(name[indices[-1]:].lower())

    return '_'.join(split_name)


def snake_to_camel(name):
    split_name = name.split('_')
    return ''.join([
        split_name[i].capitalize() if i else split_name[i]
        for i in range(len(split_name))
    ])
