/********************************************************************************
** Form generated from reading UI file '{{ config.project_name.upper() }}.ui'
**
** Created by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_{{ config.project_name.upper() }}_H
#define UI_{{ config.project_name.upper() }}_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHeaderView>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_{{ config.project_name }}
{
public:

	void setupUi(QWidget *{{ config.project_name }})
	{
		if ({{ config.project_name }}->objectName().isEmpty())
			{{ config.project_name }}->setObjectName(QString::fromUtf8("{{ config.project_name }}"));
		{{ config.project_name }}->resize(721, 574);

		retranslateUi({{ config.project_name }});

		QMetaObject::connectSlotsByName({{ config.project_name }});
	} // setupUi

	void retranslateUi(QWidget *{{ config.project_name }})
	{
		{{ config.project_name }}->setWindowTitle(QApplication::translate("{{ config.project_name }}", "{{ config.project_name }}", 0, QApplication::UnicodeUTF8));
	} // retranslateUi

};

namespace Ui {
	class {{ config.project_name }}: public Ui_{{ config.project_name }} {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_{{ config.project_name }}_H
