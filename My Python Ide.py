from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
root =Tk()

root.title("Kunals Python IDE")
editor= Text(bg='#778899',fg='white',height=25,insertbackground="white")
editor.pack(fill= BOTH ,expand=1,ipady=40)
code_output = Text(bg='#18191A',fg='white',height=10,width=500)
code_output.pack(expand=1)
root.geometry('700x600')


#defining the file path for saving
file_path=''
def set_file_path(path):
    global file_path
    file_path = path

#Save function 
def save_as():
    if file_path == '':

     path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
         path=file_path
    with open(path, 'w') as file:
         code = editor.get('1.0',END)
         file.write(code)
         set_file_path(path)
#run function defination 
def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)



#Open function 
def open_file():
     path = askopenfilename(filetypes=[('Python Files', '*py')])
     with open(path, 'r') as file:
         code = file.read()
         editor.delete('1.0', END)
         editor.insert('1.0', code)
         set_file_path(path)

def Clear_Terminal():
    code_output.delete('1.0',END)
    


menu_bar= Menu(root)
file_bar= Menu(menu_bar , tearoff=0)
file_bar.add_command(label='Open', command=open_file)
file_bar.add_command(label='Save', command=save_as)
file_bar.add_command(label='Save AS', command=save_as)
#file_bar.add_command(label='Exit', command=Exit)
menu_bar.add_cascade(label='File', menu=file_bar)
#---------------------------------------------------------
run_bar= Menu(menu_bar , tearoff=0)
run_bar.add_command(label='Run', command=run)
run_bar.add_command(label='Clear_Terminal', command=Clear_Terminal)
menu_bar.add_cascade(label='Run', menu=run_bar)
root.config(menu=menu_bar)


root.mainloop()