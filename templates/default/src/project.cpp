#include "{{ config.project_name }}.h"
#include <QDebug>
#include "AllOneFoundation/AllOneException.h"
{% for lib in config.libs %}
{%- if lib['name']  == 'EventNotification' -%}
#include "EventNotification/MsgFeedbackEvent.h"
#include "EventNotification/EventNotification.h"
#include "EventNotification/KeyboardOperEvent.h"
{% elif lib['name'] == 'DBCommon' -%}
#include "DBManagerComp/DBManagerComp.h"
#include "DBCommon/DBConnection.h"
#include "DBCommon/ConnectionPool.h"
#include "DBCommon/Database.h"
#include "DBCommon/DBCursor.h"
#include "DBCommon/DBStruct.h"
{% elif lib['name'] == 'UDPCommunication' -%}
#include "UDPCommunication/UDPDataEvent.h"
#include "UDPCommunication/Communicator.h"
{% elif lib['name'] == 'DDSMsgHandle' -%}
#include "DDSMsgHandle/ManHandleDDSDataRule.h"
#include "DDSMsgHandle/DDSDataEvent.h"
{% elif lib['name'] == 'RTDBDriver' -%}
#include "RTDBDriver/RTDBEvent.h"
#include "RTDBDriver/RTDB.h"
{% endif -%}
{% endfor %}

CComponent* CreateComp( const std::string& CompName)
{
	CComponent* comp = 0;
	if (CompName == "{{ config.project_name }}")
	{
		comp = new {{ config.project_name }}(CompName);
	}

	return comp;
}
{% if config.component_type == "window" %}
{{ config.project_name }}::{{ config.project_name }}(const std::string& sCompID)
    :CComponentWin(sCompID)
{
    ui.setupUi(this);

    qDebug()<<"{{ config.project_name }} has been loaded.";
}
{% elif config.component_type == "server" %}
{{ config.project_name }}::{{ config.project_name }}(const std::string& sCompID)
    :CComponent(sCompID)
{
    qDebug()<<"{{ config.project_name }} has been loaded.";
}
{% endif %}
{{ config.project_name }}::~{{ config.project_name }}()
{
}
{% if config.component_type == "window" %}
{% if config.interfaces["changeShowMode"] %}
void {{ config.project_name }}::changeShowMode(const std::string& name)
{
}
{% endif %} {% if config.interfaces["curScreenDescribe"] %}
void {{ config.project_name }}::curScreenDescribe(const std::string& sDescribe)
{
	CComponentWin::curScreenDescribe(sDescribe);
}
{% endif %} {% endif %} {% if config.interfaces["initialize"] %}
void {{ config.project_name }}::initialize(const CompConfigInfo& compCfgInfo)
{
}
{% endif %} {% if config.interfaces["onListenerCompStatusUpdate"] %}
void {{ config.project_name }}::onListenerCompStatusUpdate(const std::string sWho,COMPSTATUS_TYPE event)
{
}
{% endif %} {% if config.interfaces["showComp"] %}
bool {{ config.project_name }}::showComp()
{
    return true;
}
{% endif %} {% if config.interfaces["hideComp"] %}
bool {{ config.project_name }}::hideComp()
{
    return true;
}
{% endif %} {% if config.interfaces["suspendComp"] %}
bool {{ config.project_name }}::suspendComp()
{
    return true;
}
{% endif %} {% if config.interfaces["resumeComp"] %}
bool {{ config.project_name }}::resumeComp()
{
    return true;
}
{% endif %} {% if config.interfaces["terminateComp"] %}
bool {{ config.project_name }}::terminateComp()
{
    return true;
}
{% endif %} {% if config.interfaces["run"] %}
bool {{ config.project_name }}::run()
{
    return true;
}
{% endif %} {% if config.interfaces["saveCompMemento"] %}
void {{ config.project_name }}::saveCompMemento()
{
}
{% endif %} {% if config.interfaces["resumeCompMemento"] %}
void {{ config.project_name }}::resumeCompMemento()
{
}
{% endif %} {% if config.interfaces["workModelChange"] %}
void {{ config.project_name }}::workModelChange(EWorkSituation iWorkMode)
{
}
{% endif %} {% if config.interfaces["initData"] %}
void {{ config.project_name }}::initData(const CInitParam& params)
{
}
{% endif %}
