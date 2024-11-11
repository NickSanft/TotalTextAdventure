class RpgPath:

    PATHS_LOCATION = "sample.json"
    ID_KEY = "path_id"
    PROMPT_KEY = "prompt"

    def __init__(self, path_id, prompt, routes):
        self.path_id = path_id
        self.prompt = prompt
        self.routes = routes