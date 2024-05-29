#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import random as rd

def recognize_celebrities(photo):
    
    celeb = ['아이유', '츄', '김채원', '김지원']
#     session = boto3.Session(profile_name='profile-name')
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})
        
#     rand_num = rd.randrange(4)
#     rand_num = rd.randint(0,4)
    rand_celeb = rd.choice(celeb)
    
        
    if len(response['CelebrityFaces']) == 0 :
        print('닮은 사람은 {} 입니다.'.format(rand_celeb))
    else :
        print('닮은 사람은 {} 입니다.'.format(response['CelebrityFaces'][0]['Name']))

#     print('Detected faces for ' + photo)
#     for celebrity in response['CelebrityFaces']:
#         print('Name: ' + celebrity['Name'])
# #         print('Id: ' + celebrity['Id'])
# #         print('KnownGender: ' + celebrity['KnownGender']['Type'])
# #         print('Smile: ' + str(celebrity['Face']['Smile']['Value']))
# #         print('Position:')
# #         print('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
# #         print('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
# #         print('Info')
# #         for url in celebrity['Urls']:
# #             print('   ' + url)
# #         print()
#         return len(response['CelebrityFaces'])
    
def main():
    photo = '류선재.jpg'
    celeb_count = recognize_celebrities(photo)
    print("Celebrities detected: " + str(celeb_count))

if __name__ == "__main__":
    main()