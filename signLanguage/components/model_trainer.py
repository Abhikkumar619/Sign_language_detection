import os, sys
import yaml
from signLanguage.logger import log
from signLanguage.entity.config_entity import ModelTainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifacts
from signLanguage.utils.main_utils import read_yaml_file
from pathlib import Path
import shutil

class ModelTrainer: 
    def __init__(self, model_trainer_config: ModelTainerConfig) -> None:
        self.model_trainer_config=model_trainer_config
        
    def initate_data_model_trainer(self): 
        log.info(f"Entered in Model Trainer class to initate model trainer function")
        try: 
            log.info(f"Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
            
            with open("data.yaml",'r') as strem: 
                content=yaml.safe_load(strem)
                log.info(f"Content in data. yaml file {content}")
                num_classes=content['nc']
                
                log.info(f"Num of classes in data : {num_classes}")
                
            model_config_file_name=self.model_trainer_config.weight_name.split(".")[0]
            log.info(f"Model name: {model_config_file_name}")
                
            # config=read_yaml_file(f"yolov5\models\{model_config_file_name}.yaml")
                
            # log.info(f"Yaml of yolov5 file \n\n {config}")
                
            # config['nc']=int(num_classes)
            # log.info(f"Yaml of yolov5 file \n\n {config}")

            # with open(f'yolov5\models\custom_{model_config_file_name}.yaml', 'w') as custom_file: 
            #     yaml.dump(config,custom_file)                
                    
            # os.system("cd yolov5")
            # log.info(f"Current directories : {os.getcwd()}")
                
            # os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epoch} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml  --weights {self.model_trainer_config.weight_name} --name yolov5_result --cache")
            # os.system(f"copy yolov5/models/runs/train/yolov5_result/weights/best.pt yolov5/")
            shutil.copy("yolov5/runs/train/yolov5_result8/weights/best.pt", "yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
                
            log.info(f"copy best model to model_train direcotories.")

            # os.system(f"copy yolov5/models/runs/train/yolov5_result/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
            shutil.copy("yolov5/runs/train/yolov5_result8/weights/best.pt", f"{self.model_trainer_config.model_trainer_dir}/")
                
            log.info(f" Removing train , test valid , and data.yaml file")
            os.system("rmdir /s /q yolov5/runs/train")
            os.system('rmdir /s /q  train')
            os.system('rmdir /s /q test')
            os.system('rmdir /s /q valid')
            os.system('rmdir /s /q data.yaml')


                
            model_trainer_artifact=ModelTrainerArtifacts(
                    train_model_file_path="yolov5/best.pt",
                )
                
            
            log.info("From ModelTrainer class exited")
                    
            return model_trainer_artifact
       
                
        except Exception as e: 
            raise e