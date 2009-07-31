# -*- coding: utf-8 -*-

import grok
from dolmen.queue import ITaskManager


class TaskContainer(grok.Container):
    """A TaskContainer contains flatly all the tasks.
    """
    grok.implements(ITaskManager)
