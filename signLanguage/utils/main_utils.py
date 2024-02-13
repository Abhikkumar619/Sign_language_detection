import yaml
from pathlib import Path
from  signLanguage.logger import log
import os
import base64
# from box import ConfigBox

def read_yaml_file(file_path: Path): 
    try: 
        with open(file_path, 'r') as yaml_file:
            content=yaml.safe_load(yaml_file)
            # log.info(f"Yaml file load sucessful: {content}")
            return content
    except Exception as e: 
        raise e
    
    
def write_yaml_file(file_path: Path, content: object, replace: bool)-> None:
    try: 
        if replace: 
            if os.path.exists(file_path): 
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as f: 
            yaml.dump(content, file_path)
            log.info(f"Sucessful write yaml file")
        
    except Exception as e: 
        raise e
    
#  Base64 encoding is commonly used for encoding binary data into a text-based format  
# Here image into string and image string into image. 

def DecodeImage(img, file_name): 
    imgdata=base64.b64decode(img)
    # log.info(f"Image Data:  {imgdata}")
    with open("./data/"+file_name, 'wb') as f: 
        f.write(imgdata)
        f.close()
        
        
def EncodeImage(DecodeData_path): 
    with open(DecodeData_path, 'rb') as f: 
        content=base64.b64encode(f.read())
        
        return content