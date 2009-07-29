# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.app.container.constraints import contains


class ITask(Interface):
    """A simple task. A task is a generic operation, that is dispatched by
    the queue. Tasks are usually successive and not concurrent. The task can
    be executed remotely so don't take the locales and env for granted !
    """   
    def execute():
        """Execute the task. This is the job itself.
        Called during the dipatching. The return value
        will be used as the result of the execution.
        """


class ICallbackTask(ITask):
    """A task that will trigger a callback when executed.
    """       
    def callback(result):
        """Callback, triggered once the task is finished.
        'result' is the return value of the completed execution.
        """


class ITaskManager(Interface):
    """A simple container that contain tasks.
    """
    contains(ITask)
