import sys  #
import face_recognition  #人脸识别模块
import os  #可以用来打开文件
from xlutils.copy import copy   # 记录在记录信息到excel的时候用
import xlrd    # 计入excel
from os import listdir  # 地址 用于打开位置
import cv2  #打开摄像头
import threading  #多线程
from PyQt5.QtWidgets import QApplication ,QMainWindow,QMessageBox,QFileDialog
from PyQt5.QtCore import QBasicTimer,pyqtSignal,Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from datetime import datetime  #可以用于获取当前的时间
from time import time   #用于计算时间差 可以用来计算一个模块运行的时间
import ft2  #汉字标框模块
from voice_syn_ui import Ui_MainWindow2  # 第二个界面用于 语音合成
from face_re_ui import Ui_MainWindow  # 主窗体ui代码
from baiduyuyin import baidu_voice   #百度语音合成模块
t=time()
class MyMainWindow(QMainWindow,Ui_MainWindow):
    signal=pyqtSignal()  #初始化信号  为了实现双重界面
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.source=0
        # self.timer_camera = QTimer()  # 需要定时器刷新摄像头界面
        self.cap = cv2.VideoCapture()
        self.video_btn=0    # 用去区分打开摄像头和人脸识别 当打开人脸识别按钮的时候 video_btn 就会变成1  这样的话 关闭人脸识别 摄像头还是处于打开的状态
        self.need_record_name1=([])
        self.need_record_name2=([])
# 信号槽设置  ------------------------------


        self.pushButton_8.clicked.connect(lambda:self.video_source(1)) # 对打开摄像头1 按钮进行连接函数  lamda
        self.pushButton_6.clicked.connect(lambda:self.video_source(2)) # 对打开摄像头2 按钮进行连接函数
        self.pushButton_7.clicked.connect(lambda:self.video_source(3))# 对打开摄像头3 按钮进行连接函数  调用了video_source 函数
        self.pushButton_4.clicked.connect(self.face_recognition_btn) # 人脸识别按钮连接函数 调用face_recogniton_btn
        self.pushButton_5.clicked.connect(self.photo_face)  # 拍照按钮 连接函数
        self.pushButton_3.clicked.connect(self.signal_emit) #连接发射信号的函数打开第二个窗口
        self.pushButton.clicked.connect(self.open_file)  # 显示信息 打开文件夹
        self.pushButton_2.clicked.connect(self.open_record)  # 显示记录 连接打开记录的函数
        self.pushButton_9.clicked.connect(self.video_announce)
        print('mainwindow  is running')
        self.progressbarr_move()  # 一个假的进度条 一直在运行 不过到 打开人脸识别按钮的时候它才会变化
        self.show()
# 信号槽对应的函数



    def video_source(self,num):  # 打开摄像头123  这三个按钮 的响应函数 词函数只是提供一个rtsp地址实际的打开摄像头的函数还是下面的btn_opoen_cam_click

        print('切换摄像头')
        if num==1:        #摄像头1
            self.source = "rtsp://admin:5417010101xx@192.168.1.61/Streaming/Channels/1"
            self.btn_open_cam_click(1)

        elif num==2:  #摄像头2 pushButton_6
            self.source= "rtsp://admin:541701010xx@192.168.1.60/Streaming/Channels/1"
            self.btn_open_cam_click(2)
        elif num==3:  #摄像头3
            QMessageBox.about(self,'warning','萤石云摄像头无法使用局域网访问')

    def btn_open_cam_click(self,num):  #打开摄像头 按钮函数

        self.t3=time()
        self.qingping()
        print('click is ok')
        flag2=self.cap.isOpened()  #判断摄像头是否被打开 如果被打开flag2就是ture反之就是false
        print(flag2,' flag')
        if flag2 == False:
             # 使用海康威视网络摄像头
            self.cap.open(self.source)
            #self.progressbarr_move()

            print(self.cap.isOpened())
            self.show_camera()

        else:
            print('关闭摄像头')
            #self.qingping()
            # self.timer_camera.stop()
            self.cap.release()   # 关闭摄像头 对cap进行释放
            self.label_5.clear()
            if num == 1:
                self.pushButton_8.setText(u'打开摄像头1')
            elif num == 2:
                 self.pushButton_6.setText(u'打开摄像头2')
            # 这里设置num1和2  对不同的摄像头进行处理
        self.qingping()
    def face_recognition_btn(self):  # 人脸识别按钮  通过video_btn的值来控制
        self.t2=time()
        self.time_step=0
        if self.video_btn==0:
            self.video_btn=1
            self.pushButton_4.setText(u'关闭人脸识别')
            self.show_camera()
            #由于
        elif self.video_btn==1:
            self.video_btn=0
            self.time_step=0  #进度条初始化 当下次打开人脸识别的时候  再次打开进度条
            self.pushButton_4.setText(u'人脸识别')
            self.qingping()
            self.show_camera()
            self.qingping()
    def progressbarr_move(self):  #使用这个函数和下面的timerEvent(QBasicTimer自带的构造函数) 使得在打卡人脸识别的时候有一个进度条
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
    def timerEvent(self, e):  #这个进度条并不是实际意义上的进度条  我弄了好久发现我想要的那种效果根本实现不了  又不忍心删掉 就用了一种比较不太好的方法实现了进度条
                               #在初始化ui的时候进度条已经开始了不过我没有让他变化 等到打开了人脸识别的开关就开始了变化等到 成为了100%就瞬间变成0
        if self.step >= 100:
          #time.sleep(3) 尝试休眠 但起不到效果
            self.progressBar.setValue(0)
            self.step=0
            self.time_step=1
            return
        if self.video_btn==1 and self.time_step==0:
            self.step = self.step+18
        elif self.video_btn==0:
            self.step=0
        else :
            self.step=self.step
        self.progressBar.setValue(self.step)


    def show_camera(self):  #展示摄像头画面并进行人脸识别的功能
        print('show_camera is open ')
        if self.video_btn==0:    #在前面就设置了video_btn为0 为了在人脸识别的时候直接把这个值给改了 这样人脸识别和摄像头展示就分开了
            if  self.source == "rtsp://admin:5417010101xx@192.168.1.61/Streaming/Channels/1":
                self.pushButton_8.setText(u'关闭摄像头1')
            else:
                self.pushButton_6.setText(u'关闭摄像头2')
            while (self.cap.isOpened()):

                ret, self.image = self.cap.read()
                QApplication.processEvents()  #这句代码告诉QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者  让代码变的没有那么卡
                show = cv2.resize(self.image, (800, 494))
                show = cv2.cvtColor(show,cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                self.showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.label_5.setPixmap(QPixmap.fromImage(self.showImage))

              #  因为他最后会存留一张 图像在lable上需要对 lable_5进行清理
            self.label_5.clear()
            print('打开摄像头时间',time()-self.t3)

        elif self.video_btn==1:
            #这段代码是 获取photo文件夹中 人的信息
             filepath='photo'
             filename_list=listdir(filepath)
             known_face_names=[]
             known_face_encodings=[]
             a=0
             print('2')
             for filename in filename_list:#依次读入列表中的内容
                a+=1
                QApplication.processEvents()
                if filename.endswith('jpg'):# 后缀名'jpg'匹对
                    known_face_names.append(filename[:-4])#把文件名字的后四位.jpg去掉获取人名
                    file_str='photo\\'+filename
                    a_images=face_recognition.load_image_file(file_str)
                    print(file_str)
                    a_face_encoding = face_recognition.face_encodings(a_images)[0]
                    known_face_encodings.append(a_face_encoding)
             print(known_face_names,a)
            #knowe_face_names里面放着每个人的名字   known_face_encodings里面放着提取出来的每个人的人脸特征信息

             face_locations = []
             face_encodings = []
             face_names =[]
             process_this_frame = True
             while (self.cap.isOpened()):
                 ret, frame = self.cap.read()
                 QApplication.processEvents()
                    # 改变摄像头图像的大小，图像小，所做的计算就少
                 small_frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)
                # print('3 is running')
                    # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
                 rgb_small_frame = small_frame[:, :, ::-1]
                 #print('4 is running')
                 if process_this_frame:
                     QApplication.processEvents()
                        # 根据encoding来判断是不是同一个人，是就输出true，不是为flase
                     face_locations = face_recognition.face_locations(rgb_small_frame)
                     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                     face_names = []
                    # print('5 is  running')
                     for face_encoding in face_encodings:
                            # 默认为unknown
                         matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.42)
                            #阈值太低容易造成无法成功识别人脸，太高容易造成人脸识别混淆 默认阈值tolerance为0.6
                            #print(matches)
                         name = "Unknown"

                         if True in matches:
                             first_match_index = matches.index(True)
                             name = known_face_names[first_match_index]

                         face_names.append(name)
                 process_this_frame = not process_this_frame
                    # 将捕捉到的人脸显示出来
                 self.set_name=set(face_names)
                 self.set_names=tuple(self.set_name) # 把名字先设为了一个 集合 把重复的去掉 再设为tuple 以便于下面显示其他信息和记录 调用
                 voice_syn=str()
                 print(self.set_names) #把人脸识别检测到的人 用set_names 这个集合收集起来
                 self.write_record() #把名字记录到excel中去
                 #self.video_announce()
                 for (top, right, bottom, left), name in zip(face_locations, face_names):
                        #由于我们检测到的帧被缩放到1/4大小，所以要缩小面位置
                     top *= 3
                     right *= 3
                     bottom *= 3
                     left *= 3
                        # 矩形框
                     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
                     ft = ft2.put_chinese_text('msyh.ttf')
                        #引入ft2中的字体
                       # cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)这是不输入汉字时可以用的代码

                     frame = ft.draw_text(frame, (left+10 , bottom ), name, 25, (0, 0, 255))
                     print('face recognition is running')
                        #def draw_text(self, image, pos, text, text_size, text_color)

                 self.show_picture() # 调用显示详细信息的函数

                 show_video = cv2.resize(frame, (800, 494))
                 show_video = cv2.cvtColor(show_video,cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                 self.showImage = QImage(show_video.data, show_video.shape[1], show_video.shape[0], QImage.Format_RGB888)
                 self.label_5.setPixmap(QPixmap.fromImage(self.showImage))
             print('打开人脸识别所需要的时间',time()-self.t2)


    def photo_face(self):  #实现保存截图的功能 图片保存在了 video_screenshot 文件夹里面  名字是根据时间命名
        photo_save_path = os.path.join(os.path.dirname(os.path.abspath('__file__')),
                                       'video_screenshot/')
        # self.time_flag.append(datetime.now().strftime("%Y%m%d%H%M%S")
        self.showImage.save(photo_save_path + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg")


        QMessageBox.information(self, "Information",
                                self.tr("拍照成功!"))

    def show_picture(self):  #  在人脸识别的右边显示 识别出来人的详细信息
         if self.video_btn==1:
             fr = open("test.txt",'r+')  #读取information.txt中的信息  里面是录入信息时写入的
             infor_dic = eval(fr.read())   #从information.txt文件中读取的str转换为字

             try:
                person1=self.set_names[0]
                infor_names=infor_dic[person1]
                name_str='photo//'+person1+'.jpg'
                picture=QPixmap(name_str)

                infor_str='姓名：'+person1+'                '+'年龄：'+infor_names['年龄']+'                 '+'性别：'+infor_names['性别']+'                 '+'更多信息： '+infor_names['更多信息']

                self.label_2.setText(infor_str)
                self.label_2.setStyleSheet("color:rgb(192,192,192);font-size:20px;font-family:Microsoft YaHei;")
                self.label_2.setWordWrap(True)  #自适应大小换行
                self.label_7.setPixmap(picture)  #把照片放到label_7上面去
                self.label_7.setScaledContents(True)  #让照片能够在label上面自适应大小
             except:
                self.label_7.clear()  # 照片1
                self.label_2.setText("")
                print('没有检测到人脸')
             try:
                person2=self.set_names[1]
                infor_names=infor_dic[person2]
                name_str='photo//'+person2+'.jpg'
                picture=QPixmap(name_str)

                infor_str='姓名：'+person2+'                '+'年龄：'+infor_names['年龄']+'                 '+'性别：'+infor_names['性别']+'                 '+'更多信息： '+infor_names['更多信息']

                self.label.setText(infor_str)
                self.label.setStyleSheet("color:rgb(192,192,192);font-size:20px;font-family:Microsoft YaHei;")
                self.label.setWordWrap(True)  #自适应大小换行
                self.label_6.setPixmap(picture)  #把照片放到label_7上面去
                self.label_6.setScaledContents(True)  #让照片能够在label上面自适应大小
             except:
                self.label.clear()
                self.label_6.setText("")
                print('没有检测到两个人脸')
             try:
                person3=self.set_names[2]
                infor_names=infor_dic[person3]
                name_str='photo//'+person3+'.jpg'
                picture=QPixmap(name_str)

                infor_str='姓名：'+person3+'                '+'年龄：'+infor_names['年龄']+'                 '+'性别：'+infor_names['性别']+'                 '+'更多信息： '+infor_names['更多信息']

                self.label_3.setText(infor_str)
                self.label_3.setStyleSheet("color:rgb(192,192,192);font-size:20px;font-family:Microsoft YaHei;")
                self.label_3.setWordWrap(True)  # 自适应大小换行
                self.label_4.setPixmap(picture)  # 把照片放到label_7上面去
                self.label_4.setScaledContents(True)  # 让照片能够在label上面自适应大小
             except:
                print('没有检测到三个人脸')
                self.label_3.clear()
                self.label_4.setText("")

             fr.close()
    def qingping(self):  # 不需要显示信息的时候   把显示到信息的那部分清除掉 在循环中保存了几次那些lable就不在发生变化了
         self.label_7.clear()  # 照片1
         self.label_2.setText("")  # 信息1
         self.label.clear()
         self.label_6.setText("")
         self.label_3.clear()
         self.label_4.setText("")

    def signal_emit(self):
        self.signal.emit()#  信号发出
        #baidu_voice('欢迎来到郑州轻工业大学ai人工智能实验室')
    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self,"录入信息","E:\Python code\zwh_face_voice_items\photo")#  打开这个文件夹 选择打开的文件 phot里面的照片是打不开的 因为.py文件在外面
        print(file_name)   # file_name 是一个返回值 类似于这种('E:/Python code/gui/hkvideo/information.txt', 'All Files (*)') 想要打开需要一些处理
        try:
            file_name2=list(file_name)[0] # 想要的是information，text 所以需要需要对file_name进行处理 需要注意的是打开的是 photo文件夹是向里面传照片的再返回出来 填写information
            t_file=0
            for i in file_name2:
                if i=='/':
                    num=t_file
                t_file=t_file+1
            open_file3=file_name2[(num+1):]
            os.system(open_file3)
        except:
            print('没有打开文件')

    def write_record(self):   #把识别出来的人脸记录到一个excel表格中（有漏洞）
        #self.need_record_name=set(self.need_record_name)
        print('need_record_names1 is',self.need_record_name1)
        print('need_record_names2 is',self.need_record_name2)

        if self.source=="rtsp://admin:5417010101xx@192.168.1.61/Streaming/Channels/1":
            if self.set_name.issubset(self.need_record_name1):  # 如果self.set_names是self.need_record_names 的子集返回ture
                pass                                             # need_record_name1是要写进excel中的名字信息 set_name是从摄像头中读出人脸的tuple形式
            else :
                print('ready to write')
                self.different_name1=self.set_name.difference(self.need_record_name1) # 获取到self.set_name有 而self.need_record_name 无的名字
                self.need_record_name1=self.set_name.union(self.need_record_name1)  # 把self.need_record_name  变成两个集合的并集
                                            #different_name是为了获取到之前没有捕捉到的人脸  并且再次将need_recore_name1进行更新

                filename='data.xls'            #文件名准备打开excel
                book = xlrd.open_workbook(filename)  # 打开excel
                new_book = copy(book)  # 复制excel
                sheet2 = new_book.get_sheet(0)  # 获取第一个表格的数据
                sheet0 = book.sheet_by_index(0)
                nrows = sheet0.nrows    # 获取行总数
                print("行数",nrows)
                ncols = sheet0.ncols    #获取列总数
                print("列数",ncols)
                write_in_data=tuple(self.different_name1)  #上面的different-name1还是一个集合需要变成一个tuple
                names_length=len(write_in_data)      # 获取到需要写入表格 人数的长度
                for i in range(names_length):
                    #baidu_voice(write_in_data[i])  对进入的人脸进行播报
                    str_time=str(datetime.now())
                    sheet2.write(nrows+i,0,str_time)
                    sheet2.write(nrows+i,2,write_in_data[i])
                    sheet2.write(nrows+i,1,'摄像头1')
                    sheet2.write(nrows+i,3,'使用摄像头1进行测试')

                new_book.save('secondsheet.xls')  # 保存新的excel
                os.remove(filename)  # 删除旧的excel
                os.rename('secondsheet.xls', filename)  # 将新excel重命名
        elif self.source=="rtsp://admin:541701010xx@192.168.1.60/Streaming/Channels/1":
            if self.set_name.issubset(self.need_record_name2):  # 如果self.set_names是self.need_record_names 的子集返回ture
                pass
            else :
                print('ready to write')
                self.different_name2=self.set_name.difference(self.need_record_name2) # 获取到self.set_name有 而self.need_record_name 无的名字
                self.need_record_name2=self.set_name.union(self.need_record_name2)  # 把self.need_record_name  变成两个集合的并集

                filename='data.xls'
                book = xlrd.open_workbook(filename)  # 打开excel
                new_book = copy(book)  # 复制excel
                sheet2 = new_book.get_sheet(0)  # 获取第一个表格的数据
                sheet0 = book.sheet_by_index(0)
                nrows = sheet0.nrows    # 获取行总数
                print("行数",nrows)
                ncols = sheet0.ncols    #获取列总数
                print("列数",ncols)
                write_in_data=tuple(self.different_name2)
                names_length=len(write_in_data)      # 获取到需要写入表格 人数的长度
                for i in range(names_length):
                   # baidu_voice(write_in_data[i])
                    str_time=str(datetime.now())
                    sheet2.write(nrows+i,0,str_time)
                    sheet2.write(nrows+i,2,write_in_data[i])
                    sheet2.write(nrows+i,1,'摄像头2')
                    sheet2.write(nrows+i,3,'使用摄像头2进行测试或是进入实验室')

                new_book.save('secondsheet.xls')  # 保存新的excel
                os.remove(filename)  # 删除旧的excel
                os.rename('secondsheet.xls', filename)  # 将新excel重命名

    def video_announce(self):  #语音播报模块  点击之后会对已经记录下来的人脸名字进行播报
        #跟录入excel中数据情况类似  self.need_record_name1 是一个当前包含所有名字的集合 利用这个集合输出
        if self.source=="rtsp://admin:541701010xx@192.168.1.60/Streaming/Channels/1":
            need_voice_name=self.need_record_name2
 # 由于在记录表格时 对于两种不同摄像头下设了两个集合 所以要进行一下判断
        elif self.source=="rtsp://admin:5417010101xx@192.168.1.61/Streaming/Channels/1":
            need_voice_name=self.need_record_name1
        print(need_voice_name)
        if 'Unknown' in need_voice_name :# 把unknown去掉 不进行播报
            need_voice_name.remove('Unknown')
        tuple_voice_name=tuple(need_voice_name)
        if tuple_voice_name==():
            QMessageBox.about(self,'warning','还未识别出人脸')
        else:
            voice_str='欢迎'
            for i in tuple_voice_name:
                voice_str=voice_str+i+' '
            voice_str=voice_str+'的到来'
            baidu_voice(voice_str)  # 欢迎 某 某某 的到来






    def open_record(self):
        os.system('data.xls')


class MineWindow(QMainWindow,Ui_MainWindow2): # ui_mainwindow2 是baiduyuyin这个ui里面的 为了实现双重界面 使用信号
    def __init__(self,parent=None):
        super(MineWindow, self).__init__(None, Qt.FramelessWindowHint)  # 这句和普通的不一样 因为可以实现无边框
        #super(MineWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.baidu_voice2)  #合成按钮 执行合成函数
        self.pushButton_2.clicked.connect(self.close_voice) #退出按钮 执行退出窗口

    def baidu_voice2(self):
        self.text_Edit = self.textEdit.toPlainText()  #获取 输入到 textEdit上的字体  并传递给语音合成函数
        print(self.text_Edit)
        baidu_voice(self.text_Edit)#  调用百度语音合成的模块
    def close_voice(self):
        os.system('taskkill /f /im PotPlayerMini64.exe')  #关闭播放音频的软件
        self.close()  #关闭界面


if __name__=="__main__" :
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    Mine=MineWindow()
    myWin.signal.connect(Mine.show)  #连接信号
    print('打开ui界面所需时间',time()-t)
    sys.exit(app.exec_())
