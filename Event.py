import wx
import wx.html
import time


class MyHTMLWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = "Event Example", pos = wx.DefaultPosition,
                          size = wx.Size(1280, 720), style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        wx.InitAllImageHandlers()

        self.counter = 0

        self.html = wx.html.HtmlWindow(self)
        self.html.SetRelatedFrame(self, "%s")
        self.html.SetPage('<html><body><img src="img2.jpg" /></body></html>')

        self.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.OnLinkClicked, self.html)
        self.Bind(wx.html.EVT_HTML_CELL_CLICKED, self.OnCellClicked, self.html)
        self.Bind(wx.html.EVT_HTML_CELL_HOVER, self.OnCellHover, self.html)

    def OnLinkClicked(self, event):
        dialog = wx.MessageDialog(self, "Link wird geladen!", "", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()
        event.Skip()

    def OnCellHover(self, event):
        print(f"{self.counter} I'm different!")
        if self.counter == 200:
            self.Unbind(wx.html.EVT_HTML_CELL_HOVER, self.html)
            self.html.SetPage('<html><body><img src="img1.jpg" /><br><a href="http://info.cern.ch/hypertext/WWW/TheProject.html">Go to info.cern.ch</a></body></html>')
        self.counter += 1
        event.Skip()

    def OnCellClicked(self, event):
        dialog = wx.MessageDialog(self, "The cake is a lie!", "", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()
        self.Unbind(wx.html.EVT_HTML_CELL_CLICKED, self.html)
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MyHTMLWindow(None)
    frame.Show()
    app.MainLoop()
