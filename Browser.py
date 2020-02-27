import wx
import wx.html


class MyHTMLWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = "Basic Example", pos = wx.DefaultPosition,
                          size = wx.Size(500, 300), style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        wx.InitAllImageHandlers()

        bSizerMain = wx.BoxSizer(wx.VERTICAL)

        html = wx.html.HtmlWindow(self)
        html.SetRelatedFrame(self, "%s")
        # bSizerMain.Add(html, 0, wx.ALL, 1)
        html.LoadPage("http://info.cern.ch/hypertext/WWW/TheProject.html")


if __name__ == "__main__":
    app = wx.App()
    frame = MyHTMLWindow(None)
    frame.Show()
    app.MainLoop()
