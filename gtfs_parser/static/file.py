import zipfile


def read_zip(filename):
    with zipfile.ZipFile(filename, 'r') as f:
        infos = f.infolist()
        return {
            i.filename: f.read(i.filename)
            for i in infos
        }


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
