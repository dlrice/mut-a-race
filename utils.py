#!/usr/bin/env python3
import json


def get_resource_paths():
    with open('./resources/resources.json') as f:
        return json.load(f)


resource_paths = get_resource_paths()


def get_resource_path(resource):
    return resource_paths[resource]
