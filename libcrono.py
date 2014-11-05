import wx

Blanco=(0,0,0)

class cronopy(wx.Frame):
  Pro_nom="ninguno"
  Tarea_nom="ninguna"
  def __init__(self, title, pos, size):
    wx.Frame.__init__(self, None, -1, title, pos, size)

    
    self.CreateStatusBar()
    self.crearToolbar()
    self.SetStatusText("Bienvenido a Cronopy!")



  def crearToolbar(self):
   toolbar= self.CreateToolBar();
   for elemento in self.barraInicial():
      self.crearEspacio(toolbar, *elemento)
   toolbar.AddSeparator()
   toolbar.Realize()

  def crearEspacio(self, toolbar, etiqueta, archivo, ayuda, manejador):
   if not etiqueta:
     toolbar.AddSeparator()
     return
   icono=wx.Image(archivo, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
   espacio = toolbar.AddSimpleTool(-1, icono, etiqueta, ayuda)
   self.Bind(wx.EVT_MENU, manejador, espacio)

  def barraInicial(self):
   return (("Proyectos", "imagenes/new.png", "Opciones de Proyecto", self.SiPronuevo), ("Tareas", "imagenes/open.png", "Opciones de tareas", self.SiInfo), ("Acerca de", "imagenes/save.png", "Informacion del aplicactivo", self.SiSalir))

  def SiSalir(self, event):
    self.Close()

  def SiInfo(self, event):
    wx.MessageBox("Este es Cronopy, Aplicacion para registro de tiempo. \n Autor: Carlos Andres Lopez", 
           "Acerca de CronoPy", wx.OK | wx.ICON_INFORMATION, self)

  def SiPronuevo(self, event):
    valor=wx.TextEntryDialog(self, "Nombre del proyecto: ", "Crear proyecto", "pro", style=wx.OK|wx.CANCEL)
    if valor.ShowModal() == wx.ID_OK:
       self.pro_nom=valor.GetValue()
       print "Tu digitaste: %s" % self.pro_nom      
       self.SetStatusText(self.pro_nom + ": " + self.Tarea_nom)
    valor.Destroy()  
