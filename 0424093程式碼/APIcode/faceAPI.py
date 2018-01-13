import cv2
import time
from aip import AipFace
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
class faceAPI():
    def __init__(self):
        """API key information"""
        self.__APP_ID = 'APP_ID'
        self.__API_KEY = 'API_KEY'
        self.__SECRET_KEY = 'SECRET_KEY'
        self.__faceConnect=AipFace(self.__APP_ID,self.__API_KEY,self.__SECRET_KEY)
        #Face Feature configure
        self.feature_get_options = {'max_face_num':1,'face_fields':"race,gender,faceshape,qualities"}
        self.tempFeaturePath='../TempPicture/FaceFeature/Temp.png'
        self.tempFeatureDBPath ="../TempPicture/FaceFeature/TempFeatureDB/TempFeature"
        self.tempFTDBpath="../TempPicture/FaceFeature/TempDB/Temp"
        #Identify configure
        self.identify_option= {"ext_fields": "faceliveness","user_top_num":1}
        self.identify_detect_option={'max_face_num':10,'face_fields':"gender,faceshape,qualities"}
        self.tempIdentifyPath="../TempPicture/Identify/TempIdentify.png"
        self.tempIdentifyFeaturePath="../TempPicture/Identify/IdentifyFeature/FaceFeature"
        self.tempIdentifyDBPath="../TempPicture/Identify/IdentifyRecord/IDT"
    # image  resize
    def rectangle(self,image,width,height,xloc,yloc,path):
        frame = cv2.rectangle(image, (xloc, yloc),
        (xloc+width,yloc+height), (255, 0, 0), 2)
        cv2.imwrite(path,frame)
    def resize(self,image,width,height,xloc,yloc,path):
        frame=cv2.resize(image[yloc:yloc + height, xloc:xloc + width], (width, height))
        cv2.imwrite(path,frame)

    def face_feature_detect(self,image):
        self.__system_time=time.strftime('%Y_%m_%d_%H_%M_%S')
        cv2.imwrite(self.tempFeaturePath,image)
        __faceresult = self.__faceConnect.detect(image=get_file_content(self.tempFeaturePath), options=self.feature_get_options)
        print(__faceresult)
        if __faceresult['result_num'] ==1:
                race=__faceresult['result'][0]['race']
                gender=__faceresult['result'][0]['gender']
                if gender=='male':
                    gender='男'
                else:
                    gender='女'
                face_probability, human_probability = __faceresult['result'][0]['face_probability'],__faceresult['result'][0]['qualities']['type']['human']
                if race=='yellow':
                    race='黃色'
                elif race=='white':
                    race='白色'
                elif race=='black':
                    race='黑色'
                if face_probability<=0.9 or human_probability<=0.9:
                    print("低於取樣標準\n再試一次")
                else:
                    print("性別:{}\n膚色:{}\n臉部置信度:{}\n人臉置信度:{}".format(
                        gender,race,
                        face_probability, human_probability))
                    xloc, yloc = __faceresult['result'][0]['location']['left'], __faceresult['result'][0]['location']['top']
                    width, height = __faceresult['result'][0]['location']['width'], __faceresult['result'][0]['location']['height']
                    # image mark face location
                    self.rectangle(image=image,path=self.tempFeaturePath,
                                   width=width,height=height,xloc=xloc,yloc=yloc)
                    self.rectangle(image=image, path=self.tempFTDBpath+self.__system_time+".png",
                                   width=width, height=height, xloc=xloc, yloc=yloc)
                    #image cut face location
                    self.resize(image=image,path=self.tempFeatureDBPath + self.__system_time + ".png"
                                ,width=width,height=height,xloc=xloc,yloc=yloc)
                    add_result=self.__faceConnect.addUser(uid="test02",group_id="groupTest",
                    user_info="姓名:{}|性別:{}|膚色:{}".format("宋東儒",gender,race),
                            image=get_file_content("../TempPicture/FaceFeature/Temp.png"))
                    print(add_result)
        else:
            print("請勿超過一人或空白畫面")
    def identify_user(self,image):
        self.__system_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        cv2.imwrite(self.tempIdentifyPath,image)
        identify_detect_result=self.__faceConnect.detect(
            image=get_file_content(self.tempIdentifyPath),options=self.identify_detect_option)
        detect_num=identify_detect_result['result_num']
        print(detect_num)
        for index in range(0,detect_num):
            xloc,yloc=identify_detect_result['result'][index]['location']['left'],identify_detect_result['result'][index]['location']['top']
            width,height=identify_detect_result['result'][index]['location']['width'],identify_detect_result['result'][index]['location']['height']
            # image mark face location
            self.rectangle(image=image,width=width,height=height,xloc=xloc,yloc=yloc,
                           path=self.tempIdentifyDBPath+self.__system_time+".png")
            # image cut face location
            self.resize(image=image,width=width,height=height,xloc=xloc,yloc=yloc,
                        path=self.tempIdentifyFeaturePath+str(detect_num)+".png")
            __identify_result = self.__faceConnect.identifyUser(
                group_id='groupTest',image=get_file_content(self.tempIdentifyPath),options=self.identify_option)
            print(__identify_result)
            try:
                    if __identify_result['result'][0]['scores'][-1] >=70:
                        print("使用者ID:{}\n所屬群組:{}\n描述:{}".format(
                        __identify_result['result'][0]['uid'],
                        __identify_result['result'][0]['group_id'],
                        __identify_result['result'][0]['user_info']))
                    else:
                        print("Faild不通過\n不符合任一用戶")
                        cv2.imshow("Suspect",cv2.imread(self.tempIdentifyDBPath+self.__system_time+".png"))
            except :
                print("不存在資料庫")

    def update_user(self):
        __update_result = self.__faceConnect.updateUser(
            uid='test_001',
            group_id='groupTest', user_info='testPhoto',
            image=get_file_content('../TempTake/jia.jpg')
        )
        print(__update_result)
    def delete_user(self):
        __delete_result = self.__faceConnect.deleteUser(uid='test01')
        print(__delete_result)
    def delete_group_user(self):
        __delete_group_result=self.__faceConnect.deleteGroupUser(uid='test_002',group_id="groupTest")
        print(__delete_group_result)
    def all_user_query(self):
        __all_query_result = self.__faceConnect.getUser('test_001')
        print(__all_query_result)
    def user_query(self):
        query_options={"group_id":'groupTest'}
        __query_result = self.__faceConnect.getUser(uid='test_001'
                        ,options=query_options)
        print(__query_result)

    def version(self):
        ver=self.__faceConnect.getVersion()
        print(ver)
    def get_groupList(self):
        __list=self.__faceConnect.getGroupList()
        print(__list)
    def get_groupUser(self,):
        __group_user=self.__faceConnect.getGroupUsers(group_id='groupTest')
        print(__group_user)