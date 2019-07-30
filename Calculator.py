＃ -*- coding: utf-8 -*-
 
import wx
import wx.xrc
import math
 
 
#############################################
## Class MyFrame1
#############################################
 
class MyFrame1(wx.Frame):
 def __init__(self, parent):
  wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
       size=wx.Size(486, 448), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
 
  self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
 
  bSizer1 = wx.BoxSizer(wx.VERTICAL)
 
  self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(600, 60), style=wx.TE_RIGHT)
  self.m_textCtrl1.SetMinSize(wx.Size(470, 60))
 
  bSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)
 
  bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
 
  self.m_button1 = wx.Button(self, wx.ID_ANY, u"退格", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer2.Add(self.m_button1, 0, wx.ALL, 5)
 
  self.m_button2 = wx.Button(self, wx.ID_ANY, u"清屏", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer2.Add(self.m_button2, 0, wx.ALL, 5)
 
  self.m_button3 = wx.Button(self, wx.ID_ANY, u"sqrt", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer2.Add(self.m_button3, 0, wx.ALL, 5)
 
  self.m_button4 = wx.Button(self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer2.Add(self.m_button4, 0, wx.ALL, 5)
 
  bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)
 
  bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
 
  self.m_button10 = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer6.Add(self.m_button10, 0, wx.ALL, 5)
 
  self.m_button11 = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer6.Add(self.m_button11, 0, wx.ALL, 5)
 
  self.m_button12 = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer6.Add(self.m_button12, 0, wx.ALL, 5)
 
  self.m_button13 = wx.Button(self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer6.Add(self.m_button13, 0, wx.ALL, 5)
 
  bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)
 
  bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
 
  self.m_button15 = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer7.Add(self.m_button15, 0, wx.ALL, 5)
 
  self.m_button16 = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer7.Add(self.m_button16, 0, wx.ALL, 5)
 
  self.m_button17 = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer7.Add(self.m_button17, 0, wx.ALL, 5)
 
  self.m_button18 = wx.Button(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer7.Add(self.m_button18, 0, wx.ALL, 5)
 
  bSizer1.Add(bSizer7, 0, wx.EXPAND, 5)
 
  bSizer34 = wx.BoxSizer(wx.HORIZONTAL)
 
  self.m_button140 = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer34.Add(self.m_button140, 0, wx.ALL, 5)
 
  self.m_button141 = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer34.Add(self.m_button141, 0, wx.ALL, 5)
 
  self.m_button142 = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer34.Add(self.m_button142, 0, wx.ALL, 5)
 
  self.m_button143 = wx.Button(self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer34.Add(self.m_button143, 0, wx.ALL, 5)
 
  bSizer1.Add(bSizer34, 0, wx.EXPAND, 5)
 
  bSizer35 = wx.BoxSizer(wx.HORIZONTAL)
 
  self.m_button145 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer35.Add(self.m_button145, 0, wx.ALL, 5)
 
  self.m_button148 = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer35.Add(self.m_button148, 0, wx.ALL, 5)
 
  self.m_button149 = wx.Button(self, wx.ID_ANY, u"＋／－", wx.DefaultPosition, wx.Size(110, 60), 0)
  bSizer35.Add(self.m_button149, 0, wx.ALL, 5)
 
  self.m_button150 = wx.Button(self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size(110, 600), 0)
  self.m_button150.SetMinSize(wx.Size(110, 60))
 
  bSizer35.Add(self.m_button150, 0, wx.ALL, 5)
 
  bSizer1.Add(bSizer35, 0, wx.EXPAND, 5)
 
  self.SetSizer(bSizer1)
  self.Layout()
 
  self.Centre(wx.BOTH)
 
  # Connect Events
  self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)
  self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
  self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)
  self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
  self.m_button10.Bind(wx.EVT_BUTTON, self.m_button10OnButtonClick)
  self.m_button11.Bind(wx.EVT_BUTTON, self.m_button11OnButtonClick)
  self.m_button12.Bind(wx.EVT_BUTTON, self.m_button12OnButtonClick)
  self.m_button13.Bind(wx.EVT_BUTTON, self.m_button13OnButtonClick)
  self.m_button15.Bind(wx.EVT_BUTTON, self.m_button15OnButtonClick)
  self.m_button16.Bind(wx.EVT_BUTTON, self.m_button16OnButtonClick)
  self.m_button17.Bind(wx.EVT_BUTTON, self.m_button17OnButtonClick)
  self.m_button18.Bind(wx.EVT_BUTTON, self.m_button18OnButtonClick)
  self.m_button140.Bind(wx.EVT_BUTTON, self.m_button140OnButtonClick)
  self.m_button141.Bind(wx.EVT_BUTTON, self.m_button141OnButtonClick)
  self.m_button142.Bind(wx.EVT_BUTTON, self.m_button142OnButtonClick)
  self.m_button143.Bind(wx.EVT_BUTTON, self.m_button143OnButtonClick)
  self.m_button145.Bind(wx.EVT_BUTTON, self.m_button145OnButtonClick)
  self.m_button148.Bind(wx.EVT_BUTTON, self.m_button148OnButtonClick)
  self.m_button149.Bind(wx.EVT_BUTTON, self.m_button149OnButtonClick)
  self.m_button150.Bind(wx.EVT_BUTTON, self.m_button150OnButtonClick)
 
 def __del__(self):
  pass
 
 # Virtual event handlers, overide them in your derived class
 def m_button1OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result[:-1]
  self.m_textCtrl1.SetValue(result)
 
 def m_button2OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=''
  self.m_textCtrl1.SetValue(result)
 
 def m_button3OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=int(result)
  result=math.sqrt(result)
  self.m_textCtrl1.SetValue(str(result))
 
 def m_button4OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'/'
  self.m_textCtrl1.SetValue(result)
 
 def m_button10OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'7'
  self.m_textCtrl1.SetValue(result)
 
 def m_button11OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'8'
  self.m_textCtrl1.SetValue(result)
 
 def m_button12OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'9'
  self.m_textCtrl1.SetValue(result)
 
 def m_button13OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'*'
  self.m_textCtrl1.SetValue(result)
 
 def m_button15OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'4'
  self.m_textCtrl1.SetValue(result)
 
 def m_button16OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'5'
  self.m_textCtrl1.SetValue(result)
 
 def m_button17OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'6'
  self.m_textCtrl1.SetValue(result)
 
 def m_button18OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'-'
  self.m_textCtrl1.SetValue(result)
 
 def m_button140OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'1'
  self.m_textCtrl1.SetValue(result)
 
 def m_button141OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'2'
  self.m_textCtrl1.SetValue(result)
 
 def m_button142OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'3'
  self.m_textCtrl1.SetValue(result)
 
 def m_button143OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'+'
  self.m_textCtrl1.SetValue(result)
 
 def m_button145OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'0'
  self.m_textCtrl1.SetValue(result)
 
 def m_button148OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=result+'.'
  self.m_textCtrl1.SetValue(result)
 
 def m_button149OnButtonClick(self, event):
  result=self.m_textCtrl1.GetValue()
  result=-int(result)
  self.m_textCtrl1.SetValue(str(result))
 
 def m_button150OnButtonClick(self, event):
  self.m_textCtrl1.SetValue(str(eval(self.m_textCtrl1.GetValue())))
 
app=wx.App()
window=MyFrame1(None)
window.Show(True)
app.MainLoop()
