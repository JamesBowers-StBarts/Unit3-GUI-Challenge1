from tkinter import *

main=Tk()

title_frame=Frame(main, bg="blue")
title_frame.grid(row=0,column=0,sticky=E+W+S+N)
title=Label(title_frame, text="test")
title.grid(row=1,column=0)

output_frame=Frame(main)
output_frame.grid(row="0",column="0",sticky=E+W+S+N)



main.rowconfigure(0,minsize = 100,weight=0)
main.rowconfigure(1,minsize = 400,weight=1)
main.columnconfigure(0,minsize = 500,weight=1)


title_frame.columnconfigure(0,minsize = 200,weight=1)
title_frame.rowconfigure(0,minsize = 200)
output_frame.columnconfigure(0,minsize = 200,weight=1)
 
main.mainloop()