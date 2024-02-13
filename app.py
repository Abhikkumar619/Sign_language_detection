from flask import Flask, render_template, request, jsonify
import os, sys
from pathlib import Path
from signLanguage.logger import log
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.utils.main_utils import EncodeImage, DecodeImage


app=Flask(__name__)


class ClientApp:
    def __init__(self) -> None:
        self.file_name="input_image.jpg"

@app.route("/", methods=['GET'])
def home(): 
    return render_template('index.html')

@app.route("/train", methods=['GET'])
def training(): 
    trainPipe=TrainPipeline()
    trainPipe.run_pipeline()
    
    return "Training sucessfully Done"

@app.route("/predict", methods=['GET', 'POST'])
def predictRoute(): 
    try: 
        image=request.json['image']
        DecodeImage(image, clApp.file_name)
    
        os.system("cd yolov5/ && python detect.py --weights my_best.pt --img 416 --conf 0.3 --source ../data/input_image.jpg")
        
        opencode_base64=EncodeImage("yolov5/runs/detect/exp/input_image.jpg")
        
        result={"image": opencode_base64.decode('utf-8')}
        
        return jsonify(result)
        
    except Exception as e: 
        raise e

@app.route("/live", methods=['GET'])
def predictlive(): 
    try: 
        os.system("cd yolov5/ && python detect.py --weights my_best.pt --img 416 --conf 0.3 --source 0")
        # os.system("cd yolov5 && rmdir /s /q runs")
        return "camera starting"
    
    except Exception as e: 
        raise e
    



if __name__ == "__main__": 
    clApp=ClientApp()
    app.run(host='0.0.0.0', debug=True)


