import tkinter as tk
import re

from tkinter import messagebox

class GUI:

    def __init__(self):


        #init
        self.Root = tk.Tk()
        self.Root.title("Milo Label Editor")
        self.UILabelIsShowing_state = tk.IntVar()
        self.VerificationFail = 0

        #the setup for the drop down menu
        self.UIComponentList = [
            "UILabel",
            "BandLabel",
            "HamLabel"
        ]

        self.DefaultUIComp = tk.StringVar(self.Root)
        self.DefaultUIComp.set(self.UIComponentList[0]) 

        #shit for menu bar and the shit in it.
        self.MenuBar = tk.Menu(self.Root)
        self.FileMenu = tk.Menu(self.MenuBar, tearoff=0)
        self.FileMenu.add_command(label="Exit", command=exit)
        self.MenuBar.add_cascade(menu=self.FileMenu,label="File")

        self.Root.config(menu=self.MenuBar)

        #Labels
        self.LabelNameLabel = tk.Label(self.Root, text=".lbl")
        self.GroupFileTypeLabel = tk.Label(self.Root, text=".grp")
        self.TextSizePercent = tk.Label(self.Root, text="%")
        #-
        self.NameDesc = tk.Label(self.Root, text="The name of the label?")
        self.TypeDesc = tk.Label(self.Root, text="The Type of label, UILabel is availble in all games but is limited.\n HamLabel and BandLabel are only availible in DC and RB.")
        self.ShowingDesc = tk.Label(self.Root, text="Set Showing?")
        self.TextTokenEntryDesc = tk.Label(self.Root, text="What token should be used for locale?")
        self.TextSizeDesc = tk.Label(self.Root, text="Text size in percentage of screen height (i.e. \n50% is half the screen height for the largest glyph)")
        self.GroupDesc = tk.Label(self.Root, text="What is the group the label should be added to.")


        #all the other shit
        self.UILabelEntry = tk.Entry(self.Root, width=15)
        self.UIComponent = tk.OptionMenu(self.Root, self.DefaultUIComp, *self.UIComponentList)
        self.UILabelIsShowing = tk.Checkbutton(self.Root, variable=self.UILabelIsShowing_state)
        self.TextTokenEntry = tk.Entry(self.Root, width=15)
        self.TextSizeEntry = tk.Entry(self.Root, width=7)





        self.GroupEntry = tk.Entry(self.Root, width=15)
        self.GenerateButton = tk.Button(self.Root, text="Generate Script", command=self.GenerateLabelCode)
        

        #run column 0 objects
        self.NameDesc.grid(row=0, column=0, padx=10, pady=10)
        self.TypeDesc.grid(row=1, column=0, padx=10, pady=10)
        self.ShowingDesc.grid(row=2, column=0, padx=10, pady=10)
        self.TextTokenEntryDesc.grid(row=3, column=0, padx=10, pady=10)
        self.TextSizeDesc.grid(row=4, column=0, padx=10, pady=10)
        self.GroupDesc.grid(row=5, column=0, padx=10, pady=10)

        #run column 1 objects
        self.UILabelEntry.grid(row=0, column=1, pady=10)
        self.UIComponent.grid(row=1, column=1)
        self.UILabelIsShowing.grid(row=2, column=1,padx=10, pady=10)
        self.TextTokenEntry.grid(row=3, column=1, padx=10, pady=10)
        self.TextSizeEntry.grid(row=4, column=1, padx=10, pady=10)

        self.GroupEntry.grid(row=5, column=1, pady=10)
        self.GenerateButton.grid(row=6, column=1, padx=10, pady=10)

        #run column 2 objects
        self.LabelNameLabel.grid(sticky="w", row=0, column=2, pady=10)
        self.TextSizePercent.grid(sticky="w",row=4, column=2, pady=10)  
        self.GroupFileTypeLabel.grid(sticky="w",row=5, column=2, pady=10)

        #run the code
        self.Root.mainloop()


    def VerifyData(self, string, error):
        if re.match(r'^[A-Za-z_]+$', string):
            return
        else:
            messagebox.showerror("Error",error)
            self.VerificationFail = 1

    def VerifyNumbers(self, NumEntry, error):
            try:
            int(NumEntry)
            if int(NumEntry) < 0:
                FailOnPurpose = 10 / 0
            return
        except (ZeroDivisionError, ValueError):
            messagebox.showerror("Error",error)
            self.VerificationFail = 1

    def PullData(self):
        self.UILabelEntry_Print = self.UILabelEntry.get()
        self.GroupEntry_Print = self.GroupEntry.get()
        self.text_token_Print = self.TextTokenEntry.get()
        self.Text_Size_Print = self.TextSizeEntry.get()

        self.VerifyData(self.UILabelEntry_Print, "Invalid LabelName")
        self.VerifyData(self.text_token_Print, "Invalid Text Token Name")
        self.VerifyNumbers(self.Text_Size_Print,"Invalid Text Size Value")
        self.VerifyData(self.GroupEntry_Print, "Invalid Group Name")

    def GenerateLabelCode(self):
        self.VerificationFail = 0
        self.PullData()
        if self.VerificationFail == 0:
            open("lbl_out.dta", "w+").write(f"{{new {self.DefaultUIComp.get()} {self.UILabelEntry.get()}.lbl}}")
            open("lbl_out.dta", "a").write(f"\n{{{self.UILabelEntry.get()}.lbl set_showing {self.UILabelIsShowing_state.get()}}}")
            open("lbl_out.dta", "a").write(f"\n{{{self.UILabelEntry.get()}.lbl set_text_token {self.TextTokenEntry.get()}}}")
            open("lbl_out.dta", "a").write(f"\n{{{self.GroupEntry.get()}.grp add_object {self.UILabelEntry.get()}.lbl}}")
        else:
            return
GUI()