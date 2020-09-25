'''
#reference
https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
#check kakfa version
http://30daydo.com/article/449
'''
import cv2
import numpy as np
from kafka_producer_iot import main_api

#選擇照片
pic_link = ''

#正確度域值
conf_threshold=0.8

#模型位址
faceProto = "./models/opencv_face_detector.pbtxt"
faceModel = "./models/opencv_face_detector_uint8.pb"

ageProto = "./models/age_deploy.prototxt"
ageModel = "./models/age_net.caffemodel"

genderProto = "./models/gender_deploy.prototxt"
genderModel = "./models/gender_net.caffemodel"

# Load network
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)

#定義年齡性別和模型的平均值
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60 ~)']
genderList = ['Male', 'Female']

#定義函數，送入
def getFaceBox(image):
    img = image.copy()
    rows = img.shape[0]
    cols = img.shape[1]
    faceNet.setInput(cv2.dnn.blobFromImage(img,1,size=(360, 540), mean=(104.0, 177.0, 123.0), swapRB=True, crop=False))
    # faceNet.setInput(img,swapRB=True)
    cvOut = faceNet.forward()
    bboxes = []
    r_score = []
    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        if score > conf_threshold:
            print(score)
            r_score.append(score)
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            bboxes.append([left, top, right, bottom])
    return bboxes, r_score


def main():
    img = cv2.imread(pic_link)      #load picture
    print(img.shape)
    bboxes, score = getFaceBox(img)
    age_lst , gender_lst = [],[]
    user_d = {'line_name':'', 'line_id':'','order_whisky':'','datetime':'','total_person':'','age':''}

    for bbox in bboxes:
        print(bbox)
        face = img[np.array(bbox[1],dtype = 'int16'):np.array(bbox[3],dtype = 'int16'),np.array(bbox[0],dtype = 'int16'):np.array(bbox[2],dtype = 'int16')]
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
        gender_lst.append(gender)

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        print("Age Output : {}".format(agePreds))
        print("Age : {}, conf = {:.3f}".format(age, agePreds[0].max()))
        age_lst.append(age)

        label = "{},{}".format(gender, age)
        print(label)
        cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 230, 20),thickness=2)  # (影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
        cv2.putText(img, str(round(score[bboxes.index(bbox)],4)), (int(bbox[2]), int(bbox[3])), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 80), 2)
        cv2.putText(img, label, (np.array(bbox[0],dtype = 'int16'), np.array(bbox[1],dtype = 'int16') - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 157, 80), 2, cv2.LINE_AA)

    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.imshow('img', img)
    # cv2.imwrite('result.jpg',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    user_d['total_person'] = len(bboxes)
    user_d['age'] = ','.join(age_lst)
    user_d['gender'] = ','.join(gender_lst)
    # print(len(bboxes))
    # print(user_d)
    main_api(user_d)

if __name__ == '__main__':
    main()