import json
import unittest
import os.path

from rpg_path import RpgPath


class TestRpgPathsFile(unittest.TestCase):

    def test_file_present(self):
        self.assertTrue(os.path.isfile(RpgPath.PATHS_LOCATION))

    def test_all_ids_present_no_dupes(self):
        path_ids = []
        with open(RpgPath.PATHS_LOCATION, 'r') as f:
            paths_array = json.load(f)
        for path in paths_array:
            self.assertTrue(RpgPath.ID_KEY in path)
            path_id = path[RpgPath.ID_KEY]
            self.assertFalse(path_id in path_ids)
            path_ids.append(path_id)

