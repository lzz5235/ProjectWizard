#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-11-11
概述：关于窗口
'''

import app
from PyQt4 import QtGui
from PyQt4.QtGui import *


styleSheet = "QPushButton#btn_ok{Width:110px;Height:28px;border-image:url(:/image/确定_normal.png);}" \
             "QPushButton#btn_ok:!enabled{Width:110px;Height:28px;border-image:url(:/image/确定_disable.png);}" \
             "QPushButton#btn_ok:hover{Width:110px;Height:28px;border-image:url(:/image/确定_hover.png);}" \
             "QPushButton#btn_ok:pressed{Width:110px;Height:28px;border-image:url(:/image/确定_pressed.png);}" \
             "QGroupBox{font:16px;font-family:'微软雅黑';color:#000000;border-color:#cccccc;}" \
             "QLabel{font:14px;font-family:'微软雅黑';color:#333333;font-weight:bold;}" \
             "QDialog{color:#dddddd}"

class AboutDlg(QtGui.QDialog):
    def __init__(self):
        super(AboutDlg, self).__init__()
        self.setWindowTitle('关于')
        self.setWindowIcon(QIcon(':/image/关于.png'))
        self.setMinimumSize(558,300)

        gbox1 = QGroupBox()
        gbox1.setTitle("产品信息")
        gbox1.setFixedWidth(538)
        gbox1.setFixedHeight(84)
        gbox1.setContentsMargins(15,15,15,15)
        vblay1 = QVBoxLayout()
        label1 = QLabel('')
        label2 = QLabel('')
        vblay1.addWidget(label1)
        vblay1.addWidget(label2)
        gbox1.setLayout(vblay1)

        gbox2 = QGroupBox()
        gbox2.setTitle("许可信息")
        gbox2.setFixedWidth(538)
        gbox2.setFixedHeight(84)
        gbox2.setContentsMargins(15, 15, 15, 15)
        vblay2 = QVBoxLayout()
        label3 = self.getLicenseType()
        label4 = QLabel('过期: ' + app.g_LicenseInfo )
        vblay2.addWidget(label3)
        vblay2.addWidget(label4)
        gbox2.setLayout(vblay2)

        hblay = QHBoxLayout()
        btn = QPushButton('')
        btn.setObjectName("btn_ok")
        btn.clicked.connect(self.on_close)
        space = QSpacerItem(30, 5, QSizePolicy.Expanding)
        hblay.addSpacerItem(space)
        hblay.addWidget(btn)

        vblayt = QVBoxLayout()
        copyright = QLabel('')
        vblayt.addWidget(gbox1)
        vblayt.addWidget(gbox2)
        vblayt.addWidget(copyright)
        vblayt.addLayout(hblay)

        self.setStyleSheet(styleSheet)
        self.setLayout(vblayt)


    def getLicenseType(self):
        flag = app.g_LicenseType
        if (flag == 0):
            return QLabel('状态: 开发版')
        elif flag == 1:
            return QLabel('状态: 部署版')
        elif flag == 2:
            return QLabel('状态: 无限制')

    def on_close(self):
        self.close()