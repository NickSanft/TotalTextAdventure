import json

def load_json(file_name: str):
    with open(file_name, 'r') as f:
        r = json.load(f)
        print(r)
        return r

if __name__ == '__main__':
    load_json("sample.json")

