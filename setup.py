#!/usr/bin/python
# coding:utf-8
import sys
import py2exe
from distutils.core import setup

sys.path.append('C:\Python27\Lib\site-packages\py2exe')
#op={"py2exe": {"includes": ["sip"],"dll_excludes":["MSVCP90.dll","MSVCR90.dll"]}}

op={"py2exe": {'optimize': 0,'includes': ['sip','jinja2'],'packages':['ctypes','_ctypes','encodings'],'dll_excludes':["MSVCP90.dll","MSVCR90.dll"]}}
setup(windows=[{"script":"ComponentDesignTool.py"}],options=op)

#python setup.py py2exe