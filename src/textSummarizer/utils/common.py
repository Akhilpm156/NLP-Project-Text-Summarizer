import os
from box.exceptions import BoxValueError
import yaml
from box import Box
from textSummarizer.logging import logger
from pathlib import Path
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> Box:
    """reads yaml file and return config box type"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded successfully")
            return Box(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """Create list of directories"""
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")