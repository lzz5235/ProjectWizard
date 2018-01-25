#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-6-14
概述：工程信息
'''
from PyQt4.QtGui import QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QCheckBox,QComboBox,QSpacerItem,QSizePolicy
from PyQt4.QtCore import QStringList,SIGNAL
import app
import os
import configuration

styleSheet = \
             "QComboBox{border-radius:3px;color:#333333;font-family:'微软雅黑';font-size:14px;border-radius:3px;Width:440px;Height:25px;border-image:url(:/image/下拉框_normal.png);border-style:none;}" \
             "QComboBox::drop-down{color:#333333;font-family:'微软雅黑';font-size:14px;border-style:none;}" \
             "QLineEdit{border-radius:3px;color:#333333;font-family:'微软雅黑';font-size:14px;Width:440px;Height:25px;Width:100px;background-color:#ffffff;border: 1px solid gray groove;}" \
             "QLabel{Height:25px;font-weight:bold;font-family:'微软雅黑';font-size:14px;color:#333333;}" \
             "QCheckBox{spacing:10px;spacing:10px;color:#333333;font-family:'微软雅黑';font-size:14px;font-weight:bold;}" \
             "QCheckBox::indicator{Width:16px;Height:16px;border-image:url(:/image/选择_normal.png);}" \
             "QCheckBox::indicator:unchecked{border-image:url(:/image/选择_normal.png);}" \
             "QCheckBox::indicator:unchecked:hover{border-image:url(:/image/选择_hover.png);}" \
             "QCheckBox::indicator:unchecked:pressed{border-image:url(:/image/选择_hover.png);}" \
             "QCheckBox::indicator:checked{border-image:url(:/image/选择_pressed.png);}" \
             "QCheckBox::indicator:checked:hover{border-image:url(:/image/选择_pressed.png);}" \
             "QCheckBox::indicator:checked:pressed{border-image:url(:/image/选择_pressed.png);}"

class BaseInfoPage(QWizardPage):

    def __init__(self):
        super(BaseInfoPage,self).__init__()

        self.setTitle('工程配置')
        self.setSubTitle('设置工程的参数')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        self.project_name = ""
        self.project_dir = ""
        self.completed = False

        row1 = QHBoxLayout()
        lable1 = QLabel('工程名称:')
        self.et_project_name = QLineEdit()
        self.et_project_name.setTextMargins(-6,0,0,0)
        self.et_project_name.textChanged.connect(self.on_text_changed)
        row1.addWidget(lable1)
        row1.addWidget(self.et_project_name)

        # row2 = QHBoxLayout()
        # lable2 = QLabel('工程位置：')
        # self.et_project_location = QLineEdit()
        # self.et_project_location.textChanged.connect(self.on_text_changed)
        # self.et_project_location.setReadOnly(True)
        # btn_location = QPushButton('...')
        # btn_location.setFixedWidth(50)
        # btn_location.clicked.connect(self.getSavePath)
        # row2.addWidget(lable2)
        # row2.addWidget(self.et_project_location)
        # row2.addWidget(btn_location)

        row3 = QHBoxLayout()
        lable3 = QLabel('源模板:   ')
        self.cb_wizard_type = QComboBox()
        items = QStringList()
        for key in app.g_templates:
            items.append(key)
        self.cb_wizard_type.addItems(items)
        row3.addWidget(lable3)
        row3.addWidget(self.cb_wizard_type)

        row4 = QHBoxLayout()
        lable4 = QLabel('平台类型:')
        checkboxLayout = QHBoxLayout()
        self.cb_pt_win = QCheckBox('Win')
        self.cb_pt_linux = QCheckBox('Linux')
        checkboxLayout.addWidget(self.cb_pt_win)
        checkboxLayout.addWidget(self.cb_pt_linux)
        row4.addWidget(lable4)
        row4.addLayout(checkboxLayout)

        row6 = QHBoxLayout()
        self.cb_pt_version = QComboBox()
        items_pt_version = QStringList()
        items_pt_version.append('x86')
        items_pt_version.append('x64')
        self.cb_pt_version.addItems(items_pt_version)
        row6.addWidget(QLabel('平台级别:'))
        row6.addWidget(self.cb_pt_version)

        row5 = QHBoxLayout()
        lable5 = QLabel('组件类型:')
        self.cb_component_type = QComboBox()
        items_component_type = QStringList()
        items_component_type.append('服务')
        items_component_type.append('窗口')
        self.cb_component_type.addItems(items_component_type)
        self.registerField('component_type*', self.cb_component_type)
        self.cb_component_type.currentIndexChanged.connect(self.on_currentIndex_Changed)
        row5.addWidget(lable5)
        row5.addWidget(self.cb_component_type)

        space1 = QSpacerItem(40, 28, QSizePolicy.Expanding)
        row7 = QHBoxLayout()
        lable7 = QLabel('翻译文件:')
        self.chkb_transFile = QCheckBox()
        row7.addWidget(lable7)
        row7.addWidget(self.chkb_transFile)
        row7.addSpacerItem(space1)

        space2 = QSpacerItem(40, 28, QSizePolicy.Expanding)
        row8 = QHBoxLayout()
        lable8 = QLabel('资源文件:')
        self.chkb_resourceFile = QCheckBox()
        row8.addWidget(lable8)
        row8.addWidget(self.chkb_resourceFile)
        row8.addSpacerItem(space2)

        rootLayout.addLayout(row1)
        rootLayout.addSpacing(10)
        rootLayout.addLayout(row3)
        rootLayout.addSpacing(10)
        rootLayout.addLayout(row5)
        rootLayout.addSpacing(10)
        rootLayout.addLayout(row6)
        rootLayout.addSpacing(10)
        rootLayout.addLayout(row7)
        rootLayout.addSpacing(10)
        rootLayout.addLayout(row8)
        rootLayout.addSpacing(31)

        self.setLayout(rootLayout)
        self.setStyleSheet(styleSheet)

    def initializePage(self):
        super(BaseInfoPage, self).initializePage()
        if app.g_configurations.initialized:
            self.et_project_name.setText(app.g_configurations.project_name)

            self.cb_pt_win.setChecked(app.g_configurations.platform_type & configuration.PT_WIN32)
            self.cb_pt_linux.setChecked(app.g_configurations.platform_type & configuration.PT_LINUX)

            if app.g_configurations.platform_version == "x86_64":
                self.cb_pt_version.setCurrentIndex(1)
            else:
                self.cb_pt_version.setCurrentIndex(0)

            index = self.cb_wizard_type.findText(app.g_configurations.template_source)
            self.cb_wizard_type.setCurrentIndex(index)

            if app.g_configurations.component_type == "server":
                self.cb_component_type.setCurrentIndex(0)
            else:
                self.cb_component_type.setCurrentIndex(1)

            if app.g_configurations.translateFile == "True":
                self.chkb_transFile.setChecked(True)
            if app.g_configurations.resourcesFile == "True":
                self.chkb_resourceFile.setChecked(True)

    # def getSavePath(self):
    #     path = QFileDialog.getExistingDirectory()
    #     self.et_project_location.setText(path)

    def test_completed(self):
        project_name = self.et_project_name.text().trimmed()
        #project_dir = self.et_project_location.text().trimmed()
        #return not project_name.isEmpty() and not project_dir.isEmpty()
        return not project_name.isEmpty()

    def on_text_changed(self,text):
        self.isComplete()

    def on_currentIndex_Changed(self,text):
        pass


    def isComplete(self):
        ret = self.test_completed()
        if ret != self.completed:
            self.completed = ret
            self.emit(SIGNAL("completeChanged()"))
        return ret

    def validatePage(self):
        project_name = self.et_project_name.text().trimmed()
        #project_dir = self.et_project_location.text().trimmed()
        wizard_template = self.cb_wizard_type.currentText()
        component_type = self.cb_component_type.currentIndex()

        platform_type = 0
        if self.cb_pt_win.isChecked():
            platform_type |= configuration.PT_WIN32
        if self.cb_pt_linux.isChecked():
            platform_type |= configuration.PT_LINUX

        if self.cb_pt_version.currentIndex() == 1:
            app.g_configurations.platform_version = "x86_64"
        else:
            app.g_configurations.platform_version = "x86_32"

        app.g_configurations.project_name = app.QString2str(project_name)
        #app.g_configurations.project_location = app.QString2str(project_dir)
        app.g_configurations.template_source = app.QString2str(wizard_template)
        app.g_configurations.platform_type = platform_type

        if self.chkb_transFile.isChecked():
            app.g_configurations.translateFile = "True"
        else:
            app.g_configurations.translateFile = "False"

        if self.chkb_resourceFile.isChecked():
            app.g_configurations.resourcesFile = "True"
        else:
            app.g_configurations.resourcesFile = "False"

        if component_type == 0:
            app.g_configurations.component_type = "server"
        elif component_type == 1:
            app.g_configurations.component_type = "window"

        template_name = app.g_configurations.template_source
        template_dir = app.g_pwd + os.sep + 'templates' + os.sep + template_name.encode('utf-8')
        with open(template_dir + os.sep + 'config.json', 'r') as f:
            app.g_configurations.config_content = f.read()
        return True