#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-6-14
概述：接口选择
'''

import app

from PyQt4.QtGui import QWizardPage,QVBoxLayout,QListWidget,QListWidgetItem
from PyQt4.QtCore import Qt

sheetstyle = "QListWidget{Width:513px;Height:141px;spacing:8px;show-decoration-selected: 1;}" \
             "QCheckBox{spacing:10px;spacing:10px;color:#333333;font-family:'微软雅黑';font-size:14px;font-weight:bold;}" \
             "QCheckBox::indicator{Width:16px;Height:16px;}" \
             "QCheckBox::indicator:unchecked{border-image:url(:/image/选择_normal.png);}" \
             "QCheckBox::indicator:unchecked:hover{border-image:url(:/image/选择_hover.png);}" \
             "QCheckBox::indicator:unchecked:pressed{border-image:url(:/image/选择_hover.png);}" \
             "QCheckBox::indicator:checked{background:red;border-image:url(:/image/选择_pressed.png);}" \
             "QCheckBox::indicator:checked:hover{border-image:url(:/image/选择_pressed.png);}" \
             "QCheckBox::indicator:checked:pressed{border-image:url(:/image/选择_pressed.png);}" \
             "QListWidget::indicator{Width:16px;Height:16px;}" \
             "QListWidget::indicator:unchecked{border-image:url(:/image/选择_normal.png);}" \
             "QListWidget::indicator:unchecked:hover{border-image:url(:/image/选择_hover.png);}" \
             "QListWidget::indicator:unchecked:pressed{border-image:url(:/image/选择_hover.png);}" \
             "QListWidget::indicator:checked{background:red;border-image:url(:/image/选择_pressed.png);}" \
             "QListWidget::indicator:checked:hover{border-image:url(:/image/选择_pressed.png);}" \
             "QListWidget::indicator:checked:pressed{border-image:url(:/image/选择_pressed.png);}" \
             "QListWidget::item{Height:25px;padding-right:10px;}"

class InterfacePage(QWizardPage):

    def __init__(self):
        super(InterfacePage,self).__init__()
        self.completed = False
        self.setTitle('接口设置')
        self.setSubTitle('设置需要实现的接口')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(14, 20, 10, 20)
        self.cb_component_type = self.field('component_type*')

        self.lw_interface = QListWidget()
        rootLayout.addWidget(self.lw_interface)
        self.setLayout(rootLayout)
        self.setStyleSheet(sheetstyle)
        #component_type = self.cb_component_type.currentIndex()
        #if component_type == 0:
        #    app.g_configurations.component_type = "server"
        #elif component_type == 1:
        #    app.g_configurations.component_type = "window"


    def initializePage(self):
        super(InterfacePage, self).initializePage()
        self.lw_interface.clear()
        exsits = []
        for key in app.g_configurations.interfaces:
            if app.g_configurations.interfaces[key]:
                exsits.append(key)

        for interface in app.g_configurations.config['interfaces']:
            # name + description
            display = interface['name'] + ' (' + interface['description'] + ')'
            # print display
            # litem = QListWidgetItem(interface['name'])
            litem = QListWidgetItem(display)
            litem.setToolTip(interface['description'])
            litem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

            isdefault = False
            isUseable = True

            if app.g_configurations.component_type == "window":
                if interface['flag_win'] == 3: #必须实现
                    isdefault = True
                    litem.setFlags(Qt.ItemIsUserCheckable)
                elif interface['flag_win'] == 2: #可选并选中
                    isdefault = True
                elif interface['flag_win'] == 1: #可选并不选
                    isdefault = False
                else:   #不需实现
                    isUseable = False
            else:
                if interface['flag_service'] == 3:
                    isdefault = True
                    litem.setFlags(Qt.ItemIsUserCheckable)
                elif interface['flag_service'] == 2:
                    isdefault = True
                elif interface['flag_service'] == 1:
                    isdefault = False
                else:
                    isUseable = False

            if app.g_configurations.initialized:
                if interface['name'] in exsits:
                    isdefault = True
                else:
                    isdefault = False

            if isdefault:
                litem.setCheckState(Qt.Checked)
            else:
                litem.setCheckState(Qt.Unchecked)
            if isUseable:
                self.lw_interface.addItem(litem)

    def validatePage(self):
        interfaces = {}
        for i in range(self.lw_interface.count()):
            litem = self.lw_interface.item(i)
            display = litem.text()
            key = app.QString2str(display.split(' (')[0])
            if litem.checkState() == 2:
                interfaces[key] = True;
            else:
                interfaces[key] = False;

        app.g_configurations.interfaces = interfaces
        return True
    def flush(self,text):
        self.initializePage(self)