# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class BuilderFrameMain
###########################################################################

class BuilderFrameMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"BMI Calculator"), pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 300,250 ), wx.Size( 300,250 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.Colour( 183, 253, 255 ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Clear"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Open File"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Save File"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Exit"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )
		
		self.m_menubar1.Append( self.m_menu1, _(u"File") ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"About"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem5 )
		
		self.m_menubar1.Append( self.m_menu2, _(u"Help") ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 300,80 ) ) 
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Name: "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		
		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer2.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Height (cm): "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 1, 250, 165, 1 )
		self.m_spinCtrlDouble1.SetDigits( 1 )
		bSizer3.Add( self.m_spinCtrlDouble1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Weight (kg): "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		
		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_spinCtrlDouble2 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 1, 250, 60, 1 )
		self.m_spinCtrlDouble2.SetDigits( 1 )
		bSizer4.Add( self.m_spinCtrlDouble2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"BMI: "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		
		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"22.04"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		
		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Normal"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		
		bSizer8.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"green.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_bitmap1, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_clear, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.on_openfile, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.on_savefile, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.on_exit, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about_open, id = self.m_menuItem5.GetId() )
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.on_name_select )
		self.m_comboBox1.Bind( wx.EVT_TEXT_ENTER, self.on_name_entered )
		self.m_spinCtrlDouble1.Bind( wx.EVT_SPINCTRLDOUBLE, self.on_height_spin )
		self.m_spinCtrlDouble1.Bind( wx.EVT_TEXT_ENTER, self.on_height_entered )
		self.m_spinCtrlDouble2.Bind( wx.EVT_SPINCTRLDOUBLE, self.on_weight_spin )
		self.m_spinCtrlDouble2.Bind( wx.EVT_TEXT_ENTER, self.on_weight_entered )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_clear( self, event ):
		pass
	
	def on_openfile( self, event ):
		pass
	
	def on_savefile( self, event ):
		pass
	
	def on_exit( self, event ):
		pass
	
	def on_about_open( self, event ):
		pass
	
	def on_name_select( self, event ):
		pass
	
	def on_name_entered( self, event ):
		pass
	
	def on_height_spin( self, event ):
		pass
	
	def on_height_entered( self, event ):
		pass
	
	def on_weight_spin( self, event ):
		pass
	
	def on_weight_entered( self, event ):
		pass
	

###########################################################################
## Class BuilderDialogAbout
###########################################################################

class BuilderDialogAbout ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"About BMI Calculator"), pos = wx.DefaultPosition, size = wx.Size( 198,136 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"BMI Calculator ver0.1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		
		bSizer6.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Gabriel Shih, 2018"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		
		bSizer6.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_about_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_about_close( self, event ):
		pass
	

