from flask import Flask, render_template
import os
import boto3

def compare_faces():

    client = boto3.client('rekognition')

    sourceFile = 'image1.jpg' # 원본 파일 
    targetFile = 'temp.jpg' # 방금 찍은 사진
    
    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})
    
    result = response['FaceMatches'][0]['Similarity']

    imageSource.close()
    imageTarget.close()
    return result

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main2.html') # 해당 파일의 같은 위치에 있는 templates 폴더 안에 있음

@app.route('/detect')
def index():
    os.system('raspistill -o temp.jpg')
    result = compare_faces()
    return str(result)

if __name__ == "__main__" :
    app.run(host='192.168.219.185', port=5000)