import osssss
import shutil
import time
import zipfile
import ortho_process
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import  QWidget,QMessageBox
class Ui_MainWindow(object):
    zip_files=[]
    input_directory_path = ''
    output_directory_path = ''
    dem_directory_path = ''
    zip_process_counter = 0
    file_process_counter = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 577)
        MainWindow.setStyleSheet("QPushButton{\n""background-color: rgb(255, 255, 255);\n""qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n""}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messagebox=QtWidgets.QMessageBox(MainWindow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(60, 17, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_isro_logo = QtWidgets.QLabel(self.widget)
        self.label_isro_logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_isro_logo.setObjectName("label_isro_logo")
        self.horizontalLayout_2.addWidget(self.label_isro_logo)
        self.verticalLayout_2.addWidget(self.widget)
        self.mainwidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.mainwidget.sizePolicy().hasHeightForWidth())
        self.mainwidget.setSizePolicy(sizePolicy)
        self.mainwidget.setObjectName("mainwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.mainwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_zip_files = QtWidgets.QListWidget(self.mainwidget)
        self.listWidget_zip_files.setMinimumSize(QtCore.QSize(175, 0))
        self.listWidget_zip_files.setMaximumSize(QtCore.QSize(200, 16777215))
self.listWidget_zip_files.setObjectName("listWidget_zip_files")
        self.gridLayout.addWidget(self.listWidget_zip_files, 0, 0, 4, 1)
        self.listWidget_zip_files.show()
        self.widget1 = QtWidgets.QWidget(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(172, 17, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_start = QtWidgets.QPushButton(self.widget1)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.setDisabled(True)
        self.process_thread = orthorectifyProgressThread(self)
self.pushButton_start.clicked.connect(self.process_thread.start)
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.widget1)
        self.pushButton_stop.setDisabled(True)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_stop.clicked.connect(self.stop_pushed)
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.gridLayout.addWidget(self.widget1, 1, 1, 1, 2)
        self.groupBox_current_process_image = QtWidgets.QGroupBox(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.groupBox_current_process_image.sizePolicy().hasHeightForWidth())
        self.groupBox_current_process_image.setSizePolicy(sizePolicy)
self.groupBox_current_process_image.setObjectName("groupBox_current_process_image")
        self.gridLayout.addWidget(self.groupBox_current_process_image, 2, 1, 1, 1)
        self.groupBox_rectified_image_out = QtWidgets.QGroupBox(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.groupBox_rectified_image_out.sizePolicy().hasHeightForWidth())
        self.groupBox_rectified_image_out.setSizePolicy(sizePolicy)
self.groupBox_rectified_image_out.setObjectName("groupBox_rectified_image_out")
        self.gridLayout.addWidget(self.groupBox_rectified_image_out, 2, 2, 1, 1)
        self.label_current_image_name = QtWidgets.QLabel(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.label_current_image_name.sizePolicy().hasHeightForWidth())
        self.label_current_image_name.setSizePolicy(sizePolicy)
        self.label_current_image_name.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_current_image_name.setWordWrap(True)
self.label_current_image_name.setObjectName("label_current_image_name")
        self.gridLayout.addWidget(self.label_current_image_name, 3, 1, 1, 1)
        self.label_processed_image_name = QtWidgets.QLabel(self.mainwidget)
self.label_processed_image_name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_processed_image_name.setWordWrap(True)
self.label_processed_image_name.setObjectName("label_processed_image_name")
        self.gridLayout.addWidget(self.label_processed_image_name, 3, 2, 1, 1)
        self.centralwidget.ProgressWidget = QtWidgets.QWidget(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.centralwidget.ProgressWidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.ProgressWidget.setSizePolicy(sizePolicy)
self.centralwidget.ProgressWidget.setObjectName("ProgressWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget.ProgressWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_zip_processed_status = QtWidgets.QLabel(self.centralwidget.ProgressWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_zip_processed_status.sizePolicy().hasHeightForWidth())
        self.label_zip_processed_status.setSizePolicy(sizePolicy)
        self.label_zip_processed_status.setObjectName("label_zip_processed_status")
        self.verticalLayout.addWidget(self.label_zip_processed_status)
        self.centralwidget.progressBar_zip_process_progress = QtWidgets.QProgressBar(self.centralwidget.ProgressWidget)
        self.centralwidget.progressBar_zip_process_progress.setProperty("value", 0)
        self.centralwidget.progressBar_zip_process_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.centralwidget.progressBar_zip_process_progress.setObjectName("progressBar_zip_process_progress")
        self.verticalLayout.addWidget(self.centralwidget.progressBar_zip_process_progress)
        self.label_tiff_processed_status = QtWidgets.QLabel(self.centralwidget.ProgressWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tiff_processed_status.sizePolicy().hasHeightForWidth())
        self.label_tiff_processed_status.setSizePolicy(sizePolicy)
        self.label_tiff_processed_status.setObjectName("label_tiff_processed_status")
        self.verticalLayout.addWidget(self.label_tiff_processed_status)
        self.centralwidget.progressBar_file_process_progress = QtWidgets.QProgressBar(self.centralwidget.ProgressWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.progressBar_file_process_progress.sizePolicy().hasHeightForWidth())
        self.centralwidget.progressBar_file_process_progress.setSizePolicy(sizePolicy)
        self.centralwidget.progressBar_file_process_progress.setProperty("value", 0)
        self.centralwidget.progressBar_file_process_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.centralwidget.progressBar_file_process_progress.setObjectName("progressBar_file_process_progress")
        self.verticalLayout.addWidget(self.centralwidget.progressBar_file_process_progress)
        self.gridLayout.addWidget(self.centralwidget.ProgressWidget, 0, 1, 1, 2)
        self.verticalLayout_2.addWidget(self.mainwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 21))
        self.menubar.setObjectName("menubar") 
        self.menuFiles = QtWidgets.QMenu(self.menubar) 
        self.menuFiles.setObjectName("menuFiles")
        self.menuHelp = QtWidgets.QMenu(self.menubar) 
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow) 
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #create actions in the File Menu
        self.actionSelect_Input_Directory = QtWidgets.QAction(MainWindow)        self.actionSelect_Input_Directory.setObjectName("actionSelect_Input_Directory")
        self.actionSelect_Input_Directory.triggered.connect(self.setInputDirectory) 
        self.actionOutput_Directory = QtWidgets.QAction(MainWindow) 
self.actionOutput_Directory.setObjectName("actionOutput_Directory") 
self.actionOutput_Directory.triggered.connect(self.setOutputDirectory) 
        self.actionSelect_DEM_Directory = QtWidgets.QAction(MainWindow) #object for the action to set DEM Directory
        self.actionSelect_DEM_Directory.setObjectName("actionSelect_DEM_Directory")
        self.actionSelect_DEM_Directory.triggered.connect(self.setDEMDirectory)#Connect the action to the signal function setDEMDirectory() which will open folder selection dialog
        self.actionQuit = QtWidgets.QAction(MainWindow)#object for QUIT Action
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)#Exit the Application on selction of action

        #create actions in Help Menu
        #functions for these actions are yet to be implemented
        self.actionAbout_NRSC = QtWidgets.QAction(MainWindow) #Action object for AboutNRSC
        self.actionAbout_NRSC.setObjectName("actionAbout_NRSC")
        self.actionAbout_OrthoRectifiction = QtWidgets.QAction(MainWindow) #Action object for About Orthorectification
        self.actionAbout_OrthoRectifiction.setObjectName("actionAbout_OrthoRectifiction")

        #add the created actions to the Menu
        self.menuFiles.addAction(self.actionSelect_Input_Directory)
        self.menuFiles.addAction(self.actionSelect_DEM_Directory)
        self.menuFiles.addAction(self.actionOutput_Directory)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_NRSC)
        self.menuHelp.addAction(self.actionAbout_OrthoRectifiction)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label_isro_logo.setBuddy(self.label_isro_logo)


        self.process_thread.file_progressed.connect(self.updateFileProgress)
        self.process_thread.zip_progressed.connect(self.updateZipProgress)
        self.process_thread.thread_start.connect(self.thread_start_init)
        self.process_thread.message.connect(self.alert)
        self.process_thread.fileexist.connect(self.fexist)
        self.process_thread.zipexist.connect(self.zexist)
        self.process_thread.quit.connect(self.threadquit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def threadquit(self):
        #self.process_thread.file_progressed=0
        #self.process_thread.zip_progressed=0
        self.zip_files=[]
        self.input_directory_path = ''
        self.output_directory_path = ''
        self.dem_directory_path = ''
        self.zip_process_counter = 0
        self.centralwidget.progressBar_zip_process_progress.setValue(0)
        self.file_process_counter = 0
        self.listWidget_zip_files.clear()
        self.process_thread.terminate()

    def fexist(self):
        self.process_thread.merge = False
        btn=self.messagebox.question(self.centralwidget,"orthorefication message","image not exists press yes for skip & no for stopping the process",self.messagebox.Yes | self.messagebox.No, self.messagebox.No)
        if(btn==self.messagebox.Yes): 
            self.process_thread.btnreply=1
            self.process_thread.fileflag=False;
        else:
            self.process_thread.btnreply=0
            self.process_thread.fileflag=False;

    def zexist(self):
        zipbtn=self.messagebox.question(self.centralwidget,"orthorefication message","zip file not exists press yes for skip & no for stopping the process",self.messagebox.Yes | self.messagebox.No, self.messagebox.No)
        self.process_thread.merge = False
        print("the zipbtn is",zipbtn)
        if(zipbtn==self.messagebox.Yes): 
            print("i am in zipbtn true")
            self.process_thread.zipbtnreply=1
            self.process_thread.zipflag=False;
        else:
            print("i am in zipbtn true")
            self.process_thread.zipbtnreply=0
            self.process_thread.zipflag=False;


    def alert(self):
        self.process_thread.merge = False
        btnreply=self.messagebox.question(self.centralwidget,"orthorefication message","file not in format",self.messagebox.Cancel,self.messagebox.Cancel)
        if(btnreply==self.messagebox.Cancel): 
            self.process_thread.flag=False;


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NRSC Orthorectification"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#e26701;\">Ortho Rectification using Opensource Tools</span></p><p><span style=\" font-size:14pt; color:#047dc8;\">NRSC Outreach Project</span></p></body></html>"))
        self.label_isro_logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"D:\\NRSC_Times\\Python\\pygdalftp\\src\\img\\100x97.png\"></p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.groupBox_current_process_image.setTitle(_translate("MainWindow", "Currently Processing Image: "))
        self.groupBox_rectified_image_out.setTitle(_translate("MainWindow", "Previously Processed Image Output : "))
        self.label_current_image_name.setText(_translate("MainWindow", "<html><head/><body><p>Current_Image_Name.tiff</p></body></html>"))
        self.label_processed_image_name.setText(_translate("MainWindow", "<html><head/><body><p>Previous_Image_recitfied_output.tif</p></body></html>"))
        self.label_zip_processed_status.setText(_translate("MainWindow", "Waiting for Input Directory"))
        self.centralwidget.progressBar_zip_process_progress.setFormat(_translate("MainWindow", "%p% Completed"))
        self.label_tiff_processed_status.setText(_translate("MainWindow", "Waiting for Input Directory"))
        self.centralwidget.progressBar_file_process_progress.setFormat(_translate("MainWindow", "%p% Completed"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSelect_Input_Directory.setText(_translate("MainWindow", "Input Directory"))
        self.actionSelect_DEM_Directory.setText(_translate("MainWindow", "DEM Directory"))
        self.actionOutput_Directory.setText(_translate("MainWindow", "Output Directory"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout_NRSC.setText(_translate("MainWindow", "About NRSC"))
        self.actionAbout_OrthoRectifiction.setText(_translate("MainWindow", "About OrthoRectifiction"))

    def setInputDirectory(self):
        self.input_directory_path = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Open Directory", "/home", QtWidgets.QFileDialog.ShowDirsOnly|QtWidgets.QFileDialog.DontResolveSymlinks);
        #print("the input directory path is",self.input_directory_path)
        if(self.input_directory_path):
            self.zip_files = [x for x in os.listdir(self.input_directory_path) if x.endswith('.zip')]
            self.pushButton_start.setEnabled(True)
        self.populateList()

    def setDEMDirectory(self):
        self.dem_directory_path = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Open Directory", "/home", QtWidgets.QFileDialog.ShowDirsOnly|QtWidgets.QFileDialog.DontResolveSymlinks);

    def setOutputDirectory(self):
        self.output_directory_path = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Open Directory", "/home", QtWidgets.QFileDialog.ShowDirsOnly|QtWidgets.QFileDialog.DontResolveSymlinks);

    def populateList(self):
        self.listWidget_zip_files.clear()
        #print("the current working directory",os.getcwd())
        for zip_file in self.zip_files:
            #print("the zip file is",zip_file)
            list_item = QtWidgets.QListWidgetItem(self.listWidget_zip_files)
            list_item.setText(zip_file)
        lbl_txt = "0 out of " + str(len(self.zip_files)) + " archives processed"
        self.label_zip_processed_status.setText(lbl_txt)
        self.label_tiff_processed_status.setText("Click Start to Begin Orthorectification")

    def updateZipProgress(self, value, count):
        self.centralwidget.progressBar_zip_process_progress.setValue(value)
        self.listWidget_zip_files.item(count-1).setBackground(QtGui.QColor('#008000'))
        if count != len(self.zip_files):
            self.listWidget_zip_files.item(count).setBackground(QtGui.QColor('#000080'))

    def updateFileProgress(self, value):
        self.centralwidget.progressBar_file_process_progress.setValue(value)

    def thread_start_init(self):
        for i in range (len(self.zip_files)):
            self.listWidget_zip_files.item(i).setBackground(QtGui.QColor('#800000'))
        self.listWidget_zip_files.item(0).setBackground(QtGui.QColor('#000080'))
        self.pushButton_start.setEnabled(False)
        self.pushButton_stop.setDisabled(False)

    def stop_pushed(self):
        self.process_thread.terminate()
        self.file_process_counter = 0
        self.zip_process_counter = 0
        self.pushButton_start.setEnabled(True)
        self.pushButton_stop.setDisabled(True)

    def check_cwd_progress(self):
        log_file = self.input_directory_path+'/log.txt'
        if os.path.exists(log_file):
            lfile = open(log_file, 'r')
            log = lfile.readline()
            self.zip_process_counter, self.file_process_counter = log.split(' ')
        else:
            self.zip_process_counter = 0
            self.file_process_counter = 0

class orthorectifyProgressThread(QThread):
    thread_start = pyqtSignal()           
    zip_progressed = pyqtSignal(int,int)  
    file_progressed = pyqtSignal(int) 
    message=pyqtSignal()
    fileexist=pyqtSignal()
    zipexist=pyqtSignal()
    quit=pyqtSignal()
    quitmsg = True
    merge = True
    def __init__(self,parent):
        QThread.__init__(self)
        self.parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        self.zipbtnreply=0
        self.thread_start.emit()
        progress = 0
        self.parent.file_process_counter = 0
        temp_directory_path = self.parent.input_directory_path + '/temp/'
        self.zipsuccess=True
        self.merge = True
        for file in self.parent.zip_files:
            #self.zipsuccess=True
            self.merge = True
            print("the file is",file)
            print("the temp directory path is",temp_directory_path)
            print("the result is",os.path.isfile(file))
            print("the current working directory",os.getcwd())
            os.chdir(self.parent.input_directory_path)
            if(os.path.exists(self.parent.input_directory_path )==False):
                os.makedirs(temp_directory_path)
                print("the result in if is",os.path.isfile(file))
            if(os.path.isfile(file)==False):
                print("in file")
                self.zipflag=True
                self.zipsuccess=False
                self.zipbtn=""
                self.zipexist.emit()
                print("the self.zipbtnreply is",self.zipbtnreply)
                while(self.zipflag):
                    print("in while thread sleep")
                    self.sleep(1)
                if(self.zipbtnreply==1):
                    print("in skipping")
                    self.zipflag=False
                elif(self.zipbtnreply==0):
                    self.quit.emit()
                    self.quitmsg=False
                    self.zipflag=False

            if(self.zipsuccess==True):
                print("in zipsuccess")
                zip_path = self.parent.input_directory_path + '/' + file
                zip_ref = zipfile.ZipFile(zip_path)
                zip_ref.extractall(temp_directory_path)
                print(temp_directory_path)
                zip_name = self.parent.listWidget_zip_files.item(self.parent.zip_process_counter).text()[0:-4]
                print(zip_name)
                file_progress = 0   
                il_bands = []
                print("the result is",os.path.isdir(temp_directory_path+zip_name))
                if(os.path.isdir(temp_directory_path+zip_name)==False):
                    self.flag=True;
                    self.message.emit()
                    while(self.flag):
                        self.sleep(1)    
                else:
                    for file in os.listdir(temp_directory_path+zip_name):
                        quit=True
                        if file.endswith('.tif'):
                            il_bands.append(file)
                    file_count = len(il_bands)
                    outpath = self.parent.output_directory_path+'/'+zip_name
                    if(os.path.isdir(outpath)==False):
                        os.makedirs(outpath)
                    self.file_progressed.emit(0)
                    i=2
                    temp=True
                    self.fileflag=True
                    self.btnreply=""
                    while(temp):
                        imgname=""
                        imgname="BAND"+str(i)+"_RPC.tif"
                        if any(imgname in s for s in il_bands):
                            i+=1;
                            tempoutput=True
                            if(i>5):
                                temp=False       
                        else:
                            tempoutput=False
                            self.fileexist.emit()
                            while(self.fileflag):                
                                self.sleep(1)
                            if(self.btnreply==1):        
                                temp=False
                                self.fileflag=True
                            else:
                                self.quit.emit()
                                temp=False
                                self.zipsuccess=False
                                self.quitmsg=False
                                self.fileflag=True
                    if(tempoutput==True):
                        for file in il_bands:
                            band_path = temp_directory_path + zip_name +'/'+ file
                            self.parent.file_process_counter += 1
                            print(band_path)
                            self.parent.label_tiff_processed_status.setText("Processing " + file + "("+str(self.parent.file_process_counter)+"/"+str(file_count)+")")
                            time.sleep(0.3)
                            ortho = ortho_process.OrthoRectification()
                            ortho.OrthoRectifyEPSG(band_path, outpath)
                            file_progress =  int(float(self.parent.file_process_counter)/file_count*100)
                            self.file_progressed.emit(file_progress)
                            os.remove(band_path)
                if(self.quitmsg==True):
                    self.parent.file_process_counter = 0
                    self.parent.zip_process_counter += 1
                    self.parent.label_zip_processed_status.setText(str(self.parent.zip_process_counter)+" out of " + str(len(self.parent.zip_files)) + " archives processed")
                    progress = int(float(self.parent.zip_process_counter)/len(self.parent.zip_files)*100)
self.zip_progressed.emit(progress,self.parent.zip_process_counter)
            else:
                self.zipsuccess=True
                self.parent.file_process_counter = 0
                if(len(self.parent.zip_files)==0):
                    self.parent.zip_process_counter=0
                else:
                    self.parent.zip_process_counter += 1
self.parent.label_zip_processed_status.setText(str(self.parent.zip_process_counter)+" out of " + str(len(self.parent.zip_files)) + " archives processed")
                if(len(self.parent.zip_files)!=0):
                    progress = int(float(self.parent.zip_process_counter)/len(self.parent.zip_files)*100)
                    self.zip_progressed.emit(progress,self.parent.zip_process_counter)
            if(self.merge):
                ortho.MergeBands(outpath, il_bands)                     shutil.rmtree(temp_directory_path)
        self.parent.zip_process_counter = 0
