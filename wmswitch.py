#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import sys
import gtk
#EndImports

class iscApp1:
 iscVThePath2 = ""
 iscVThePath1 = ""
 iscVThePath0 = ""
 iscVreplace = " --replace"
 iscVunity = "unity"
 iscVmetacity = "metacity"
 iscVcompiz = "compiz"
 iscVTheCommand = ""
 iscVThePath = ""
 iscWindow5Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow5Window1Fixed = gtk.Fixed()
 iscWindow5Label0 =gtk.Label("This program switches window managers.")
 iscWindow5TextBox0 = gtk.Entry()
 iscWindow5Label10 =gtk.Label("...Or select from a predefined list.")
 iscWindow5compiz0 = gtk.Button("Switch to 'compiz'")
 iscWindow5metacity0 = gtk.Button("Switch to 'metacity'")
 iscWindow5unity0 = gtk.Button("Switch to 'unity'")
 iscWindow5Label20 =gtk.Label("Created by PizzaDude")
 iscWindow5Button0 = gtk.Button("Switch to custom")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscCombineText2():
 thisiscApp1.iscVTheCommand = thisiscApp1.iscVcompiz + thisiscApp1.iscVreplace
 iscRunShellScript8()
 #iscCombineText2Done


def iscAppQuit7():
 thisiscApp1.destroy(None,None)
 #iscAppQuit7Done


def iscRunShellScript8():
 os.system(thisiscApp1.iscVTheCommand)
 #iscRunShellScript8Done


def iscCombineText9():
 thisiscApp1.iscVTheCommand = thisiscApp1.iscVunity + thisiscApp1.iscVreplace
 iscRunShellScript10()
 #iscCombineText9Done


def iscRunShellScript10():
 os.system(thisiscApp1.iscVTheCommand)
 iscCloseWindow14()
 #iscRunShellScript10Done


def iscCombineText11():
 thisiscApp1.iscVTheCommand = thisiscApp1.iscVmetacity + thisiscApp1.iscVreplace
 iscRunShellScript12()
 #iscCombineText11Done


def iscRunShellScript12():
 os.system(thisiscApp1.iscVTheCommand)
 #iscRunShellScript12Done


def iscCloseWindow14():
 thisiscApp1.iscWindow5Window1.destroy()
 #iscCloseWindow14Done


def iscRunShellScript4():
 os.system(thisiscApp1.iscVTheCommand)
 #iscRunShellScript4Done


def iscCombineText3():
 thisiscApp1.iscVTheCommand = thisiscApp1.iscVThePath + thisiscApp1.iscVreplace
 iscRunShellScript4()
 #iscCombineText3Done


def iscGetTextBox1():
 thisiscApp1.iscVThePath = thisiscApp1.iscWindow5TextBox0.get_text()
 iscCombineText3()
 #iscGetTextBox1Done


def iscWindow5():
 thisiscApp1.iscWindow5Label0 =gtk.Label("This program switches window managers.")
 thisiscApp1.iscWindow5TextBox0 = gtk.Entry()
 thisiscApp1.iscWindow5Label10 =gtk.Label("...Or select from a predefined list.")
 thisiscApp1.iscWindow5compiz0 = gtk.Button("Switch to 'compiz'")
 thisiscApp1.iscWindow5metacity0 = gtk.Button("Switch to 'metacity'")
 thisiscApp1.iscWindow5unity0 = gtk.Button("Switch to 'unity'")
 thisiscApp1.iscWindow5Label20 =gtk.Label("Created by PizzaDude")
 thisiscApp1.iscWindow5Button0 = gtk.Button("Switch to custom")
 thisiscApp1.iscWindow5Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow5Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow5Window1.set_title("Window Manager Switcher")
 thisiscApp1.iscWindow5Window1.set_default_size(316, 240)
 thisiscApp1.iscWindow5Window1.add(thisiscApp1.iscWindow5Window1Fixed)
 thisiscApp1.iscWindow5Window1Fixed.width = 316
 thisiscApp1.iscWindow5Window1Fixed.height = 240
 thisiscApp1.iscWindow5Window1.connect("delete_event", iscWindow5Closed)
 thisiscApp1.iscWindow5Window1Fixed.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5Label0, 14, 13)
 thisiscApp1.iscWindow5Label0.set_size_request(291, 26)
 thisiscApp1.iscWindow5Label0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5TextBox0, 20, 39)
 thisiscApp1.iscWindow5TextBox0.set_text("Type your custom window manager")
 thisiscApp1.iscWindow5TextBox0.set_size_request(243, 25)
 thisiscApp1.iscWindow5TextBox0.connect("changed", iscWindow5TextBoxChanged)
 thisiscApp1.iscWindow5TextBox0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5Label10, 13, 64)
 thisiscApp1.iscWindow5Label10.set_size_request(258, 28)
 thisiscApp1.iscWindow5Label10.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5compiz0, 18, 89)
 thisiscApp1.iscWindow5compiz0.set_size_request(194, 25)
 thisiscApp1.iscWindow5compiz0.connect("clicked", iscWindow5compizClicked)
 thisiscApp1.iscWindow5compiz0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5metacity0, 17, 146)
 thisiscApp1.iscWindow5metacity0.set_size_request(194, 24)
 thisiscApp1.iscWindow5metacity0.connect("clicked", iscWindow5metacityClicked)
 thisiscApp1.iscWindow5metacity0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5unity0, 18, 116)
 thisiscApp1.iscWindow5unity0.set_size_request(193, 26)
 thisiscApp1.iscWindow5unity0.connect("clicked", iscWindow5unityClicked)
 thisiscApp1.iscWindow5unity0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5Label20, 166, 219)
 thisiscApp1.iscWindow5Label20.set_size_request(146, 20)
 thisiscApp1.iscWindow5Label20.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5Button0, 17, 174)
 thisiscApp1.iscWindow5Button0.set_size_request(195, 24)
 thisiscApp1.iscWindow5Button0.connect("clicked", iscWindow5ButtonClicked)
 thisiscApp1.iscWindow5Button0.show()
 thisiscApp1.iscWindow5Window1.show()
 #iscWindow5Opened
 #iscWindow5Done


def iscWindow5Closed(self, other):
 pass
 iscAppQuit7()
 #iscWindow5Closed


def iscWindow5TextBoxChanged(self):
 pass
 #iscWindow5TextBoxChanged


def iscWindow5compizClicked(self):
 pass
 iscCombineText2()
 #iscWindow5compizClicked


def iscWindow5metacityClicked(self):
 pass
 iscCombineText11()
 #iscWindow5metacityClicked


def iscWindow5unityClicked(self):
 pass
 iscCombineText9()
 #iscWindow5unityClicked


def iscWindow5ButtonClicked(self):
 pass
 iscGetTextBox1()
 #iscWindow5ButtonClicked


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow5()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()