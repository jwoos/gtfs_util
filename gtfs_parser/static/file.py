from csv import DictReader
import json
import zipfile


def load(filename, model=False):
    if model:
        raise NotImplementedError()

    with zipfile.ZipFile(filename, 'r') as f:
        infos = f.infolist()
        data = {
            i.filename: DictReader(f.read(i.filename).decode().split('\r\n'))
            for i in infos
        }

        # TODO clean up fieldnames to match model
        # for file, reader in data.items():
            # reader.fieldnames = [x for x in reader.fieldnames]


def load_file(filename, model=False):
    if model:
        raise NotImplementedError()

    with open(filename, 'r') as f:
        return DictReader(f.read().split('\r\n'))
