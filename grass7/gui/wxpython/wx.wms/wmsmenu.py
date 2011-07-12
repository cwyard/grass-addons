#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Jul 11 04:58:20 2011

import wx
from wxPython.wx import *
from urllib2 import Request, urlopen, URLError, HTTPError
from parse import parsexml
from WMSMapDisplay import NewImageFrame

# begin wxGlade: extracode
# end wxGlade



class wmsFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wmsFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.URL = wx.StaticText(self, -1, "URL")
        self.ServerList = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_SIMPLE)
        self.LayerTree = wx.TreeCtrl(self, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.GetCapabilities = wx.Button(self, -1, "GetCapabilities")
        self.GetMaps = wx.Button(self, -1, "GetMaps")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.OnServerListEnter, self.ServerList)
        self.Bind(wx.EVT_COMBOBOX, self.OnServerList, self.ServerList)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnLayerTreeSelChanged, self.LayerTree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnLayerTreeActivated, self.LayerTree)
        self.Bind(wx.EVT_BUTTON, self.OnGetCapabilities, self.GetCapabilities)
        self.Bind(wx.EVT_BUTTON, self.OnGetMaps, self.GetMaps)
        # end wxGlade
        
        #Sudeep's Code Starts
        #self.urlInput.SetValue('http://www.gisnet.lv/cgi-bin/topo')
        f = open('serverList.txt','r')
        lines = f.readlines()
        self.servers = {}
        for line in lines:
            row = line.split()
            if(len(row) == 2) :
	            self.servers[row[0]] = row[1]
            name = row[0]+" "+row[1][7:45]
            self.ServerList.Append(name)
        f.close()
        self.selectedURL="No server selected"
        self.layerTreeRoot = self.LayerTree.AddRoot("Layers")
        items = ["a", "b", "c"]
        #itemId = self.LayerTree.AppendItem(self.layerTreeRoot, "item")
        #self.LayerTree.AppendItem(itemId, "inside")
        #Sudeep's Code Ends
    def __set_properties(self):
        # begin wxGlade: wmsFrame.__set_properties
        self.SetTitle("wmsFrame")
        self.LayerTree.SetMinSize((400, 250))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wmsFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.URL, 0, 0, 0)
        sizer_3.Add(self.ServerList, 0, 0, 0)
        sizer_2.Add(sizer_3, 0, 0, 0)
        sizer_2.Add(self.LayerTree, 1, wx.EXPAND, 0)
        sizer_4.Add(self.GetCapabilities, 0, 0, 0)
        sizer_4.Add(self.GetMaps, 0, 0, 0)
        sizer_2.Add(sizer_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(sizer_2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
    

    def OnGetCapabilities(self, event): # wxGlade: wmsFrame.<event_handler>
        #Sudeep's Code Starts
        #url = 'http://www.gisnet.lv/cgi-bin/topo?request=GetCapabilities&service=wms&version=1.1.1'
    	#url = self.urlInput.GetValue()
    	url = self.selectedURL
    	url = url + '?request=GetCapabilities&service=wms&version=1.1.1'
    	print url
	req = Request(url)
	try:
	    response = urlopen(req)
	    xml = response.read()
	    #self.statusbar.SetStatusText(xml) 
	    reslist = parsexml(xml)
	    st = ''
	    for res in reslist:
	    	   st = st + res + '\n'
	    	   self.LayerTree.AppendItem(self.layerTreeRoot, res)
	    #self.Layers.SetValue(st) 
	    #print xml
	except HTTPError, e:
	    print 'The server couldn\'t fulfill the request.'
	    print 'Error code: ', e.code
	except URLError, e: 
	    print 'We failed to reach a server.'
	    print 'Reason: ', e.reason
	else:
	    print 'Successful'
	    #Sudeep's Code Ends
        event.Skip()

    def OnGetMaps(self, event): # wxGlade: wmsFrame.<event_handler>
        #Sudeep's Code Starts
        #self.layerName = self.layerSelected.GetValue()
        #url = self.urlInput.GetValue()
    	
    	self.url_in = self.selectedURL
        getMap_request_url = self.url_in+'?service=WMS&request=GetMap&version=1.1.1&format=image/png&width=800&height=600&srs=EPSG:3059&layers='+self.layerName+'&bbox=584344,397868,585500,398500'
        
        
        
	print getMap_request_url
	
	req = Request(getMap_request_url)
	try:
	    response = urlopen(req)
	    image = response.read()
	    outfile = open('map.png','wb')
	    outfile.write(image)
	    outfile.close()
	    
	    
	    NewImageFrame()
	    
	    
	except HTTPError, e:
	    print 'The server couldn\'t fulfill the request.'
	    print 'Error code: ', e.code
	except URLError, e:
	    print 'We failed to reach a server.'
	    print 'Reason: ', e.reason
	else:
	    print 'Successful'
        #Sudeep's Code Ends
        event.Skip()

    def OnServerListEnter(self, event): # wxGlade: wmsFrame.<event_handler>
        print "Event handler `OnServerListEnter' not implemented"
        #Sudeep's Code Starts
        print self.ServerList.CurrentSelection
        newUrl = self.ServerList.GetValue()
        self.ServerList.Append(newUrl)
        
        url = newUrl.split()
        if(len(url)==2):
            self.servers[url[0]] = url[1]
            f = open('serverList.txt','a')
            f.write(newUrl+"\n")
            f.close()
            self.selectedURL = url[1]
            print self.selectedURL
            print self.servers
  
        else:
            print "Format not recognized, Format: Severname URL"
        #Sudeep's Code Ends
        event.Skip()

    def OnServerList(self, event): # wxGlade: wmsFrame.<event_handler>
        print "Event handler `OnServerList' not implemented"
        #Sudeep's Code Starts
        print self.ServerList.CurrentSelection
        url = self.ServerList.GetValue()
        urlarr = url.split()
        if(len(urlarr)==2):
            self.selectedURL = self.servers[urlarr[0]]
            print self.selectedURL
        else:
            print "Wrong format of URL selected"
        #Sudeep's Code Ends
        event.Skip()

    def OnLayerTreeActivated(self, event): # wxGlade: wmsFrame.<event_handler>
        #Sudeep's Code Starts
        print "OnLayerTreeActivated: ", self.LayerTree.GetItemText(event.GetItem())
        #Sudeep's Code Ends
        print "Event handler `OnLayerTreeActivated' not implemented"
        event.Skip()

    def OnLayerTreeSelChanged(self, event): # wxGlade: wmsFrame.<event_handler>
        self.layerName = self.LayerTree.GetItemText(event.GetItem())
        print "Event handler `OnLayerTreeSelChanged' not implemented"
        
        event.Skip()

# end of class wmsFrame

#Sudeep's Code Starts
def DisplayWMSMenu():
     	app = wx.PySimpleApp(0)
    	wx.InitAllImageHandlers()
    	wms_Frame = wmsFrame(None, -1, "")
   	app.SetTopWindow(wms_Frame)
    	wms_Frame.Show()
    	app.MainLoop()
#Sudeep's Code Ends

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    wms_Frame = wmsFrame(None, -1, "")
    app.SetTopWindow(wms_Frame)
    wms_Frame.Show()
    app.MainLoop()
