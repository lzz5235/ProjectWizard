#ifndef {{ config.project_name.upper() }}_H
#define {{ config.project_name.upper() }}_H

#include "{{ config.project_name }}Def.h"
#include "EventNotification/BaseEventHandler.h"
{% if config.component_type == "window" %}
#include <QWidget>
#include "ui_{{ config.project_name }}.h"
#include "ComponentBase/ComponentWin.h"

using namespace Allone;

extern "C" {{ config.project_name.upper() }}_EXPORT CComponent* CreateComp(const std::string& CompName);

class {{ config.project_name.upper() }}_EXPORT {{ config.project_name }}:public CComponentWin,public QWidget
{
{% elif config.component_type == "server" %}
#include "ComponentBase/Component.h"
using namespace Allone;

extern "C" {{ config.project_name.upper() }}_EXPORT CComponent* CreateComp(const std::string& CompName);

class {{ config.project_name.upper() }}_EXPORT {{ config.project_name }}:public CComponent
{
{% endif %}
public:
    /*
	 *\fn		CShowVResultWin(const std::string& sCompID)
	 *\brief	Constructor.
	 *\param	sCompID	Identifier of the comp.
	 */
    {{ config.project_name }}(const std::string& sCompID);

    /*
	 *\fn		~CShowVResultWin()
	 *\brief	Finaliser.
	 */
    virtual ~{{ config.project_name }}();
{% if config.component_type == "window" %}
{% if config.interfaces["changeShowMode"] %}
    /*
	 *\fn		void changeShowMode(const std::string& name)
	 *\brief	Change show mode.
	 *\param	name	The name.
	 */
	void changeShowMode(const std::string& sShowMode);
{% endif %} {% if config.interfaces["curScreenDescribe"] %}
/*
	 *\fn		virtual void curScreenDescribe(const std::string& sDescribe)
	 *\brief	Current screen describe. 
	 *\param	sDescribe	The describe. 
	 */
	virtual void curScreenDescribe(const std::string& sDescribe);
{% endif %}{% endif %} {% if config.interfaces["initialize"] %}
/*
	 *\fn		virtual void initialize(const CompConfigInfo& compCfgInfo)
	 *\brief	Initializes this object.
	 *\param	compCfgInfo	Information describing the comp configuration.
	 */
	virtual void initialize(const CompConfigInfo& compCfgInfo);
{% endif %} {% if config.interfaces["onListenerCompStatusUpdate"] %}
	/*
	 *\fn		virtual void onListenerCompStatusUpdate(COMPSTATUS_TYPE event) = 0
	 *\brief	Executes the listener comp status update action. 被监听的功能组件状态改变.
	 *\param	event	The event. 被监听的功能组件状态.
	 */
	virtual void onListenerCompStatusUpdate(const std::string sWho,COMPSTATUS_TYPE event);
{% endif %} {% if config.interfaces["showComp"] %}
	/*
	*\fn		virtual bool showComp()
	*\brief		Shows the comp. 显示功能组件
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool showComp();
{% endif %} {% if config.interfaces["hideComp"] %}
	/*
	*\fn		virtual bool hideComp()
	*\brief		Hides the comp. 隐藏功能组件
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool hideComp();
{% endif %} {% if config.interfaces["suspendComp"] %}
	/*
	*\fn		virtual bool suspendComp()
	*\brief		Suspend comp. 挂起功能组件
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool suspendComp();
{% endif %} {% if config.interfaces["resumeComp"] %}
	/*
	*\fn		virtual bool resumeComp()
	*\brief		Resume comp. 恢复功能组件
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool resumeComp();
{% endif %} {% if config.interfaces["terminateComp"] %}
	/*
	*\fn		virtual bool terminateComp()、
	*\brief		Terminate comp. 卸载功能组件
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool terminateComp();
{% endif %} {% if config.interfaces["run"] %}
	/*
	*\fn		virtual bool run()
	*\brief		Runs this object.
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool run();
{% endif %} {% if config.interfaces["saveCompMemento"] %}
	/*
	*\fn		virtual void saveCompMemento()
	*\brief		Saves the comp memento. 保存组件备忘录数据
	*/
	virtual void saveCompMemento();
{% endif %} {% if config.interfaces["resumeCompMemento"] %}
	/*
	*\fn		virtual void resumeCompMemento()
	*\brief		Resume comp memento. 从备忘录中恢复数据
	*/
	virtual void resumeCompMemento();
{% endif %} {% if config.interfaces["workModelChange"] %}
	/*
     *\fn        virtual void workModelChange(EWorkSituation iWorkMode)
     *\brief    Work model change.
     *\param    iWorkMode    The work mode.
     */
    virtual void workModelChange(EWorkSituation iWorkMode);
{% endif %}
protected:
{% if config.interfaces["initData"] %}
	/*
	 *\fn		void initData(const CInitParam& params)
	 *\brief	Initialises the data.
	 *\param	params	Options for controlling the operaation.
	 */
	void initData(const CInitParam& params);
{% endif %}
private:
{% if config.component_type == "window" %}
	Ui::{{ config.project_name }} ui;
{% endif %}
};

#endif
