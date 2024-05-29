# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def compare_faces(sourceFile, targetFile):

#     session = boto3.Session(profile_name='profile-name')
    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb') # 원본 파일 
    imageTarget = open(targetFile, 'rb') # 비교 파일 

    # Similarity 가 80 이상일 때만 같은 사람이라고 판단하고 결과를 가져옴
    response = client.compare_faces(SimilarityThreshold=1, # 숫자를 1로 바꾸면 다 닮았다고 나옴!
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']: # 만약 결과 값이 있다면
        
        # 해당 얼굴이 인식된 좌표를 가져옴 
#         position = faceMatch['Face']['BoundingBox']

        # 얼마나 닮았는지 수치도 가져옴 
#         similarity = str(faceMatch['Similarity'])

#         print('The face at ' +
#               str(position['Left']) + ' ' +
#               str(position['Top']) +
#               ' matches with ' + similarity + '% confidence')

        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imageSource.close() # 원본 파일 닫기
    imageTarget.close() # 비교 파일 닫기 
    return len(response['FaceMatches'])

def main():
    source_file = 'image1.jpg'
    target_file = 'T1.jpg'
    face_matches = compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))

if __name__ == "__main__":
    main()