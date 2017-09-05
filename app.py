# -*- coding: utf-8 -*- 


import wx
import wx.xrc
import wx.calendar
import main
import sys
reload(sys)
sys.setdefaultencoding('utf8')







class MainApp ( wx.Frame ):
	
	def __init__( self, parent ):
		self.operate = 0
		main.mas = main.upmas()
		
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyDC", pos = wx.DefaultPosition, size = wx.Size( 500,348 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,-1 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Я должен", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer5.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Мне должны", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
				

		C_listChoices = []
		for item in main.mas:
			if item[1] == 'C':
				C_listChoices.append(item[0])
				
		self.C_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,200 ), C_listChoices, 0 )
		self.C_list.SetBackgroundColour( wx.Colour( 255, 198, 198 ) )
		
		fgSizer5.Add( self.C_list, 0, wx.ALL, 5 )
		
		D_listChoices = []
		C_listChoices = []
		for item in main.mas:
			if item[1] == 'D':
				D_listChoices.append(item[0])
		
		self.D_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,200 ), D_listChoices, 0 )
		self.D_list.SetBackgroundColour( wx.Colour( 221, 255, 221 ) )
		
		fgSizer5.Add( self.D_list, 0, wx.ALL, 5 )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Всего:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gSizer9.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.s1 = 0
		
		for item in main.mas:
			if item[1] == 'C':
				self.s1+=int(item[4])
		
		self.C_sum = wx.StaticText( self, wx.ID_ANY, str(self.s1), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.C_sum.Wrap( -1 )
		gSizer9.Add( self.C_sum, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Профит", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gSizer9.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		
		self.profit = 0
		
		
		self.P_sum = wx.StaticText( self, wx.ID_ANY, str(self.profit), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.P_sum.Wrap( -1 )
		gSizer9.Add( self.P_sum, 0, wx.ALL, 5 )
		
				
		
		fgSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Всего:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gSizer7.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		
		self.s2 = 0
		
		for item in main.mas:
			if item[1] == 'D':
				self.s2+=int(item[4])
		
		self.D_sum = wx.StaticText( self, wx.ID_ANY, str(self.s2), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.D_sum.Wrap( -1 )
		gSizer7.Add( self.D_sum, 0, wx.ALL, 5 )
		
		self.profit = self.s2-self.s1
		self.P_sum.SetLabel(str(self.profit))
		
		fgSizer5.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		fgSizer4.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Суть", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		sbSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.ess_text = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.ess_text.SetMinSize( wx.Size( 160,-1 ) )
		
		sbSizer3.Add( self.ess_text, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Партнёр", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		sbSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.part_text = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.part_text.SetMinSize( wx.Size( 160,-1 ) )
		
		sbSizer3.Add( self.part_text, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Сумма", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		sbSizer3.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.summ_text = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.summ_text.SetMinSize( wx.Size( 160,-1 ) )
		
		sbSizer3.Add( self.summ_text, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Дедлайн", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		sbSizer3.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.deadl_text = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.deadl_text.SetMinSize( wx.Size( 160,-1 ) )
		
		sbSizer3.Add( self.deadl_text, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.menu = wx.Menu()
		self.add_new = wx.MenuItem( self.menu, wx.ID_ANY, u"Добавить"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu.AppendItem( self.add_new )
		
		self.del_item = wx.MenuItem( self.menu, wx.ID_ANY, u"Удалить"+ u"\t" + u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu.AppendItem( self.del_item )
		
		self.m_menubar1.Append( self.menu, u"Запись" ) 
		
		self.SetMenuBar( self.m_menubar1 )

		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.C_list.Bind( wx.EVT_LISTBOX, self.operate_c_item )
		self.D_list.Bind( wx.EVT_LISTBOX, self.operate_d_item )
		self.Bind( wx.EVT_MENU, self.raise_adder, id = self.add_new.GetId() )
		self.Bind( wx.EVT_MENU, self.delete_item, id = self.del_item.GetId() )
		
		self.Show(True)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	
	def operate_c_item( self, event ):
		self.operate = 1
		self.D_list.DeselectAll()
		for item in main.mas:
			if item[0] == self.C_list.StringSelection and item[1] == 'C':
				self.ess_text.SetValue(item[2])
				self.part_text.SetValue(item[3])
				self.summ_text.SetValue(item[4])
				self.deadl_text.SetValue(item[5])
				
	def operate_d_item( self, event ):
		self.operate = 2
		self.C_list.DeselectAll()
		for item in main.mas:
			if item[0] == self.D_list.StringSelection and item[1] == 'D':
				self.ess_text.SetValue(item[2])
				self.part_text.SetValue(item[3])
				self.summ_text.SetValue(item[4])
				self.deadl_text.SetValue(item[5])
	
	def raise_adder( self, event ):
		new = NewTask(None)
		
	def delete_item( self, event ):
		if self.operate == 1:
			self.s1-=int(self.summ_text.Value)
			self.C_sum.SetLabel(str(self.s1))
			main.delselected(self.C_list.StringSelection)
			main.downmas()
			self.C_list.Delete(self.C_list.GetSelection())
		if self.operate == 2:
			self.s2-=int(self.summ_text.Value)
			self.D_sum.SetLabel(str(self.s2))
			main.delselected(self.D_list.StringSelection)
			main.downmas()
			self.D_list.Delete(self.D_list.GetSelection())
			
		self.D_sum.SetLabel(str(self.s2-self.s1))

class NewTask ( wx.Frame ):
	
	def __init__( self, parent ):
		
		self.typ = 0
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 328,491 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( -1,410 ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.add_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.add_name, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		choose1Choices = [ u"Я должен", u"Мне должны" ]
		self.choose1 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, choose1Choices, 1, wx.RA_SPECIFY_COLS )
		self.choose1.SetSelection( 0 )
		fgSizer3.Add( self.choose1, 0, wx.ALL, 5 )
		
		choose2Choices = [ u"Деньги", u"Услугу" ]
		self.choose2 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, choose2Choices, 1, wx.RA_SPECIFY_COLS )
		self.choose2.SetSelection( 1 )
		fgSizer3.Add( self.choose2, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Суть", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer3.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.ess_add = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer3.Add( self.ess_add, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Партнёр", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer3.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.part_add = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.part_add, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Сумма", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer3.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.sum_add = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100000, 0 )
		self.sum_add.Enable( False )
		
		fgSizer3.Add( self.sum_add, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Дедлайн", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer3.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.deadl_add = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer3.Add( self.deadl_add, 0, wx.ALL, 5 )
		
		self.calendar = wx.calendar.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.calendar.CAL_MONDAY_FIRST|wx.calendar.CAL_SHOW_HOLIDAYS )
		fgSizer3.Add( self.calendar, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.confirm_btn = wx.Button( self, wx.ID_ANY, u"ГОТОВО", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.confirm_btn.SetDefault() 
		gSizer6.Add( self.confirm_btn, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.cancel_btn = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.cancel_btn, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		self.choose1.Bind( wx.EVT_RADIOBOX, self.set_type )
		self.choose2.Bind( wx.EVT_RADIOBOX, self.check_sum )
		self.calendar.Bind( wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.set_deadl_date )
		self.confirm_btn.Bind( wx.EVT_BUTTON, self.confirm_adding )
		self.cancel_btn.Bind( wx.EVT_BUTTON, self.cancel_adding )
		
		self.Show(True)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_type( self, event ):
		self.typ = self.choose1.Selection
	
	def check_sum( self, event ):
		if self.choose2.Selection == 1:
			self.sum_add.Disable()
		if self.choose2.Selection == 0:
			self.sum_add.Enable()
	
	def set_deadl_date( self, event ):
		self.deadl_add.Value = str(self.calendar.Date)[0:8]
	
	def confirm_adding( self, event ):
		self.newitem = []
		self.newitem.append(self.add_name.Value)
		if self.typ == 0:
			self.newitem.append ('C')
		if self.typ == 1:
			self.newitem.append ('D')
		self.newitem.append(self.ess_add.Value)
		self.newitem.append(self.part_add.Value)
		if self.sum_add.Enabled == True:
			self.newitem.append(self.sum_add.Value)
		else:
			self.newitem.append('0')
		self.newitem.append(self.deadl_add.Value)
		main.addnew(self.newitem[0], self.newitem[1], self.newitem[2], self.newitem[3], str(self.newitem[4]), self.newitem[5])
		main.downmas()
		
		if self.typ == 0:
			
			app.C_list.Append(self.newitem[0])
			app.s1+=int(self.newitem[4])
			app.C_sum.SetLabel(str(app.s1))
			
		if self.typ == 1:
			
			app.D_list.Append(self.newitem[0])
			app.s2+=int(self.newitem[4])
			app.D_sum.SetLabel(str(app.s2))
		
		app.D_sum.SetLabel(str(app.s2-app.s1))
		
		self.Close()
		
	
	def cancel_adding( self, event ):
		self.Close()
		








list = wx.App()
app = MainApp(None)
list.MainLoop()