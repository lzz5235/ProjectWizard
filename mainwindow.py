#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-6-14
概述：程序主窗口
'''

import os
import copy
import json
import app
import wizard
import configuration
import AboutDlg
import ProjectWizard  # 资源

from AboutDlg import AboutDlg
from PyQt4 import QtCore,QtGui
from configuration import Configuration
from PyQt4.QtCore import QStringList,QFileInfo,QDir,QUrl
from PyQt4.QtGui import QDialog,QVBoxLayout,QHBoxLayout,QListWidget,QWidget,QTreeWidget,QPushButton,QLabel, \
    QTreeWidgetItem,QAbstractItemView,QLineEdit,QFileDialog,QGroupBox,QMessageBox,QStatusBar,QIcon, \
    QAction,QPixmap,QToolButton,QToolBar,QSizePolicy,QListWidgetItem,QDesktopServices

class mainwindow(QtGui.QMainWindow):
    '''主窗体'''

    def __init__(self):
        super(mainwindow,self).__init__()
        self.setWindowTitle('组件设计工具')
        self.setWindowIcon(QIcon(':/image/组件设计工具.png'))

        self.setMinimumWidth(1024)
        self.setMinimumHeight(800)

        self.showMaximized()
        self.menuBar().show()
        self.createMenus()

        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        labelSizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        editSizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        cwVLayout = QVBoxLayout()
        cwHLayout = QHBoxLayout()

        lLayout = QVBoxLayout()
        rLayout = QVBoxLayout()
        self.lw = QListWidget()
        self.lw.setSelectionMode(QAbstractItemView.SingleSelection )

        lLayout.addWidget(self.lw)
        self.lw.itemSelectionChanged.connect(self.on_select)

        lGroup = QGroupBox('项目列表')
        lGroup.setLayout(lLayout)
        cwHLayout.addWidget(lGroup,2)
        lGroup.setContentsMargins(0,12,0,22)


        tLayout = QVBoxLayout()
        bLayout = QHBoxLayout()

        self.tGroup = QGroupBox('配置信息')
        self.bGroup = QGroupBox('生成代码')
        self.tGroup.setLayout(tLayout)
        self.tGroup.setEnabled(False)
        self.bGroup.setLayout(bLayout)
        self.bGroup.setEnabled(False)


        cwHLayout.addWidget(self.tGroup, 8)
        cwVLayout.addLayout(cwHLayout)
        cwVLayout.addWidget(self.bGroup)

        self.tw_config = QTreeWidget()
        headerLabels = QStringList()
        headerLabels.append('       项目')
        headerLabels.append('       值')
        self.tw_config.setHeaderLabels(headerLabels)
        self.tw_config.setColumnWidth(0,312)
        self.tw_config.setColumnWidth(1,660)
        thLayout = QHBoxLayout()
        thLayout.setContentsMargins(0,6,0,0)
        thLayout.addSpacing(10)
        modify_btn = QPushButton('')#修改
        modify_btn.setObjectName('modify_btn')
        modify_btn.clicked.connect(self.on_modify)
        del_btn = QPushButton('')#删除
        del_btn.setObjectName('del_btn')
        del_btn.clicked.connect(self.on_del)
        thLayout.addWidget(modify_btn)
        thLayout.addWidget(del_btn)
        thLayout.addStretch(0)

        tLayout.addLayout(thLayout)
        tLayout.addWidget(self.tw_config)


        bhLayout = QHBoxLayout()

        lable1 = QLabel('工程名称：')
        lable1.setSizePolicy(labelSizePolicy)
        self.et_project_name = QLineEdit()
        self.et_project_name.setSizePolicy(editSizePolicy)
        bhLayout.addWidget(lable1)
        bhLayout.addWidget(self.et_project_name)
        bhLayout.addSpacing(16)

        lable2 = QLabel('工程位置：')
        lable2.setSizePolicy(labelSizePolicy)
        self.et_project_location = QLineEdit()
        self.et_project_location.setReadOnly(True)
        self.et_project_location.setSizePolicy(editSizePolicy)
        btn_location = QPushButton('')#打开
        btn_location.setObjectName('btn_location')
        btn_location.setSizePolicy(labelSizePolicy)
        btn_location.clicked.connect(self.getProjectLocation)
        bhLayout.addWidget(lable2)
        bhLayout.addWidget(self.et_project_location)
        bhLayout.addSpacing(10)
        bhLayout.addWidget(btn_location)

        #bhLayout.addStretch(0)
        gen_btn = QPushButton('')  # 生成
        gen_btn.setObjectName('gen_btn')
        gen_btn.setSizePolicy(labelSizePolicy)
        gen_btn.clicked.connect(self.on_gen)
        bhLayout.addSpacing(45)
        bhLayout.addWidget(gen_btn)

        bLayout.addLayout(bhLayout)
        bLayout.setContentsMargins(10,24,22,34)

        statusBar = self.statusBar()
        sBH = QHBoxLayout()
        copyright = QLabel('')
        copyright.setAlignment(QtCore.Qt.AlignCenter)
        copyright.setStyleSheet("color:#acacac")
        statusBar.setMinimumHeight(30)
        statusBar.addWidget(copyright,10)

        cw = QWidget()
        cw.setLayout(cwVLayout)
        self.setCentralWidget(cw)
        self._initByConfig()
        self.setMinimumSize(400,200)

    def _initByConfig(self):
        '''初始化'''
        pass

    def createMenus(self):
        '''创建菜单'''
        self.ToolBar = self.addToolBar('')

        self.ToolBar.setMinimumHeight(54)

        newBtn = QToolButton()
        newBtn.setText('创建项目')
        newBtn.setIcon(QIcon(':/image/创建项目.png'))
        newBtn.setToolButtonStyle(3)
        newBtn.setFixedWidth(99)

        OpenBtn = QToolButton()
        OpenBtn.setText('打开项目')
        OpenBtn.setIcon(QIcon(':/image/打开.png'))
        OpenBtn.setToolButtonStyle(3)
        OpenBtn.setFixedWidth(99)

        AboutBtn = QToolButton()
        AboutBtn.setText('关于')
        AboutBtn.setIcon(QIcon(':/image/关于.png'))
        AboutBtn.setToolButtonStyle(3)
        AboutBtn.setFixedWidth(99)

        HelpBtn = QToolButton()
        HelpBtn.setText('帮助')
        HelpBtn.setIcon(QIcon(':/image/帮助.png'))
        HelpBtn.setToolButtonStyle(3)
        HelpBtn.setFixedWidth(99)

        newBtn.clicked.connect(self.on_new)
        OpenBtn.clicked.connect(self.on_open)
        AboutBtn.clicked.connect(self.on_about)
        HelpBtn.clicked.connect(self.on_help)

        self.ToolBar.addWidget(newBtn)
        self.ToolBar.addWidget(OpenBtn)
        self.ToolBar.addWidget(AboutBtn)
        self.ToolBar.addWidget(HelpBtn)
        self.ToolBar.setMovable(False)
        self.ToolBar.setVisible(True)

    def on_help(self):
        app.g_pwd = os.getcwd()
        if not (QtGui.QDesktopServices.openUrl(QUrl.fromLocalFile(app.g_pwd + os.sep + 'image' + os.sep + 'help.pdf'))):
            print app.g_pwd + os.sep +'/image/help.pdf'
            QMessageBox.critical(None,"Failure","Cannot open help manual")

    def on_about(self):
        abt = AboutDlg()
        abt.exec_()

    def on_new(self):
        '''新建向导'''
        app.g_configurations = Configuration()  # 用来渲染的配置数据
        dlg = wizard.MyWizard()
        if dlg.exec_():
            app.g_configurations.initialized = True
            app.g_projects.append(app.g_configurations)
            content = app.g_configurations.toJson()
            self.path = QFileDialog.getSaveFileName(self,"选择模板保存的路径",
                                               app.g_pwd + os.sep + "configurations" + os.sep + app.g_configurations.project_name.encode('utf-8') + ".json"
                                               ,"Config (*.json)")
            fileInfo = QFileInfo(self.path)
            if not self.path.isEmpty():
                path = app.QString2str(self.path)
                with open(path,'w+') as f:
                    f.write(content)
                self.addConfig(fileInfo.baseName(),fileInfo.filePath(),content)
                #self.lw.addItem(app.g_configurations.project_name)

    def getProjectLocation(self):
        '''获取项目路径'''
        path = QFileDialog.getExistingDirectory()
        path = QDir.fromNativeSeparators(path)
        self.et_project_location.setText(path)

    def on_open(self):
        '''打开现有配置'''
        fileName = QFileDialog.getOpenFileName(self,"选择现有模板",app.g_pwd + os.sep + "configurations","Config (*.json)")
        if fileName.isEmpty():
            return
        self.path = fileName
        with open(app.QString2str(fileName), 'r') as f:
            content = f.read()

        fileInfo = QFileInfo(fileName)
        if not fileInfo.exists():
            return
        config = Configuration()
        config.fromJson(content)
        config.allone_dir = os.getenv('ALLONEDIR','../..').replace('\\','/')
        self.addConfig(fileInfo.baseName(),fileInfo.filePath(),content)
        self.on_select()

    def on_del(self):
        self.tw_config.clear()
        self.bGroup.setEnabled(False)
        self.tGroup.setEnabled(False)
        index = self.lw.currentRow()
        self.lw.takeItem(index)

    def on_select(self):
        '''选取配置'''
        item = self.lw.currentItem()
        if item != None:
            content = item.data(QtCore.Qt.UserRole).toString()
            config = Configuration()
            config.fromJson(app.QString2str(content))
            self.currentConfig = config
            self.showConfigInfo(self.currentConfig)
            self.bGroup.setEnabled(True)
            self.path = item.data(QtCore.Qt.UserRole+1).toString()

        # index = self.lw.currentRow()
        # if index < len(app.g_projects):
        #     self.currentConfig = app.g_projects[index]
        #     self.showConfigInfo(self.currentConfig)
        #     self.bGroup.setEnabled(True)

    def addConfig(self,fileName,filePath,config):
        item = QListWidgetItem(fileName)
        item.setData(QtCore.Qt.UserRole,config)
        item.setData(QtCore.Qt.UserRole+1,filePath)
        self.lw.addItem(item)
        self.lw.setCurrentRow(0)

    def showConfigInfo(self,cf):
        '''显示配置信息'''
        self.tw_config.clear()
        self.et_project_name.setText(cf.project_name)
        self.et_project_location.setText(cf.project_location)
        sr = QStringList()
        sr.append('信息')
        root1 = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('Qt库')
        root2 = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('模块')
        root3a = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('第三方库')
        root3b = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('接口')
        root4 = QTreeWidgetItem(sr)

        self.tw_config.addTopLevelItem(root1)
        self.tw_config.addTopLevelItem(root2)
        self.tw_config.addTopLevelItem(root3a)
        self.tw_config.addTopLevelItem(root3b)
        self.tw_config.addTopLevelItem(root4)

        sr1c00 = QStringList()
        sr1c00.append("项目名称")
        sr1c00.append(cf.project_name)
        r1c00 = QTreeWidgetItem(sr1c00)
        root1.addChild(r1c00)

        # sr1c0 = QStringList()
        # sr1c0.append("项目位置")
        # sr1c0.append(cf.project_location)
        # r1c0 = QTreeWidgetItem(sr1c0)
        # root1.addChild(r1c0)

        sr1c1 = QStringList()
        sr1c1.append("组件类型")
        sr1c1.append(cf.component_type)
        r1c1 = QTreeWidgetItem(sr1c1)
        root1.addChild(r1c1)

        sr1c2 = QStringList()
        sr1c2.append("源模板")
        sr1c2.append(cf.template_source)
        r1c2 = QTreeWidgetItem(sr1c2)
        root1.addChild(r1c2)

        sr1c3 = QStringList()
        sr1c3.append("平台类型")
        tmp_pt = ""
        if cf.platform_type & configuration.PT_WIN32:
            tmp_pt += "win32;"
        if cf.platform_type & configuration.PT_LINUX:
            tmp_pt += "linux"

        sr1c3.append(tmp_pt)
        r1c3 = QTreeWidgetItem(sr1c3)
        root1.addChild(r1c3)

        sr1c4 = QStringList()
        sr1c4.append("平台级别")
        sr1c4.append(cf.platform_version)
        r1c4 = QTreeWidgetItem(sr1c4)
        root1.addChild(r1c4)


        sr1c5 = QStringList()
        sr1c5.append("资源文件")
        if cf.resourcesFile == "True":
            sr1c5.append("添加")
        else:
            sr1c5.append("未添加")
        r1c5 = QTreeWidgetItem(sr1c5)
        root1.addChild(r1c5)


        sr1c6 = QStringList()
        sr1c6.append("翻译文件")
        if cf.translateFile == "True":
            sr1c6.append("添加")
        else:
            sr1c6.append("未添加")
        r1c6 = QTreeWidgetItem(sr1c6)
        root1.addChild(r1c6)

        for qt in cf.qt_libs:
            sr2 = QStringList()
            sr2.append(qt['name'])
            sr2.append(qt['qt'])
            r2 = QTreeWidgetItem(sr2)
            root2.addChild(r2)

        for module in cf.modules:
            sr3a = QStringList()
            sr3a.append(module['name'])
            sr3a.append(module['description'])
            r3a = QTreeWidgetItem(sr3a)
            root3a.addChild(r3a)

        # sr3b = QStringList()
        # sr3b.append('ALLONE_DIR')
        # sr3b.append(os.getenv('ALLONEDIR','../..')) # 第二个参数是默认值
        # r3b = QTreeWidgetItem(sr3b)
        # root3b.addChild(r3b)
        for info in cf.thirdpart_lib:
            sr3b = QStringList()
            sr3b.append(info['libname'])
            sr3b.append(info['libpath'])
            r3b = QTreeWidgetItem(sr3b)
            root3b.addChild(r3b)

        for key in cf.interfaces.keys():
            sr4 = QStringList()
            sr4.append(key)
            if cf.interfaces[key]:
                sr4.append('实现')
            else:
                sr4.append('未实现')
            r4 = QTreeWidgetItem(sr4)
            root4.addChild(r4)
        self.tw_config.expandAll()
        self.tw_config.header().resizeSection(0,300)
        self.tGroup.setEnabled(True)

    def on_modify(self):
        '''修改配置'''
        if self.currentConfig:
            app.g_configurations = copy.copy(self.currentConfig)
            dlg = wizard.MyWizard()
            if dlg.exec_():
                item = self.lw.currentItem()
                if item != None:
                    content = app.g_configurations.toJson()
                    item.setData(QtCore.Qt.UserRole, content)
                    path = item.data(QtCore.Qt.UserRole+1).toString()
                    if not path.isEmpty():
                        path = app.QString2str(path)
                        with open(path, 'w+') as f:
                            f.write(content)
                    self.on_select()

    def on_gen(self):
        '''生成工程'''
        if not self.currentConfig:
            return

        #获取工程名及有效路径
        project_name = self.et_project_name.text()
        project_location = self.et_project_location.text()
        qdir = QDir(project_location)
        if not qdir.exists():
            if not qdir.mkpath(project_location):
                QMessageBox.warning(self, '警告', '路径无效！')
                return
        project_location = qdir.absolutePath()
        if not project_location.endsWith('/') and not project_location.endsWith('\\'):
            project_location += os.sep
            project_location.replace('\\','/')
        if project_name.isEmpty() or project_location.isEmpty():
            QMessageBox.warning(self, '警告', '项目名称或路径不能为空！')
            return

        self.currentConfig.project_name = app.QString2str(project_name)
        self.currentConfig.project_location = app.QString2str(project_location)

        content = self.currentConfig.toJson()
        fileInfo = QFileInfo(self.path)
        if not self.path.isEmpty():
            path = app.QString2str(self.path)
            with open(path, 'w+') as f:
                f.write(content)
        item = self.lw.currentItem()
        item.setData(QtCore.Qt.UserRole, content)

        template_name = self.currentConfig.template_source
        template_dir = app.g_pwd + os.sep + 'templates' + os.sep + template_name.encode('utf-8')
        with open(template_dir + os.sep + 'config.json', 'r') as f:
            self.currentConfig.config_content = f.read()
        ret_json = app.render(self.currentConfig.config_content, config=self.currentConfig)
        self.currentConfig.config = json.loads(ret_json)
        for file in self.currentConfig.config['files']:
            sourcepath = template_dir + os.sep + file['source'].encode('utf-8')
            targetdir = self.currentConfig.project_location + self.currentConfig.project_name
            targetpath = targetdir + os.sep + file['target']
            fi = QFileInfo(targetpath)
            qdir = fi.absoluteDir()
            if not qdir.exists():
                qdir.mkpath(fi.absolutePath())
            with open(sourcepath, 'r') as f:
                content = f.read()
                content = app.render(content, config=self.currentConfig) #渲染文件
            with open(targetpath, 'w+') as f:
                f.write(content.encode('utf-8'))
        QMessageBox.information(self,'提示','生成成功！')