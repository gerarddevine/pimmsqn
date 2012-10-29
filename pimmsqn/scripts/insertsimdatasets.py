#! /usr/bin/env python
#coding:utf-8

import os
import sys

# putting project and application into sys.path
sys.path.append('/home/gerarddevine/dev/django/qn/pimmsqn')
sys.path.append('/home/gerarddevine/dev/django/qn/pimmsqn/qn')
#sys.path.insert(1, os.path.expanduser('\home\gerarddevine\dev\django\qn\pimmsqn'))
#sys.path.insert(0, os.path.expanduser('/home/gerarddevine/dev/django/qn/pimmsqn/'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'pimmsqn.settings'

from django.core.management import setup_environ

from pimmsqn import settings
setup_environ(settings)

from pimmsqn.apps.qn.models import *


sims = Simulation.objects.filter(isDeleted=False)

for sim in sims:
    if not len(sim.datasets.all()):
        print sim.id
        itypes = Term.objects.filter(vocab=Vocab.objects.get(name='InputTypes')).order_by('id')
        for itype in itypes:
            d = Dataset(usage=itype)
            d.save()
            sim.datasets.add(d)

