import wx
from libcrono import *

class CronoPy(wx.App):
  def OnInit(self):
    v = cronopy("CronoPy", (50, 60), (450, 340))
    v.Show()
    self.SetTopWindow(v)
    return True

if __name__ == '__main__':
 app = CronoPy(False)
 app.MainLoop()
