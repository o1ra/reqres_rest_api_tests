import json
import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))
schema_files = os.path.join(current_dir, "../schema/")


def load_schema(filepath):
    with open(os.path.join(schema_files + filepath)) as file:
        schema = json.load(file)
        return schema
