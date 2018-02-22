def save_file(file_name, content):
    file = open(file_name, "wb")
    file.write(content.encode("utf-8"))
    file.close()

