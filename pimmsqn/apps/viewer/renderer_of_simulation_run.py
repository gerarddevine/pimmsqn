"""
A concrete view over a cim instance.
"""

# Module imports.
import lxml
from lxml import etree as et

from cmip5q.viewer.base_renderer import RendererBase
from cmip5q.viewer.simhtml_generator import get_simrunhtml

# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2011 - Metafor Project"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


class RendererOfSimulationRun(RendererBase):
    """
    Manages rendering of a view over a cim simulation run.
    """

    @property
    def view_type(self):
        """
        Unique key identifying the view type.
        """
        return 'simulationRun'


    def render(self):
        """
        Renders the view in the relevant format/mode.
        """
        html_block = "".join(get_simrunhtml(self.cim_xml))
        return u'{0}'.format(html_block)
