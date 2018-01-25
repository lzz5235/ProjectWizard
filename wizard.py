#!/usr/bin/python
# coding:utf-8

'''
作者：李肇中
日期：2016-6-13
概述：向导窗口
'''

from PyQt4.QtGui import QWizard,QIcon
from pages import baseinfo,qtlibrary,frameworklibrary,interface,panel,thirdpart
import os


styleSheet = "QWizard{background-color:#dddddd;}" \
             "QWizardPage{background-color:#ebebeb;}" \
             "QPushButton#Next{Width:90px;Height:31px;border-image:url(:/image/下一步_normal.png);}" \
             "QPushButton#Next:!enabled{Width:90px;Height:31px;border-image:url(:/image/下一步_disable.png);}" \
             "QPushButton#Next:hover{Width:90px;Height:31px;border-image:url(:/image/下一步_hover.png);}" \
             "QPushButton#Next:pressed{Width:90px;Height:31px;border-image:url(:/image/下一步_pressed.png);}" \
             "QPushButton#Previous{Width:90px;Height:31px;border-image:url(:/image/上一步_normal.png);}" \
             "QPushButton#Previous:!enabled{Width:90px;Height:31px;border-image:url(:/image/上一步_disable.png);}" \
             "QPushButton#Previous:hover{Width:90px;Height:31px;border-image:url(:/image/上一步_hover.png);}" \
             "QPushButton#Previous:pressed{Width:90px;Height:31px;border-image:url(:/image/上一步_pressed.png);}" \
             "QPushButton#Cancel{Width:90px;Height:31px;border-image:url(:/image/取消_normal.png);}" \
             "QPushButton#Cancel:!enabled{Width:90px;Height:31px;border-image:url(:/image/取消_disable.png);}" \
             "QPushButton#Cancel:hover{Width:90px;Height:31px;border-image:url(:/image/取消_hover.png);}" \
             "QPushButton#Cancel:pressed{Width:90px;Height:31px;border-image:url(:/image/取消_pressed.png);}" \
             "QPushButton#Finish{Width:90px;Height:31px;border-image:url(:/image/完成_normal.png);}" \
             "QPushButton#Finish:!enabled{Width:90px;Height:31px;border-image:url(:/image/完成_disable.png);}" \
             "QPushButton#Finish:hover{Width:90px;Height:31px;border-image:url(:/image/完成_hover.png);}" \
             "QPushButton#Finish:pressed{Width:90px;Height:31px;border-image:url(:/image/完成_pressed.png);}"


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class MyWizard(QWizard):
    '''
    向导类
    '''
    def __init__(self):
        super(MyWizard,self).__init__()
        #QWizard.IndependentPages
        self.setOption(QWizard.IndependentPages,False)
        self.setWindowTitle('框架工程向导')
        self.setWindowIcon(QIcon(':/image/框架工程向导icon.png'))
        self.setWizardStyle(QWizard.ModernStyle)
        self.addPage(baseinfo.BaseInfoPage())
        self.addPage(qtlibrary.QtLibraryPage())
        self.addPage(frameworklibrary.FrameworkLibraryPage())
        self.addPage(thirdpart.ThirdPart())
        self.addPage(interface.InterfacePage())
        self.addPage(panel.PanelPage())
        self.button(QWizard.NextButton).setEnabled(False)
        self.setButtonText(QWizard.NextButton,'')
        self.setButtonText(QWizard.BackButton, '')
        self.setButtonText(QWizard.HelpButton, '')
        self.setButtonText(QWizard.CancelButton, '')
        self.setButtonText(QWizard.FinishButton, '')
        self.button(QWizard.NextButton).setObjectName("Next")
        self.button(QWizard.BackButton).setObjectName("Previous")
        self.button(QWizard.HelpButton).setObjectName("Help")
        self.button(QWizard.CancelButton).setObjectName("Cancel")
        self.button(QWizard.FinishButton).setObjectName("Finish")

        self.setStyleSheet(styleSheet)

    def accept(self):
        # template_name = app.g_configurations.template_source
        # template_dir = app.g_pwd + os.sep + 'templates' + os.sep + template_name
        # for file in app.g_configurations.config['files']:
        #     sourcepath = template_dir + os.sep + file['source']
        #     targetdir = app.g_configurations.project_location + app.g_configurations.project_name
        #     targetpath =  targetdir + os.sep + file['target']
        #     fi = QFileInfo(targetpath)
        #     qdir = fi.absoluteDir()
        #     if not qdir.exists():
        #         qdir.mkpath(fi.absolutePath())
        #     with open(sourcepath,'r') as f:
        #         content = f.read()
        #         content = app.render(content, config = app.g_configurations)
        #     with open(targetpath,'w+') as f:
        #         f.write(content.encode('utf-8'))
        super(MyWizard, self).accept()

    def validateCurrentPage(self):
        #print self.currentId()
        return super(MyWizard, self).validateCurrentPage()