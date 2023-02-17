def read_txt(path):

    file = open(path, encoding="utf8")
    bytes_data = file.read()

    return bytes_data

