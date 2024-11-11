import json

from rpg_path import RpgPath


def load_json(file_name: str):
    paths = {}
    with open(file_name, 'r') as f:
        json_full = json.load(f)

        for json_path in json_full:
            print(json_path)
            path_id = json_path["path_id"]
            prompt = json_path["prompt"]
            routes = {}
            for key, value in json_path.items():
                if key.isdigit():
                    routes[int(key)] = value
            paths[path_id] = RpgPath(path_id, prompt, routes)
        print(paths)
        return paths

def prompt_option(path: RpgPath):
    print(path.prompt)
    for key, value in path.routes.items():
        print(key, ": ", value)
    result = input(path.prompt)
    return result

if __name__ == '__main__':
    paths = load_json("sample.json")

    path_to_go = 0
    result = prompt_option(paths["0"])

    running = True
    while running:
        current_path = paths[result]
        if len(current_path.routes) == 0:
            print(current_path.prompt)
            running = False
        else:
            result = prompt_option(paths[result])




