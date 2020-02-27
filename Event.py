import wx
import wx.html


class MyHTMLWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = "Event Example", pos = wx.DefaultPosition,
                          size = wx.Size(1280, 720), style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        wx.InitAllImageHandlers()

        bSizerMain = wx.BoxSizer(wx.VERTICAL)

        html = wx.html.HtmlWindow(self)
        html.SetRelatedFrame(self, "%s")
        # bSizerMain.Add(html, 0, wx.ALL, 1)
        # html.LoadPage("http://info.cern.ch/hypertext/WWW/TheProject.html")
        html.SetPage('<html><body><img src="img1.jpg" /></body></html>')

        self.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.OnLinkClicked, html)
        self.Bind(wx.html.EVT_HTML_CELL_CLICKED, self.OnCellClicked, html)

    def OnLinkClicked(self, event):
        print("Ja")
        event.Skip()

    def OnCellClicked(self, event):
        dialog = wx.MessageDialog(self, "The cake is a lie!", "", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MyHTMLWindow(None)
    frame.Show()
    app.MainLoop()
