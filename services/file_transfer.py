from flask import request


def save_files(path):
    files_list = list()
    for f in request.files.getlist('images'):
        save_path = f'{path}/{f.filename}'
        f.save(save_path)
        files_list.append(save_path)
    return files_list