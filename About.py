
# coding=utf-8

import sys
import datetime
import os
import wx
import wx.html
import wx.lib.wxpTag
import webbrowser
from Main import __version__

# ---------------------------------------------------------------------------


class AboutDlg(wx.Dialog):
    text = '''
<html>
<body bgcolor="#DCDCDC" style="font-family: Arial; background-color: #DCDCDC;">
<center>
    <img src="{0}/images/python-64.png" width="64" height="64" alt="Python">
    <img src="{0}/images/icon-64.png" width="64" height="64" alt="NodeMCU">
    <img src="{0}/images/espressif-64.png" width="64" height="64" alt="Espressif, producers of ESP8266 et.al.">
    <img src="{0}/images/wxpython-64.png" width="64" height="43" alt="wxPython, cross-platform GUI framework">

    <h1>eBrain Update Wizard</h1>

    <p>Version {1}</p>

    <p>Fork the <a style="color: #004CE5;" href="https://github.com/opencoca/eBrain-Flasher">project on
    GitHub</a> and help improve it for all!</p>


    <p>&copy; {2} Robot In a Can & OpenCo Licensed under AGPL.</p>

    <p>
        <wxp module="wx" class="Button">
            <param name="label" value="Close">
            <param name="id" value="ID_OK">
        </wxp>
    </p>
</center>
</body>
</html>
'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "About eBrain Update Wizard")
        html = HtmlWindow(self, wx.ID_ANY, size=(420, -1))
        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            html.SetStandardFonts()
        txt = self.text.format(self._get_bundle_dir(), __version__, datetime.datetime.now().year)
        html.SetPage(txt)
        ir = html.GetInternalRepresentation()
        html.SetSize((ir.GetWidth() + 25, ir.GetHeight() + 25))
        self.SetClientSize(html.GetSize())
        self.CentreOnParent(wx.BOTH)

    @staticmethod
    def _get_bundle_dir():
        # set by PyInstaller, see http://pyinstaller.readthedocs.io/en/v3.2/runtime-information.html
        if getattr(sys, 'frozen', False):
            # noinspection PyUnresolvedReferences,PyProtectedMember
            return sys._MEIPASS
        else:
            return os.path.dirname(os.path.abspath(__file__))


class HtmlWindow(wx.html.HtmlWindow):
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())

# ---------------------------------------------------------------------------
