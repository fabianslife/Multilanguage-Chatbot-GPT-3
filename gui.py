import tkinter as tk
from ada_dialog_functions import main


class BaseFrame(tk.Frame):


    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.grid()
        self.set_language=""
        self.create_widgets()
        self.configure(background='#212124')

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError


class FrameOne(BaseFrame):
    """First page."""

    def create_widgets(self):

        """Create the base widgets for the frame."""
        global english_flag, french_flag,german_flag,italian_flag,spanish_flag,swedish_flag,finnish_flag,dutch_flag,polish_flag,czech_flag,greek_flag,hungarian_flag,chinese_flag,japanese_flag,southkorean_flag

        self.header = tk.Label(self, text="Select your language", font=("Helvetica", 25), justify='center',fg="#ffffff",bg="#212124")
        
        self.header.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        english_flag = tk.PhotoImage(file=f"app/gui/english_flag.png")
        french_flag = tk.PhotoImage(file=f"app/gui/french_flag.png")
        german_flag = tk.PhotoImage(file=f"app/gui/german_flag.png")
        italian_flag = tk.PhotoImage(file=f"app/gui/italian_flag.png")
        spanish_flag = tk.PhotoImage(file=f"app/gui/spanish_flag.png")
        swedish_flag = tk.PhotoImage(file=f"app/gui/swedish_flag.png")
        finnish_flag = tk.PhotoImage(file=f"app/gui/finnish_flag.png")
        dutch_flag = tk.PhotoImage(file=f"app/gui/dutch_flag.png")
        polish_flag = tk.PhotoImage(file=f"app/gui/polish_flag.png")
        czech_flag = tk.PhotoImage(file=f"app/gui/czech_flag.png")
        greek_flag = tk.PhotoImage(file=f"app/gui/greek_flag.png")
        hungarian_flag = tk.PhotoImage(file=f"app/gui/hungarian_flag.png")
        chinese_flag = tk.PhotoImage(file=f"app/gui/chinese_flag.png")
        japanese_flag = tk.PhotoImage(file=f"app/gui/japanese_flag.png")
        southkorean_flag = tk.PhotoImage(file=f"app/gui/southkorean_flag.png")
        self.button_english = tk.Button(self,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    image=english_flag,
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("EN")],
                                    text="english")
        self.button_english.grid(row = 1, column = 1, padx= 20, pady=20)
        self.button_german = tk.Button(self,
                                    image=german_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("DE")],    
                                    text="German")
        self.button_german.grid(row = 1, column = 2, padx= 20, pady=20)
        self.button_french = tk.Button(self,
                                    image=french_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("FR")],    
                                    text="french")
        self.button_french.grid(row = 1, column = 3, padx= 20, pady=20)
        self.button_italian = tk.Button(self,
                                    image=italian_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("IT")],    
                                    text="french")
        self.button_italian.grid(row = 1, column = 4, padx= 20, pady=20)
        self.button_spanish = tk.Button(self,
                                    image=spanish_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("ES")],    
                                    text="french")
        self.button_spanish.grid(row = 1, column = 5, padx= 20, pady=20)
        self.button_swedish = tk.Button(self,
                                    image=swedish_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("SW")],    
                                    text="swedish")
        self.button_swedish.grid(row = 2, column = 1, padx= 20, pady=20)
        self.button_finnish = tk.Button(self,
                                    image=finnish_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("FI")],    
                                    text="finnish")
        self.button_finnish.grid(row = 2, column = 2, padx= 20, pady=20)
        self.button_dutch = tk.Button(self,
                                    image=dutch_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("NL")],    
                                    text="dutch")
        self.button_dutch.grid(row = 2, column = 3, padx= 20, pady=20)
        self.button_polish = tk.Button(self,
                                    image=polish_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("PL")],    
                                    text="polish")
        self.button_polish.grid(row = 2, column = 4, padx= 20, pady=20)
        self.button_czech = tk.Button(self,
                                    image=czech_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("CS")],    
                                    text="finnish")
        self.button_czech.grid(row = 2, column = 5, padx= 20, pady=20)
        self.button_greek = tk.Button(self,
                                    image=greek_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("EL")],    
                                    text="greek")
        self.button_greek.grid(row = 3, column = 1, padx= 20, pady=20)
        self.button_hungarian = tk.Button(self,
                                    image=hungarian_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("HU")],    
                                    text="hungarian")
        self.button_hungarian.grid(row = 3, column = 2, padx= 20, pady=20)
        self.button_chinese = tk.Button(self,
                                    image=chinese_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("ZH")],    
                                    text="chinese")
        self.button_chinese.grid(row = 3, column = 3, padx= 20, pady=20)
        self.button_japanese = tk.Button(self,
                                    image=japanese_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("JA")],    
                                    text="japanese")
        self.button_japanese.grid(row = 3, column = 4, padx= 20, pady=20)
        self.button_southkorean = tk.Button(self,
                                    image=southkorean_flag,
                                    relief="groove",
                                    highlightbackground="#f2f2f2",
                                    highlightcolor="#dddddd",
                                    command=lambda: [self.controller.show_frame(FrameThree),self.select_language("FI")],    
                                    text="southkorean")
        self.button_southkorean.grid(row = 3, column = 5, padx= 20, pady=20)

    def select_language(self,language):
        global set_language
        set_language=language
        #print(self.set_language)

class FrameThree(BaseFrame):
    """Third page."""

    def create_widgets(self):
        global red_cross_flag, anything_flag
        red_cross_flag = tk.PhotoImage(file=f"app/gui/redcross_flag.png")
        anything_flag = tk.PhotoImage(file=f"app/gui/anything.png")
        """Create the base widgets for the frame."""
        self.button_two = tk.Button(self,
                                    image=red_cross_flag,
                                    #command=lambda: threading.Thread(target=self.run_chatbot()).start(),
                                    command=lambda: main(set_language,"doctor"),
                                    padx=5,
                                    pady=5,
                                    text="Doctor")
        self.button_two.grid(row = 1, column = 3,padx=5, pady=5)
        self.button_one = tk.Button(self,
                                    image=anything_flag,
                                    command=lambda: main(set_language,"anything"),
                                    padx=5,
                                    pady=5,
                                    text="Anything")
        self.button_one.grid(row = 2, column = 3,padx=5, pady=5)
        self.button_back = tk.Button(self,
                                     command=lambda: self.controller.show_frame(FrameOne),
                                     padx=5,
                                     pady=5,
                                     text="Back")
        self.button_back.grid(row = 3, column = 3,padx=5, pady=5)

    #def run_chatbot(self):
        #main("EN", "anything")

    #def select_setting(self,setting):
        #self.settings["setting"]=setting
        #print(self.settings)


class PythonGUI(tk.Tk):
    """The main window of the GUI.

    Attributes:
      container (tk.Frame): The frame container for the sub-frames.
      frames (dict of tk.Frame): The available sub-frames.

    """

    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Python GUI")
        self.create_widgets()
        self.resizable(0, 0)

    def create_widgets(self):
        """Create the widgets for the frame."""             
        #   Frame Container
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0)

        #   Frames
        self.frames = {}
        for f in (FrameOne, FrameThree): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row=3, column=5, sticky=tk.NW+tk.SE)
            self.frames[f] = frame
        self.show_frame(FrameOne)

    def show_frame(self, cls):
        """Show the specified frame.

        Args:
          cls (tk.Frame): The class of the frame to show. 

        """
        self.frames[cls].tkraise()

if __name__ == "__main__":
    app = PythonGUI()
    app.mainloop()
    exit()