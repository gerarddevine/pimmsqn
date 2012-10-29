"""
A concrete view over a cim instance.
"""

# Module imports.
import lxml
from lxml import etree as et

from pimmsqn.viewer.base_renderer import RendererBase
from pimmsqn.viewer.plathtml_generator import get_plathtml


class RendererOfPlatform(RendererBase):
    """
    Manages rendering of a view over a cim platform object.
    """

    @property
    def view_type(self):
        """
        Unique key identifying the view type.
        """
        return 'platform'


    def render(self):
        """
        Renders the view in the relevant format/mode.
        """
        html_block = "".join(get_plathtml(self.cim_xml))
        return u'{0}'.format(html_block)