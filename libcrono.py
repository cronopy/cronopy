import wx

class cronopy(wx.Frame):
  def __init__(self, title, pos, size):
    wx.Frame.__init__(self, None, -1, title, pos, size)
    m_proyecto = wx.Menu()
    m_proyecto.Append(1, "Nuevo Proyecto")
    m_proyecto.Append(2, "Abrir proyecto")
    m_proyecto.Append(3, "Renombrar Proyecto")
    m_proyecto.AppendSeparator()
    m_proyecto.Append(4, "Exportar Proyecto")
    m_proyecto.Append(5, "Importar Proyecto")  

    m_tareas = wx.Menu()
    m_tareas.Append(6, "Nueva Tarea")
    m_tareas.Append(7, "Nueva Subtarea")
    m_tareas.Append(8, "Renombrar Tarea")
    m_tareas.Append(9, "Eliminar Tarea")

    m_informacion= wx.Menu()
    m_informacion.Append(10, "Acerca de...")
    m_informacion.Append(11, "Salir")

    menuBar = wx.MenuBar()
    menuBar.Append(m_proyecto, "&Proyecto")
    menuBar.Append(m_tareas, "&Tareas")
    menuBar.Append(m_informacion, "&Ayuda")

    self.SetMenuBar(menuBar)
    self.CreateStatusBar()
    self.SetStatusText("Bienvenido a Cronopy!")
    self.Bind(wx.EVT_MENU, self.SiInfo, id=10)
    self.Bind(wx.EVT_MENU, self.SiSalir, id=11)
    self.Bind(wx.EVT_MENU, self.SiPronuevo, id=1)

  def SiSalir(self, event):
    self.Close()

  def SiInfo(self, event):
    wx.MessageBox("Este es Cronopy, Aplicacion para registro de tiempo. \n Autor: Carlos Andres Lopez", 
           "Acerca de CronoPy", wx.OK | wx.ICON_INFORMATION, self)

  def SiPronuevo(self, event):
    valor=wx.TextEntryDialog(None, "Nombre del proyecto: ", "Crear proyecto", "pro", style=wx.OK|wx.CANCEL)
    if valor.ShowModal() == wx.ID_OK:
       print "You entered: %s" % valor.GetValue()
    valor.Destroy()  

