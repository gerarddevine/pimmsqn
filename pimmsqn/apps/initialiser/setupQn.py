# -*- coding: utf-8 -*-
NEWAT=1
import os

# get the cmip5 settings
os.environ['DJANGO_SETTINGS_MODULE']='settings'

from pimmsqn.apps.qn.models import Experiment
from pimmsqn.apps.initialiser.XMLinitialiseQ import initialise
from pimmsqn.apps.initialiser.ControlledModel import *
from pimmsqn.apps.initialiser.ControlledGrid import *

from initialiseRefs import *
from initialiseFiles import *
from initialiseVars import *

# Initialise the Questionnaire
initialise()

# load cmip5 input files
#initialiseFiles()

# load variables associated with cmip5 input files
initialiseVars()

# load cmip5 input references
initialiseRefs()

# create experiments
experimentDir = './static/data/experiments'
for f in os.listdir(experimentDir):
    if f.endswith('.xml'):
        x = Experiment.fromXML(os.path.join(experimentDir, f))

# initialise a model template
initialiseModel()

# initialise a grid template
initialiseGrid()