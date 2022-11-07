import tkinter as tk



class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.barraMenu = tk.Menu(self.nossaTela)
        self.nossaTela.config(menu=self.barraMenu)
        self.barraMenu.add_command(label='arquivo')
        self.nossaTela.config(menu=self.barraMenu)
        self.barraMenu.add_command(label='cadastro', command=self.abrir_janela)
        self.nossaTela.config(menu=self.barraMenu)
        self.barraMenu.add_command(label='help', command=self.abrir_janela2)
        self.bg2 = tk.PhotoImage(file="../trabalho 50pontos/download (1).png")
        self.label12 = tk.Label(self.nossaTela, image=self.bg2)
        self.label12.place(x=20, y=20)
        self.nossaTela.geometry('300x300')

    def abrir_janela(self):
        janela2 = tk.Toplevel()
        janela2.title('CADASTRO FUNCIONARIO')
        janela2.geometry('600x600')



        self.label1 = tk.Label(janela2, width=10, height=3, text='Código:', font='Arial 13 bold', fg='black')
        self.label2 = tk.Label(janela2, width=10, height=3, text='Nome:', font='Arial 13 bold', fg='black')
        self.label3 = tk.Label(janela2, width=10, height=3, text='Estado:', font='Arial 13 bold', fg='black')
        self.label4 = tk.Label(janela2, width=10, height=3, text='Cidade:', font='Arial 13 bold', fg='black')
        self.label5 = tk.Label(janela2, width=10, height=3, text='Bairro:', font='Arial 13 bold', fg='black')
        self.label6 = tk.Label(janela2, width=10, height=3, text='logradouro:', font='Arial 13 bold', fg='black')
        self.label7 = tk.Label(janela2, width=11, height=3, text='Complemento:', font='Arial 13 bold', fg='black')
        self.label8 = tk.Label(janela2, width=20, height=1, text='cadastro do funcionario', font='Arial 10 bold', fg='black')

        self.label1.place(x=10, y=30, )
        self.label2.place(x=10, y=105)
        self.label3.place(x=10, y=175)
        self.label4.place(x=10, y=252)
        self.label5.place(x=10, y=325)
        self.label6.place(x=10, y=398)
        self.label7.place(x=10, y=470)
        self.label8.place(x=250, y=5)

        self.entry4 = tk.Entry(janela2, width=17, font='Arial 13 bold', fg='black')
        self.entry5 = tk.Entry(janela2, width=50, font='Arial 13 bold', fg='black')
        self.entry6 = tk.Entry(janela2, width=30, font='Arial 13 bold', fg='black')
        self.entry7 = tk.Entry(janela2, width=50, font='Arial 13 bold', fg='black')
        self.entry8 = tk.Entry(janela2, width=50, font='Arial 13 bold', fg='black')
        self.entry9 = tk.Entry(janela2, width=50, font='Arial 13 bold', fg='black')
        self.entry10 = tk.Entry(janela2, width=30, font='Arial 13 bold', fg='black')

        self.entry4.place(x=130, y=45)
        self.entry5.place(x=130, y=120)
        self.entry6.place(x=130, y=190)
        self.entry7.place(x=130, y=267)
        self.entry8.place(x=130, y=340)
        self.entry9.place(x=130, y=418)
        self.entry10.place(x=130, y=485)

        self.botao1 = tk.Button(janela2, width=10, font='Arial 13', text='novo', relief='raised', fg='blue')
        self.botao2 = tk.Button(janela2, width=10, font='Arial 13', text='salvar', relief='raised', fg='blue')
        self.botaovoltar = tk.Button(janela2,width=10, font='Arial 13', relief='raised', fg='blue', text='fechar', command=janela2.destroy)

        self.botao1.place(x=250, y=520)
        self.botao2.place(x=355, y=520)
        self.botaovoltar.place(x=465, y=520)

    def abrir_janela2(self):
        janela3 = tk.Toplevel()
        janela3.title('HELP')
        janela3.geometry('400x400')

        self.botaovoltar = tk.Button(janela3, text='fechar a janela', command=janela3.destroy)
        self.botaovoltar.place(x=300, y=360)

        self.label1 = tk.Label(janela3, width=15, height=2, text='Edição do sistema:', font='Arial 13 bold', fg='black')
        self.label2 = tk.Label(janela3, width=15, height=2, text='Versão do sistema:', font='Arial 13 bold', fg='black')
        self.label3 = tk.Label(janela3, width=15, height=2, text='Instalado em:', font='Arial 13 bold', fg='black')
        self.label4 = tk.Label(janela3, width=17, height=2, text='Nome do dispositivo:', font='Arial 13 bold', fg='black')
        self.label5 = tk.Label(janela3, width=15, height=2, text='Tipo de sistema:', font='Arial 13 bold', fg='black')

        self.label1.place(x=10, y=30)
        self.label2.place(x=10, y=95)
        self.label3.place(x=10, y=150)
        self.label4.place(x=10, y=215)
        self.label5.place(x=10, y=280)

        self.label6 = tk.Label(janela3, width=15, height=2, text='2022 topversion', font='Arial 10 ', fg='dark gray')
        self.label7 = tk.Label(janela3, width=15, height=2, text='1.0', font='Arial 10 ', fg='dark gray')
        self.label8 = tk.Label(janela3, width=15, height=2, text='07/11/2022', font='Arial 10 ', fg='dark gray')
        self.label9 = tk.Label(janela3, width=15, height=2, text='UserPc', font='Arial 10 ', fg='dark gray')
        self.label10 =tk.Label(janela3, width=15, height=2, text='65x', font='Arial 10 ', fg='dark gray')


        self.label6.place(x=170, y=35)
        self.label7.place(x=170, y=100)
        self.label8.place(x=170, y=155)
        self.label9.place(x=190, y=220)
        self.label10.place(x=170, y=285)

        self.label11 = tk.Label(janela3, width=20, height=1, text='HELP', font='Arial 20 bold', fg='black')
        self.label11.place(x=30, y=5)


jalenaRaiz = tk.Tk()
Tela(jalenaRaiz)
jalenaRaiz.mainloop()