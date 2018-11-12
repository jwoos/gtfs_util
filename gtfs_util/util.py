import zipfile


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


class TextZipExtFileWrapper:
    def __init__(self, zipext_file):
        self.file = zipext_file

    def __iter__(self, *args, **kwargs):
        return TextZipExtFileWrapper(self.file.__iter__(*args, **kwargs))

    def __enter__(self, *args, **kwargs):
        return TextZipExtFileWrapper(self.file.__enter__(*args, **kwargs))

    def __exit__(self, *args, **kwargs):
        return self.file.__exit__(*args, **kwargs)

    def __next__(self, *args, **kwargs):
        return self.file.__next__(*args, **kwargs).decode()

    def read(self, *args, **kwargs):
        return self.file.read(*args, **kwargs).decode()

    def readline(self, *args, **kwargs):
        return self.file.readline(*args, **kwargs).decode()

    def readlines(self, *args, **kwargs):
        return self.file.readlines(*args, **kwargs).decode()


class TextZipFile(zipfile.ZipFile):
    def open(self, *args, **kwargs):
        return TextZipExtFileWrapper(super().open(*args, **kwargs))
