#!/usr/bin/python
# coding:utf-8
from distutils.core import setup

#op={"py2exe": {"includes": ["sip"],"dll_excludes":["MSVCP90.dll","MSVCR90.dll"]}}

op={"py2exe": {'optimize': 0,'includes': ['sip','jinja2'],'packages':['ctypes','_ctypes','encodings'],'dll_excludes':["MSVCP90.dll","MSVCR90.dll"]}}
setup(windows=[{"script":"ComponentDesignTool.py"}],options=op)

#,"icon_resources":[(1,"E:/ISCAS/ProjectWizard/cdt.png")]}
#python setup.py py2exe