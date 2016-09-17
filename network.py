from ttk import Frame, Label, Style
from Tkinter import *
import tkMessageBox
import AppKit 
import ipaddress



class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("Subnets+")
        self.pack(fill=BOTH, expand=1)
        
        #Fires onSelect function that fills the variables
        lb = Listbox(self)
        lb.bind("<<ListboxSelect>>", self.onSelect)
        #Declares the strings used 
        self.var = StringVar()
        self.var1 = StringVar()
        self.net_str = StringVar()
        self.block_size = StringVar()
        self.usable_size = StringVar()
        self.gateway = StringVar()
        self.bcast = StringVar()
        self.wildcard = StringVar()
        self.addrcont = StringVar()
        #Creates the labels that the strings are displayed in
        go_btn = Button(self, text="Enter", command=lambda:fillNet(net_txtbx, lb, self))
        net_txtbx = Entry(self)
        net_lbl = Label(self, text='Network:')
        net1_lbl = Label(self, text='Network IP:')
        self.ip = Label(self, text=0, textvariable=self.var)
        self.ip_bin = Label(self, text=0, textvariable=self.var1)
        self.ip_net = Label(self, text=0, textvariable=self.net_str)
        self.block1 = Label(self, text=0, textvariable=self.block_size)
        block2 = Label(self, text='Block Size: ')
        self.usable1 = Label(self, text=0, textvariable=self.usable_size)
        usable2 = Label(self, text='Usable Size: ')
        self.gate = Label(self, text=0, textvariable=self.gateway)
        gate1 = Label(self, text='Gateway: ')
        self.bcast1 = Label(self, text=0, textvariable=self.bcast)
        bcast2 = Label(self, text='Broadcast: ')
        wcard = Label(self, text=0, textvariable=self.wildcard)
        wcard1 = Label(self, text='Wildcard: ')
        addrcount = Label(self, text ='# of Addresses: ')
        addrcount1 = Label(self, textvariable=self.addrcont)


        #Placing all the objects that were made in this function
        net_txtbx.place(x=70, y=0)
        net_lbl.place(x=5, y=4)
        go_btn.place(x=245, y=0)
        lb.place(x=20, y=40)
        self.ip.place(x=40, y=220)
        self.ip_bin.place(x=40, y=250)
        self.ip_net.place(x=275, y=40)
        net1_lbl.place(x=190, y=40)
        self.block1.place(x=275, y=60)
        block2.place(x=190, y=60)
        self.usable1.place(x=275, y=80)
        usable2.place(x=190, y=80)
        self.gate.place(x=275, y=100)
        self.bcast1.place(x=275, y=120)
        gate1.place(x=190, y=100)
        bcast2.place(x=190, y=120)
        wcard1.place(x=190, y=140)
        wcard.place(x=275, y=140)
        addrcount.place(x=190, y=160)
        addrcount1.place(x=300, y=160)


    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)  
        self.var.set(value)

        num = (bin(int(ipaddress.IPv4Address(value))))

        num = num.split('b',2)[1]
        l = [''.join(x) for x in zip(*[list(num[z::8]) for z in range(8)])]
        #self.var1.set()


def fillNet(ip, lb, self):
    i = 0;
    if len(ip.get()) == 0:
        tkMessageBox.showinfo("Error", "Enter a Network into the textbox")
    else:
        try:
            add1 = ipaddress.ip_network(ip.get())
            self.addrcont.set(str(add1.num_addresses))
            self.net_str.set(add1)
            lb.delete(0,END)
            for addr in add1:
                lb.insert(i, str(addr))
                i = i + 1
            self.block_size.set(str(i))
            self.usable_size.set(str(i-2))
            self.gateway.set(str(add1.network_address+1))
            self.bcast.set(add1.broadcast_address)
            wc_string = str(add1.with_hostmask)
            wc_string = wc_string.split('/')[1]
            self.wildcard.set(wc_string)

        except ValueError:
            tkMessageBox.showinfo("Error", "This address is not a network address")

def main():
    root = Tk()
    ex = Example(root)
    windowsize = str("400x400" + '+' + str((root.winfo_screenwidth())/2-150) + '+' + str((root.winfo_screenheight())/2-150))
    root.geometry(windowsize)
    root.mainloop()  
  
if __name__ == '__main__':
    main()  


