import requests
import os
import json


def download_file(url, filename):
    request = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(request.content)


def delete_file(filename):
    os.remove(filename)


def get_dict_from_json(json_filename):
    with open(json_filename) as json_file:
        data = json.load(json_file)
    return data


def create_json_from_list(list, filename):
    dict = {'criteria': list}
    with open(filename, 'w') as file:
        file.write(json.dumps(dict))


def file_exists(filename):
    print(os.path.exists(filename))
    return os.path.exists(filename)
