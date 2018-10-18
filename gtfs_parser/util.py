def camel_to_snake(name):
    split_name = name.split('_')
    return ''.join([x.capitalize() for x in split_name])


def snake_to_camel(name):
    indices = [0]

    for i in range(1, len(name)):
        if name[i].isupper():
            indices.append(i)

    split_name = []
    for i in range(1, len(name)):
        start = indices[i - 1]
        end = indices[i]
        split_name.append(name[start:end])

    return ''.join(split_name)
