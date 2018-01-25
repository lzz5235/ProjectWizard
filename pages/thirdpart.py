#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-12-14
概述：第三方库选择
'''

import app
import os

from PyQt4.QtGui import QTableWidgetItem,QSizePolicy,QSpacerItem,QFileDialog,QTableWidget,QWidget,QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QCheckBox,QListWidget,QListWidgetItem
from PyQt4.QtCore import Qt,QStringList,QString,QFileInfo

sheetstyle = "QTableWidget{Width:513px;Height:42px;}" \
             "QHeaderView:section{Height:32px;font:14px;font-family:'微软雅黑';font-size:14px;color:#ffffff;background-color:#459fe2;border:1px solid #ffffff;}" \
             "QTableWidget::indicator{Width:16px;Height:16px;}" \
             "QTableWidget::indicator:unchecked{border-image:url(:/image/选择_normal.png);}" \
             "QTableWidget::indicator:unchecked:hover{border-image:url(:/image/选择_hover.png);}" \
             "QTableWidget::indicator:unchecked:pressed{border-image:url(:/image/选择_hover.png);}" \
             "QTableWidget::indicator:checked{background:red;border-image:url(:/image/选择_pressed.png);}" \
             "QTableWidget::indicator:checked:hover{border-image:url(:/image/选择_pressed.png);}" \
             "QTableWidget::indicator:checked:pressed{border-image:url(:/image/选择_pressed.png);}" \
             "QTableWidget::item{Height:25px;}" \
             "QPushButton{Width:70px;Height:28px;}"

class ThirdPart(QWizardPage):

    def __init__(self):
        super(ThirdPart, self).__init__()
        self.completed = False
        self.setTitle(u'第三方库设置')
        self.setSubTitle(u'需要设置的第三方库')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(14, 20, 10, 20)

        self.tw_interface = QTableWidget(0,3)
        headerLabels = QStringList()
        headerLabels.append(u'库名')
        headerLabels.append(u'库路径')
        headerLabels.append(u'打开')
        self.tw_interface.setHorizontalHeaderLabels(headerLabels)
        self.tw_interface.setSelectionBehavior(1)
        self.tw_interface.setRowCount(0)
        self.tw_interface.setColumnWidth(0, 200)
        self.tw_interface.setColumnWidth(1, 280)
        self.tw_interface.horizontalHeader().setStretchLastSection(True)

        self.mhlayout = QHBoxLayout()
        on_new_btn = QPushButton()
        on_new_btn.setText(u'添加类库')
        on_new_btn.clicked.connect(self.on_new)

        on_delete_btn = QPushButton()
        on_delete_btn.setText(u'删除类库')
        on_delete_btn.clicked.connect(self.on_delete)

        space = QSpacerItem(40,28,QSizePolicy.Expanding)
        self.mhlayout.addSpacerItem(space)
        self.mhlayout.addWidget(on_new_btn)
        self.mhlayout.addWidget(on_delete_btn)

        rootLayout.addWidget(self.tw_interface)
        rootLayout.addLayout(self.mhlayout)
        self.setLayout(rootLayout)
        self.setStyleSheet(sheetstyle)

        self.alloneEnv = os.getenv('ALLONEDIR', '../..').replace('\\', '/')

    def on_new(self):
        rowIndex = self.tw_interface.rowCount()
        self.tw_interface.setRowCount(rowIndex + 1)
        ptn = self.add_button(rowIndex)
        self.tw_interface.setCellWidget(rowIndex, 2, ptn)

    def on_delete(self):
        rowIndex = self.tw_interface.currentRow()
        if rowIndex != -1:
            self.tw_interface.removeRow(rowIndex)

    def updateTable(self,id):
        filePath = QFileDialog.getOpenFileName(self, "请选择库", self.alloneEnv, "Library(*.lib)")
        if filePath.isEmpty():
            return
        fileinfo = QFileInfo(filePath)
        libPath = fileinfo.absoluteDir().absolutePath()
        libName = fileinfo.baseName()
        # 支持选择文件后与系统ALLONEDIR比较一下变成相对路径
        # 并且能够手动输入相对路径或包含$(ALLONEDIR)的相对路径
        env = QString(os.getenv('ALLONEDIR', '../..').replace('\\', '/'))
        if env.endsWith('/'):
            env.remove(env.lastIndexOf('/'), 1)
        if libPath.contains(env):
            libPath.replace(env, QString('$$ALLONEDIR'))

        self.tw_interface.setItem(id, 1, QTableWidgetItem(libPath))
        self.tw_interface.setItem(id, 0, QTableWidgetItem(libName))

    def add_button(self,id):
        widget = QWidget()
        fileBtn = QPushButton()
        fileBtn.setText(u'浏览...')
        fileBtn.clicked.connect(lambda:self.updateTable(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(fileBtn)
        hLayout.setAlignment(Qt.AlignHCenter)
        hLayout.setContentsMargins(0,0,0,0)
        widget.setLayout(hLayout)
        return widget

    def initializePage(self):
        super(ThirdPart, self).initializePage()
        self.tw_interface.setRowCount(len(app.g_configurations.thirdpart_lib))
        row = 0;
        for libinfo in app.g_configurations.thirdpart_lib:
            twitem0 = QTableWidgetItem(QString(libinfo["libname"]))
            twitem1 = QTableWidgetItem(QString(libinfo["libpath"]))
            self.tw_interface.setItem(row,0,twitem0)
            self.tw_interface.setItem(row,1,twitem1)
            ptn = self.add_button(row)
            self.tw_interface.setCellWidget(row, 2, ptn)
            row +=1

    def validatePage(self):
        thirdpart_libs = []
        if self.tw_interface.rowCount() > 0:
            for i in range(self.tw_interface.rowCount()):
                libinfo = {"libname":"","libpath":""}
                libname = self.tw_interface.item(i,0).text()
                libpath = self.tw_interface.item(i,1).text()
                #print unicode(libname)
                #print unicode(libpath)
                libinfo["libname"] = unicode(libname)
                libinfo["libpath"] = unicode(libpath)
                thirdpart_libs.append(libinfo)

        print thirdpart_libs
        app.g_configurations.thirdpart_lib = thirdpart_libs
        return True