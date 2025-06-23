import tkinter as tk
from tkinter import messagebox

def sumprimes():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
    except ValueError:
        messagebox.showerror('Invalid Input', 'Please enter valid integers.')
        return

    if b > a:
        primes = []
        total = 0
        for number in range(a, b + 1):
            if number >= 2:
                is_prime = True
                for i in range(2, int(number**0.5) + 1):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(number)
                    total += number

                    result_text.config(state=tk.NORMAL)
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f'Primes: {primes}\n\nSum: {total}')
                    result_text.config(state=tk.DISABLED)
    else:
        messagebox.showwarning('Invalid Range', 'Second number must be greater than first.')

root = tk.Tk()
root.title('Prime Number Sum Calculator')
root.config(bg='black')


tk.Label(root, text='Provide first number:',bg='grey',fg='white').grid(row=1,column=1,padx=10,pady=20)
entry1 = tk.Entry(root)
entry1.grid(row=1,column=2,padx=10,pady=20)

tk.Label(root, text='Provide second number:',bg='grey',fg='white').grid(row=2,column=1,padx=10,pady=20)
entry2 = tk.Entry(root)
entry2.grid(row=2,column=2,padx=10,pady=20)

tk.Button(root, text='add', command=sumprimes,bg='grey',fg='white').grid(row=3,column=2,padx=10,pady=20)

result_text = tk.Text(root,height=10,width=30, bg='grey',fg='white',wrap=tk.WORD)
result_text.grid(row=4,column=1,padx=10,pady=20)

root.mainloop()
