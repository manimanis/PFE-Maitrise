#Boa:Dialog:LcdMsgDialog

import wx
import wx.gizmos
import Messages

def create(parent):
    return LcdMsgDialog(parent)

[wxID_LCDMSGDIALOG, wxID_LCDMSGDIALOGBTNADD, wxID_LCDMSGDIALOGBTNDEL, 
 wxID_LCDMSGDIALOGTREELIST, wxID_LCDMSGDIALOGTXTCONTENU, 
] = [wx.NewId() for _init_ctrls in range(5)]

class LcdMsgDialog(wx.Dialog):
    def _init_coll_treeList_Columns(self, parent):
        # generated method, don't edit

        parent.AddColumn(text=u'Menu')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_LCDMSGDIALOG, name='', parent=prnt,
              pos=wx.Point(596, 282), size=wx.Size(718, 486),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Messages LCD')
        self.SetClientSize(wx.Size(710, 452))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.treeList = wx.gizmos.TreeListCtrl(id=wxID_LCDMSGDIALOGTREELIST,
              name=u'treeList', parent=self, pos=wx.Point(8, 40),
              size=wx.Size(336, 400),
              style=wx.TR_SINGLE | wx.TR_LINES_AT_ROOT | wx.TR_EDIT_LABELS | wx.TR_HAS_BUTTONS)
        self.treeList.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self._init_coll_treeList_Columns(self.treeList)
        self.treeList.Bind(wx.EVT_TREE_SEL_CHANGED,
              self.OnTreeListTreeSelChanged, id=wxID_LCDMSGDIALOGTREELIST)

        self.txtContenu = wx.TextCtrl(id=wxID_LCDMSGDIALOGTXTCONTENU,
              name=u'txtContenu', parent=self, pos=wx.Point(352, 40),
              size=wx.Size(344, 80), style=wx.TE_MULTILINE,
              value=u'0123456789ABCDEF0123456789ABCDEF')
        self.txtContenu.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Courier New'))

        self.btnAdd = wx.Button(id=wxID_LCDMSGDIALOGBTNADD, label=u'Add Child',
              name=u'btnAdd', parent=self, pos=wx.Point(8, 8), size=wx.Size(75,
              23), style=0)
        self.btnAdd.Bind(wx.EVT_BUTTON, self.OnBtnAddButton,
              id=wxID_LCDMSGDIALOGBTNADD)

        self.btnDel = wx.Button(id=wxID_LCDMSGDIALOGBTNDEL,
              label=u'DeleteChild', name=u'btnDel', parent=self,
              pos=wx.Point(88, 8), size=wx.Size(75, 23), style=0)
        self.btnDel.Bind(wx.EVT_BUTTON, self.OnBtnDelButton,
              id=wxID_LCDMSGDIALOGBTNDEL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.initTreeCtrl()
        self.messages = Messages.MessagesCollection()
        
    def initTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeList.SetColumnWidth(0, 250)
        self.treeList.SetImageList(il)
        self.il = il
        
        self.root = self.treeList.AddRoot("Menu Principal")
        self.treeList.SetItemImage(self.root, fileidx, which = wx.TreeItemIcon_Normal)
        self.treeList.SetItemImage(self.root, fileidx, which = wx.TreeItemIcon_Expanded)
        #self.initFromData()
                    
        self.treeList.ExpandAll(self.root)
        
    def initFromData(self):
        data = self.messages.getData()
        
        self.txtItem1.SetLabel(data.getMessage(0))
        self.txtItem2.SetLabel(data.getMessage(1))
        self.txtItem3.SetLabel(data.getMessage(2))
        self.txtItem4.SetLabel(data.getMessage(3))
        
        self.txtPage.SetValue(self.messages.getPos())
        self.txtLabel.SetLabel(self.messages.getLabel())

    def initFromUI(self):
        data = Messages.Message()
        
        data.setMessage(0, self.txtItem1.GetLabel().encode('ascii'))
        data.setMessage(1, self.txtItem2.GetLabel().encode('ascii'))
        data.setMessage(2, self.txtItem3.GetLabel().encode('ascii'))
        data.setMessage(3, self.txtItem4.GetLabel().encode('ascii'))
        
        self.messages.setData(data)

    def OnTreeListTreeSelChanged(self, event):
        if self.treeList.GetSelection().IsOk():
            if event.GetOldItem().IsOk() and (self.treeList.GetRootItem() != event.GetOldItem()):
                self.treeList.SetItemText(event.GetOldItem(), self.txtContenu.GetLabel())
        self.txtContenu.SetLabel(self.treeList.GetItemText(event.GetItem()))

    def OnBtnAddButton(self, event):
        child = self.treeList.AppendItem(self.treeList.GetSelection(), "Item")
        self.treeList.SetItemImage(child, 0, which = wx.TreeItemIcon_Normal)

    def OnBtnDelButton(self, event):
        if self.treeList.GetSelection().IsOk():
            if self.treeList.GetRootItem() != self.treeList.GetSelection():
                self.treeList.DeleteChildren(self.treeList.GetSelection())
                self.treeList.Delete(self.treeList.GetSelection())
            

