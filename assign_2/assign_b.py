import tkinter as tk
from tkinter import messagebox

def third():
    
    user_input = entry1.get()
    arry = list(map(int,user_input.split(',')))
    arry.sort()
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f'the third number is: {arry[2]}')
    result_text.config(state=tk.DISABLED)
root = tk.Tk()
root.title('Third number')
root.config(bg='black')


tk.Label(root, text='provide number e.g 1,2,3,4,5,6,7,8:',bg='grey',fg='white').grid(row=1,column=1,padx=10,pady=20)
entry1 = tk.Entry(root)
entry1.grid(row=1,column=2,padx=10,pady=20)

tk.Button(root, text='add', command=third,bg='grey',fg='white').grid(row=3,column=2,padx=10,pady=20)

result_text = tk.Text(root,height=10,width=30, bg='grey',fg='white',wrap=tk.WORD)
result_text.grid(row=4,column=1,padx=10,pady=20)

root.mainloop()