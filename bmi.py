# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:56:17 2018

@author: gabrielshih
"""

import wx
import gettext
_ = gettext.gettext

from gui.bmi_gui import BuilderFrameMain, BuilderDialogAbout

class UserFrameMain(BuilderFrameMain):
    def __init__(self, parent):
        BuilderFrameMain.__init__(self, parent)
        self.SetIcon(wx.Icon("bmi.ico", wx.BITMAP_TYPE_ICO))
        self._bmi_update()
        self.about_box = None
        self.heights = {}
        self.weights = {}
        
    def on_clear( self, event ):
        self.m_comboBox1.Clear()
        self.m_spinCtrlDouble1.Value = 165.
        self.m_spinCtrlDouble2.Value = 60.
        self.heights = {}
        self.weights = {}
        self._bmi_update()

    def on_openfile( self, event ):
        dlg = wx.FileDialog(self, _("Open BMI CSV"),
                            defaultDir=".", defaultFile="bmi.csv",
                            wildcard="CSV files (*.csv)|*.csv;*.CSV",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if filename is not None:
                f=open(filename,'r')
                f.readline()
                self.heights = {}
                self.weights = {}
                self.m_comboBox1.Clear()
                for i in f.readlines():
                    j = i.split(',')
                    self.heights[j[0]] = float(j[1])
                    self.weights[j[0]] = float(j[2])
                    self.m_comboBox1.Append(j[0])
                f.close()

    def on_savefile( self, event ):
        dlg = wx.FileDialog(self, _("Save BMI CSV"),
                            defaultDir=".", defaultFile="bmi.csv",
                            wildcard="CSV files (*.csv)|*.csv;*.CSV",
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            f=open(filename,'w')
            f.write('Name,Height,Weight,BMI\n')
            for i in self.heights.keys():
                height=self.heights[i]
                weight=self.weights[i]
                if height != 0.:
                    f.write('{},{:5.2f},{:5.2f},{:5.2f}\n'.format(i, height, weight, weight/((height/100)**2)))
            f.close()

    def on_exit( self, event ):
        print('exit')
        self.Destroy()
        
    def on_about_open( self, event ):
        if self.about_box == None:
            self.about_box = UserDialogAbout(self)
        self.about_box.ShowModal()

    def on_name_select( self, event ):
        selection=self.m_comboBox1.GetSelection()
        if selection != wx.NOT_FOUND:
            name=self.m_comboBox1.GetItems()[selection]
            self.m_spinCtrlDouble1.Value=self.heights[name]
            self.m_spinCtrlDouble2.Value=self.weights[name]
        self._bmi_update()

    def on_name_entered( self, event ):
        name=self.m_comboBox1.GetValue()
        self.m_comboBox1.Append(name)
        self.heights[name]=self.m_spinCtrlDouble1.Value
        self.weights[name]=self.m_spinCtrlDouble2.Value
        self._bmi_update()
        
    def on_height_spin( self, event ):
        selection=self.m_comboBox1.GetSelection()
        if selection != wx.NOT_FOUND:
            name=self.m_comboBox1.GetItems()[selection]
            self.heights[name]=self.m_spinCtrlDouble1.Value
        self._bmi_update()

    def on_height_entered( self, event ):
        self.m_spinCtrlDouble1.Disable()  # Hack to update Value
        self.m_spinCtrlDouble1.Enable()   #
        self.m_spinCtrlDouble1.SetFocus() #
        selection=self.m_comboBox1.GetSelection()
        if selection != wx.NOT_FOUND:
            name=self.m_comboBox1.GetItems()[selection]
            self.heights[name]=self.m_spinCtrlDouble1.Value
        self._bmi_update()

    def on_weight_spin( self, event ):
        selection=self.m_comboBox1.GetSelection()
        if selection != wx.NOT_FOUND:
            name=self.m_comboBox1.GetItems()[selection]
            self.weights[name]=self.m_spinCtrlDouble2.Value
        self._bmi_update()

    def on_weight_entered( self, event ):
        self.m_spinCtrlDouble2.Disable()  # Hack to update Value
        self.m_spinCtrlDouble2.Enable()   #
        self.m_spinCtrlDouble2.SetFocus() #
        selection=self.m_comboBox1.GetSelection()
        if selection != wx.NOT_FOUND:
            name=self.m_comboBox1.GetItems()[selection]
            self.weights[name]=self.m_spinCtrlDouble2.Value
        self._bmi_update()

    def _bmi_update(self):
        height = self.m_spinCtrlDouble1.Value
        weight = self.m_spinCtrlDouble2.Value
        if height != 0.:
            bmi = weight/((height/100)**2)
            self.m_staticText1.Label='{:5.2f}'.format(bmi)
        else:
            self.m_staticText1.Label='Error'
        if bmi < 18.5:
            self.m_staticText6.Label = 'Underweight'
            self.m_bitmap1.SetBitmap(wx.Bitmap('red.png'))
        elif bmi > 24:
            self.m_staticText6.Label = 'Overweight'
            self.m_bitmap1.SetBitmap(wx.Bitmap('red.png'))
        else:
            self.m_staticText6.Label = 'Normal'
            self.m_bitmap1.SetBitmap(wx.Bitmap('green.png'))


class UserDialogAbout(BuilderDialogAbout):
    def __init__(self, parent):
        BuilderDialogAbout.__init__(self, parent)
        self.parent = parent

    def on_about_close( self, event ):
        self.parent.about_box = None
        self.Destroy()


class BMIApp(wx.App):
    def __init__(self):
        super(BMIApp, self).__init__(redirect=False)
        self.main_window = UserFrameMain(None)
        self.SetTopWindow(self.main_window)
        self.main_window.Show()


if __name__ == '__main__':
    BMIApp().MainLoop()