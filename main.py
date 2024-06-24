import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Stock App")

    # Set the window size
    root.geometry("1920x1080")
    root.configure(background='black')

    # Create a label
    label = tk.Label(root, text="Stock Predection")
    label.pack(pady=20)

    # Create a button
    button = tk.Button(root, text="Get Stock Data")
    button.pack()

    button2 = tk.Button(root, text="Get News Data")
    button2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
