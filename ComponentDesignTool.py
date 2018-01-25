#!/usr/bin/python
# coding:utf-8
import sys
import os
import app
import mainwindow

from PyQt4.QtGui import QApplication,QMessageBox
from PyQt4.QtCore import QTextCodec,QString
from ctypes import *;
global str;

styleSheet = "QMainWindow{background-color:#dddddd;border-style:solid;border-color:gray;}" \
             "QStatusBar{background-color:rgb(62,62,62);color:#FFFFFF;Height:50px;}" \
             "QHeaderView:section{Height:42px;font:14px;font-family:'微软雅黑';font-size:14px;color:#ffffff;background-color:#459fe2;border:1px groove inset;}" \
             "QTableWidget{Height:601px;Width:1000px;font:14pt;color:#333333;font-family:'微软雅黑';border:1px solid gray}" \
             "QToolBar{background-color:rgb(62,62,62);}" \
             "QToolButton{font-family:'微软雅黑';font-size:12px;color:#acacac;}" \
             "QToolButton:hover{background-color:rgb(62,62,62);}" \
             "QGroupBox{font:16px;font-family:'微软雅黑';color:#656466;}" \
             "QLineEdit{font-size:14px;Height:21px;Width:100px;background-color:#f8f8f8;border: 1px solid gray;padding: 0 8px;}" \
             "QListWidget{font:14px;font-family:'微软雅黑';color:#333333;font-weight:bold;Width:200px;background-color:#ebebeb;border:1px solid gray}" \
             "QLabel{font:14px;font-family:'微软雅黑';color:#656466;font-weight:bold;}" \
             "QPushButton#modify_btn{Width:70px;Height:28px;border-image:url(:/image/修改_normal.png);}" \
             "QPushButton#modify_btn:disabled{Width:70px;Height:28px;border-image:url(:/image/修改_disable.png);}" \
             "QPushButton#modify_btn:hover{Width:70px;Height:28px;border-image:url(:/image/修改_hover.png);}" \
             "QPushButton#modify_btn:pressed{Width:70px;Height:28px;border-image:url(:/image/修改_pressed.png);}" \
             "QPushButton#del_btn{Width:70px;Height:28px;border-image:url(:/image/删除_normal.png);}" \
             "QPushButton#del_btn:disabled{Width:70px;Height:28px;border-image:url(:/image/删除_disable.png);}" \
             "QPushButton#del_btn:hover{Width:70px;Height:28px;border-image:url(:/image/删除_hover.png);}" \
             "QPushButton#del_btn:pressed{Width:70px;Height:28px;border-image:url(:/image/删除_pressed.png);}" \
             "QPushButton#btn_location{Width:90px;Height:28px;border-image:url(:/image/打开_normal.png);}" \
             "QPushButton#btn_location:disabled{Width:90px;Height:28px;border-image:url(:/image/打开_disable.png);}" \
             "QPushButton#btn_location:hover{Width:90px;Height:28px;border-image:url(:/image/打开_hover.png);}" \
             "QPushButton#btn_location:pressed{Width:90px;Height:28px;border-image:url(:/image/打开_pressed.png);}" \
             "QPushButton#gen_btn{Width:110px;Height:28px;border-image:url(:/image/生成_normal.png);}" \
             "QPushButton#gen_btn:disabled{Width:110px;Height:28px;border-image:url(:/image/生成_disable.png);}" \
             "QPushButton#gen_btn:hover{Width:110px;Height:28px;border-image:url(:/image/生成_hover.png);}" \
             "QPushButton#gen_btn:pressed{Width:110px;Height:28px;border-image:url(:/image/生成_pressed.png);}" \
             "QTreeWidget{font:14px;font-family:'微软雅黑';color:#333333;font-weight:bold;}"

def main():
    qapp = QApplication(sys.argv)
    app.g_pwd = os.getcwd()
    print app.g_pwd

    tc = QTextCodec.codecForName('utf-8')
    QTextCodec.setCodecForCStrings(tc)
    QTextCodec.setCodecForLocale(tc)
    QTextCodec.setCodecForTr(tc)

    #遍历目录
    tmpdirs = os.listdir(app.g_pwd + os.sep + 'templates')
    for tmpdir in tmpdirs:
        currentdir = app.g_pwd + os.sep + 'templates' + os.sep + tmpdir
        if os.path.isdir(currentdir) and os.path.exists(currentdir + os.sep + 'config.json'):
            app.g_templates.append(tmpdir)

    #检查 ALLONEDIR 和 QTDIR
    if os.getenv('ALLONEDIR', '') == '' or os.getenv('QTDIR', '') == '':
        QMessageBox.warning(None, '提示信息', '使用组件设计工具前，请先设置 ALLONEDIR 和 QTDIR 的系统环境变量！')
        return

    m = mainwindow.mainwindow()
    m.show()
    qapp.setStyleSheet(styleSheet)
    qapp.exec_()

if __name__ == "__main__":
    main()