import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations 
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty or not a dictionary
        e: any other exception

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")

            if not isinstance(content, dict):
                raise ValueError("YAML content is not a valid dictionary")

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty or invalid")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


# New utility function to get file size in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """Returns size of the file at the given path in KB

    Args:
        path (Path): file path

    Returns:
        str: file size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

def decode_image(imgString,filename):
    imgdata = base64.b64decode(imgString)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        encodedString = base64.b64encode(f.read())
        return encodedString.decode('utf-8')
