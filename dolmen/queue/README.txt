============
dolmen.queue
============

dolmen.queue is a simple implementation of the zc.async package. It
aims to make simple the creation, enqueuing and dispatching of
jobs. The goal is to provide simple components that can be used in a
Dolmen site or in other grok application, very easily.

Tasks
=====

Tasks are the objects representating a queue job. There are 2
distinct interfaces that represent a simple job and a job that
triggers a callback when the execution is finished.

Container
=========

In order to keep track of all the tasks, easily, a tasks container is
available. Commonly, it would be used as a local utility, to store and
retrieve in a convenient way the tasks local to a given site. 
