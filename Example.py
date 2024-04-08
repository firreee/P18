sw=0
aline=''
def closewin(mainwin):
    mainwin.destroy()
def deleteobj(wcan):
    global aline,sw
    wcan.delete(aline)
    wcan.update()
    sw=0
    return
def drawline(wcan,y,cw,ch):
    global aline,sw
    if sw==0:
        aline=wcan.create_line(0, y, cw, y, width=10, fill="black")
        wcan.update()
        sw=1
        return 
def main():
    sw=1
    mainwin = Tk()
    mainwin.title("Windows and canvas")
    mainwin.geometry('800x600')
    cw = 600
    ch = 400
    wcan = Canvas(mainwin,bg='yellow', bd=5,width=cw, height=ch)
    y = int(ch / 2)
    drawline(wcan,y,cw,ch)
    wcan.grid(row=2,column=1)
    cmdbut = Button(mainwin, text="delete line", fg="red",
                    command=lambda : deleteobj(wcan))
    cmdbut.grid(row=0,column=0)
    cmdbut2 = Button(mainwin, text="restore line", fg="purple",
                     command=lambda : drawline(wcan,y,cw,ch))
    cmdbut2.grid(row=0,column=1)
    cmdbut3 = Button(mainwin, text="close Window", fg="green",
                     command=lambda : closewin(mainwin))
    cmdbut3.grid(row=0,column=2)
    mainwin.mainloop()
    main()
