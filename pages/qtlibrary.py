#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-6-14
概述：qt库选择
'''

from PyQt4.QtGui import QWizardPage,QVBoxLayout,QCheckBox,QGridLayout
from PyQt4.QtCore import Qt
import app

sheetstyle = "QCheckBox{spacing:10px;color:#333333;font-family:'微软雅黑';font-size:14px;font-weight:bold;}" \
             "QCheckBox::indicator{Width:16px;Height:16px;border-image:url(:/image/选择_normal.png);}" \
             "QCheckBox::indicator:unchecked{border-image:url(:/image/选择_normal.png);}" \
             "QCheckBox::indicator:unchecked:hover{border-image:url(:/image/选择_hover.png);}" \
             "QCheckBox::indicator:unchecked:pressed{border-image:url(:/image/选择_hover.png);}" \
             "QCheckBox::indicator:checked{border-image:url(:/image/选择_pressed.png);}" \
             "QCheckBox::indicator:checked:hover{border-image:url(:/image/选择_pressed.png);}" \
             "QCheckBox::indicator:checked:pressed{border-image:url(:/image/选择_pressed.png);}"

class QtLibraryPage(QWizardPage):

    def __init__(self):
        super(QtLibraryPage,self).__init__()
        self.setTitle('Qt模块')
        self.setSubTitle('设置Qt的模块引用')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(10, 10, 10, 10)

        self.gLayout = QGridLayout()
        self.checkboxs = []

        rootLayout.addLayout(self.gLayout)
        self.setLayout(rootLayout)
        self.setStyleSheet(sheetstyle)

    def initializePage(self):
        exsits = []
        self.checkboxs = []
        for qtlib in app.g_configurations.qt_libs:
            exsits.append(qtlib['name'])

        index = 0
        for moudel in app.g_qt_library:
            checkBox = QCheckBox(moudel['name'])
            if app.g_configurations.initialized:
                if moudel['name'] in exsits:
                    checkBox.setCheckState(Qt.Checked)
                else:
                    checkBox.setCheckState(Qt.Unchecked)
            else:
                if moudel['refer']:
                    checkBox.setCheckState(Qt.Checked)
                else:
                    checkBox.setCheckState(Qt.Unchecked)
            row = index / 3
            offset = index % 3
            self.gLayout.addWidget(checkBox, row, offset)
            self.checkboxs.append(checkBox)
            index += 1

    def validatePage(self):
        librarys = []
        for i in range(len(self.checkboxs)):
            if self.checkboxs[i].checkState() == 2:
                librarys.append(app.g_qt_library[i])

        app.g_configurations.qt_libs = librarys
        return True