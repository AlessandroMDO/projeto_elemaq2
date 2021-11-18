from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedStyle



root = tk.Tk()
root.configure(bg="#373737")
root.title('Pré-dimensionamento de fusos')
root.geometry("800x500")

style = ThemedStyle(root)
style.theme_use("equilux")


s = ttk.Style()
s.configure('Red.TLabelframe.Label', font=('calibri', 10, 'bold'))


font_title = 'Calibri 14 bold'
font_section = 'Calibri 11'

si = [['M3', 3.0, 0.5, 2.39, 5.03],
      ['M3.5', 3.5, 0.6, 2.76, 6.78],
      ['M4', 4.0, 0.7, 3.14, 8.78],
      ['M5', 5.0, 0.8, 4.02, 14.2],
      ['M6', 6.0, 1.0, 4.77, 20.1],
      ['M7', 7.0, 1.0, 5.77, 28.9],
      ['M8', 8.0, 1.25, 6.47, 36.6, 1.0, 6.77, 39.2],
      ['M10', 10.0, 1.5, 8.16, 58.0, 1.25, 8.47, 61.2],
      ['M13', 12.0, 1.75, 9.85, 84.3, 1.25, 10.5, 92.1],
      ['M14', 14.0, 2.0, 11.6, 115.0, 1.5, 12.2, 125.0],
      ['M16', 16.0, 2.0, 13.6, 157.0, 1.5, 14.2, 167.0],
      ['M18', 18.0, 2.5, 14.9, 192.0, 1.5, 16.2, 216.0],
      ['M20', 20.0, 2.5, 16.9, 245.0, 1.5, 18.2, 272.0],
      ['M22', 22.0, 2.5, 18.9, 303.0, 1.5, 20.2, 333.0],
      ['M24', 24.0, 3.0, 20.3, 353.0, 2.0, 21.6, 384.0],
      ['M27', 27.0, 3.0, 23.3, 459.0, 2.0, 24.6, 496.0],
      ['M30', 30.0, 3.5, 25.7, 561.0, 2.0, 27.6, 621.0],
      ['M33', 33.0, 3.5, 28.7, 694.0, 2.0, 30.6, 761.0],
      ['M36', 36.0, 4.0, 31.1, 817.0, 3.0, 32.3, 865.0],
      ['M39', 39.0, 4.0, 34.1, 976.0, 3.0, 35.3, 1030.0]]


su = [['0', 0.06, 0.0, 0.00151],
      ['1', 0.073, 0.00218, 0.00237],
      ['2', 0.086, 0.0031, 0.00339],
      ['3', 0.099, 0.00406, 0.00451],
      ['4', 0.112, 0.00496, 0.00566],
      ['5', 0.125, 0.00672, 0.00716],
      ['6', 0.138, 0.00745, 0.00874],
      ['8', 0.164, 0.01196, 0.01285],
      ['10', 0.19, 0.0145, 0.0175],
      ['12', 0.216, 0.0206, 0.0226],
      ['1/4', 0.25, 0.0269, 0.0326],
      ['5/16', 0.3125, 0.0454, 0.0524],
      ['3/8', 0.375, 0.067, 0.0809],
      ['7/16', 0.4375, 0.0933, 0.109],
      ['1/2', 0.5, 0.1257, 0.1486],
      ['9/16', 0.5625, 0.162, 0.189],
      ['5/8', 0.625, 0.202, 0.24],
      ['3/4', 0.75, 0.302, 0.351],
      ['7/8', 0.875, 0.419, 0.4]]

class D_fuso:
    
    def __init__(self, master):
        self.k_1 = 0
        self.k_2 = 0
        self.k_3 = 0
        self.k_4 = 0
    
#Sistema de Medidas
        self.frame_1 = ttk.LabelFrame(master, text='Sistema de Medidas',style="Red.TLabelframe")
        self.frame_1['relief']='groove'
        self.frame_1['borderwidth']=3
        self.frame_1.place(x=25, y=20)

        self.sistema = tk.StringVar(None)

        self.mult_option_1 = ttk.Radiobutton(self.frame_1, text='Sistema Unificado', 
                                             variable=self.sistema, value='SU')
        self.mult_option_1['command']= self.layout_1
        self.mult_option_1.grid(row=2, sticky=tk.W)

        self.mult_option_2 = ttk.Radiobutton(self.frame_1, text='Sistema Internacional', 
                                             variable=self.sistema, value='SI')
        self.mult_option_2['command'] = self.layout_1
        self.mult_option_2.grid(row=1,sticky=tk.W)
        
        
        
        
        
        






































        
#Creditos
        self.bottomFrame = ttk.Frame(master)
        self.bottomFrame.pack(side=tk.BOTTOM)
        self.bottomFrame.place(rely = 1.0, relx = 1.0, x = -10, y = -5, anchor = tk.SE)
        self.creditos_button = ttk.Button(self.bottomFrame, text='Créditos')
        self.creditos_button['command']=self.onClickCreditos
        self.creditos_button.pack(anchor=tk.S)

    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def layout_1(self):
        if self.k_1 == 1:
            self.label_4.grid_remove()
            self.label_10.grid_remove()
            self.label_17.grid_remove()
            self.label_15.grid_remove()
            self.label_16.grid_remove()
            
        if self.sistema.get() == 'SI':
            self.length = 'mm'
            self.force = 'N'
            self.moment = 'N.m'
            self.time = 's'
            self.potencia = 'kW' 
            self.stress = 'MPa'
            self.parafusos = ['M3','M3.5','M4','M5','M6', 'M7', 'M8', 'M10', 'M12', 'M14', 'M16', 'M18', 'M20',
                               'M22', 'M24', 'M27','M30', 'M33', 'M36', 'M39']
            
            self.label_4 = ttk.Label(self.frame_6, text='[' + self.unit_force + ']')
            self.label_4.grid(row=0, column=2, sticky= tk.W)

            self.label_10 = ttk.Label(self.frame_6, text='[' + self.unit_lenght + '/s]')
            self.label_10.grid(row=1, column=2, sticky=tk.W)

            self.label_15 = ttk.Label(self.frame_4, text='[' + self.unit_stress + ']')
            self.label_15.grid(row=0, column=3)

            self.label_16 = ttk.Label(self.frame_4, text='[' + self.unit_stress + ']')
            self.label_16.grid(row=1, column=3)

            self.label_17 = ttk.Label(self.frame_4, text='[-]')
            self.label_17.grid(row=2, column=3)

            self.k_1 = 1
            
            
    def onClickCreditos(self):
        tk.messagebox.showinfo("Créditos",  "Aluno: Alessandro Melo de Oliveira - NºUSP: 10788662 \nElementos de Máquina SEM0326 - 2021.2")

            
            








D_fuso(root)
root.mainloop()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    