#include "Python.h"
#include "LicenseProve.h"

static PyObject *LicenseError;

static PyObject *isHavingLicense(PyObject *self, PyObject *args)
{
    const char *name;
    char *err;
    if (!PyArg_ParseTuple(args, "s|s", &name,&err))
        return NULL;

	std::string modelName(name);
	std::string errorMsg(err);

	bool ret = Allone::License::CLicenseProve::getInstance()->isHavingLicense(modelName,errorMsg);

	//if(ret == false)
	//	return Py_False;
  //return Py_True;
	return Py_BuildValue("(iss)",(int)ret,modelName.c_str(),errorMsg.c_str());
}

static PyObject *getLicenseType(PyObject *self, PyObject *args)
{
	size_t ret = Allone::License::CLicenseProve::getInstance()->getLicenseType();
    return PyInt_FromSize_t(ret);
}

static PyObject *getLicenseInfo(PyObject *self, PyObject *args)
{
	std::string retMsg = Allone::License::CLicenseProve::getInstance()->getLicenseInfo();
    return PyString_FromStringAndSize(retMsg.c_str(),strlen(retMsg.c_str()));
}

static PyObject *getRegisterInfo(PyObject *self, PyObject *args)
{
	std::string retMsg = Allone::License::CLicenseProve::getInstance()->getRegisterInfo();
    return PyString_FromStringAndSize(retMsg.c_str(),strlen(retMsg.c_str()));
}

static PyObject *getAppendInfo(PyObject *self, PyObject *args)
{
	std::string retMsg = Allone::License::CLicenseProve::getInstance()->getAppendInfo();
    return PyString_FromStringAndSize(retMsg.c_str(),strlen(retMsg.c_str()));
}

static PyMethodDef LicenseMethods[] = {
  {"isHavingLicense",  isHavingLicense, METH_VARARGS,"Having License in this Computer?"},
	{"getLicenseType", getLicenseType, METH_NOARGS,"Get License type"},
	{"getLicenseInfo", getLicenseInfo, METH_NOARGS,"Get License Info"},
	{"getRegisterInfo", getRegisterInfo, METH_NOARGS,"Get License Register Info"},
	{"getAppendInfo", getAppendInfo, METH_NOARGS,"Get License Append Info"},
  {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initLicense(void)
{
    PyObject *m;

    m = Py_InitModule("License", LicenseMethods);
    if (m == NULL)
        return;

    LicenseError = PyErr_NewException("License.error", NULL, NULL);
    Py_INCREF(LicenseError);
    PyModule_AddObject(m, "error", LicenseError);
}
