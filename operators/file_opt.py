import os


def get_realpaths(foler_name):
    real_path_list = list()
    paths = os.listdir(foler_name)
    for path in paths:
        full_path = os.path.join(foler_name, path)
        if os.path.isdir(full_path):
            continue
        real_path_list.append(full_path.replace('\\', '/'))
    return real_path_list


def is_pdf_file(name):
    suffix = name.rsplit('.', 1)[-1]
    if suffix == 'pdf':
        return True
    else:
        return False
