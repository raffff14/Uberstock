import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SideMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Uber Stocks")
        self.root.geometry("800x600")
        self.root.configure(bg="black")  

        try:
            self.background_image = Image.open("background.jpg")
            self.background_image = self.background_image.resize((800, 600))
            self.background_image = ImageTk.PhotoImage(self.background_image)
            self.background_label = tk.Label(root, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Error loading background image:", e)
        
        self.side_menu = tk.Frame(self.root, bg="black")
        self.side_menu.pack(side=tk.TOP, fill=tk.X)

        title_label = tk.Label(self.side_menu, text="6NUMERICAL", font=("Courier New", 16, "bold"), bg="black", fg="white")
        title_label.pack(side=tk.LEFT, padx=10, pady=10)

        button_frame = tk.Frame(self.side_menu, bg="black")
        button_frame.pack(side=tk.RIGHT, fill=tk.Y)

        custom_style = ttk.Style()
        custom_style.configure('Custom.TButton', foreground='black', font=('Courier New', 12, "bold"))

        options = ["Home", "Forecast", "About"]

        for option in options:
            btn = ttk.Button(button_frame, text=option, command=lambda opt=option: self.handle_option(opt), style='Custom.TButton')
            btn.pack(side=tk.LEFT, padx=10, pady=10)
            if option == "About":
                logo_image = Image.open("uberpic.png")

        self.content_frame = tk.Frame(self.root, bg="white", width=400, height=600,highlightthickness=1,highlightbackground="black")
        self.content_frame.pack_propagate(False)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(self.content_frame, bg="black", height=2, highlightthickness=1)
        canvas.create_line(0, 1, 400, 1, fill="black", width=2)  # Assuming width of 400 for the content frame
        canvas.place(x=0, y=10)
        
        self.display_content("Home")
        
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x_offset = (self.root.winfo_screenwidth() - width) // 2
        y_offset = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry("+{}+{}".format(x_offset, y_offset))

    def handle_option(self, option):
        if option == "Calculate":
            self.add_calculator_section()
        else:
            self.display_content(option)

    def display_content(self, option):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if option == "Home":
            label = tk.Label(self.content_frame, text="UBER Stocks:Closing Price Prediction \n using Multiple Linear Regression", font=("Courier New", 15, "bold"), fg="white", bg="gray")
            label.pack(side=tk.TOP,fill=tk.X, pady=(20,0))
            label = tk.Label(self.content_frame, text="Numerical Methods CS-301", font=("Courier New", 10, "bold"), fg="Black", bg="gray70")
            label.pack(side=tk.TOP,fill=tk.X)

            image = Image.open("uberpic.png")
            image = image.resize((750, 395))
            image_tk = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.content_frame, image=image_tk, bg="black")
            image_label.image = image_tk
            image_label.pack(expand=True, side=tk.TOP, pady=20)

    
            credits_frame = tk.Frame(self.content_frame, bg="black")
            credits_frame.pack(side=tk.BOTTOM, fill=tk.X)

            label = tk.Label(credits_frame, text="Copyright © 2024 Holy Angel University • All Rights Reserved", font=("Courier New", 10), fg="white", bg="black")
            label.pack(expand=True)

        elif option == "Forecast":
            
            self.add_calculator_section()

        elif option == "About":
            aboutfull_frame = tk.Frame(self.content_frame, bg="black")
            aboutfull_frame.pack(expand=True,side=tk.TOP, fill=tk.X)

            about_frame = tk.Frame(self.content_frame, bg="black")
            about_frame.pack(expand=True, fill=tk.BOTH)

            header_label = tk.Label(aboutfull_frame, text="UBER Stocks: Closing-Price Prediction", font=("Courier New", 16, "bold"), bg="black", fg="white", pady=20)
            header_label.pack(expand=True, side=tk.TOP, fill=tk.X)
        

            description = tk.Text(about_frame, wrap="word", font=("Courier New", 12), bg="gray70", fg="black", height=6, bd=1, padx=20, pady=10)
            description.pack(expand=True, side=tk.TOP, padx=20, pady=(20, 10))
            description.insert(tk.END, """\tUBER, a global icon in ride-sharing and food delivery, represents innovation in the transportation industry.
 This project harnesses the power of data science to forecast UBER's status within the stock market, a dynamic arena where investors trade ownership in companies and a vital engine of the global economy. Providing invaluable insights for investors about UBER’s Closing Price, which reflects the consensus of the market’s valuation and influences future investment decisions, navigating the complexities of the stock market.
 Join us in unlocking the future of investment with precision and confidence.
            """)
            description.config(state="disabled")


            independent = tk.Text(about_frame, wrap="word", font=("Courier New", 11), bg="gray10", fg="white", height=1, bd=0,padx=10)
            independent.pack(side=tk.TOP, padx=20, pady=(40,10))
            independent.insert(tk.END, "Members:")
            independent.config(state="disabled")

            independent_variables = tk.Text(about_frame, wrap="word", font=("Courier New", 11), fg="black", bg="gray70", height=3, bd=0)
            independent_variables.pack(side=tk.TOP, padx=20)
            independent_variables.insert(tk.END, """\t- Fred jaafary
    \t- Rafhael Malabanan
    \t- Lindley Quiambao
    \t- CS-301""")
            independent_variables.config(state="disabled")

    def add_calculator_section(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        calculator_frame = tk.Frame(self.content_frame, bg="black")
        calculator_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(calculator_frame, text="Multiple Linear Regression Calculator", font=("Courier New", 16, "bold"), bg="black", fg="white")
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        file_path_label = tk.Label(calculator_frame, text="CSV File:", bg="black", fg="white")
        file_path_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.file_path_entry = tk.Entry(calculator_frame, bg="white", fg="black")
        self.file_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        file_path_button = tk.Button(calculator_frame, text="Browse", command=self.open_file_dialog, bg="gray70", fg="black", font=("Courier New", 12, "bold"))
        file_path_button.grid(row=1, column=2, padx=5, pady=5)

        dependent_var_label = tk.Label(calculator_frame, text="Dependent Variable:", bg="black", fg="white")
        dependent_var_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.dependent_var_entry = tk.Entry(calculator_frame, bg="white", fg="black")
        self.dependent_var_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        confirm_button = tk.Button(calculator_frame, text="Predict", command=self.perform_regression, bg="gray70", fg="black", font=("Courier New", 12, "bold"))
        confirm_button.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.result_label = tk.Label(calculator_frame, font=("Courier New", 12), bg="black", fg="white")
        self.result_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

        calculator_frame.grid_columnconfigure(0, weight=1)
        calculator_frame.grid_columnconfigure(1, weight=1)
        calculator_frame.grid_columnconfigure(2, weight=1)

        credits_frame = tk.Frame(self.content_frame, bg="white")
        credits_frame.pack(side=tk.BOTTOM, fill=tk.X)

        label = tk.Label(credits_frame, text="Copyright © 2024 Holy Angel University • All Rights Reserved", font=("Courier New", 10), fg="black", bg="white")
        label.pack(expand=True)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)
        
        if file_path:
            data = pd.read_csv(file_path)
            columns = data.columns.tolist()
            self.dependent_var_entry.delete(0, tk.END)
            self.dependent_var_entry.insert(0, columns[-3])

    def perform_regression(self):
        file_path = self.file_path_entry.get()
        data = pd.read_csv(file_path)

        # Drop NaN values
        data = data.dropna()

        # Define dependent and independent variables
        dependent_var = 'Close'
        independent_vars = ['High', 'Low', 'Volume', 'Open']

        X = data[independent_vars]
        y = data[dependent_var]

        # Add intercept term to X
        X = np.column_stack((np.ones(len(X)), X))

        # Calculate coefficients using matrix operations
        beta = np.linalg.inv(X.T @ X) @ X.T @ y

        # Predicted values
        y_pred = X @ beta

        # Calculate statistics
        St = sum((y - np.mean(y))**2)
        residuals = y - y_pred
        sse = sum(residuals**2)
        ssr = sse / (len(y) - X.shape[1])
        r_squared = 1 - sse / St
        r = np.corrcoef(y, y_pred)[0, 1]

        # Format the result
        equation = "Y = {:.2f} + ".format(beta[0]) + " + ".join(["{:.2f} * {}".format(b, var) for b, var in zip(beta[1:], independent_vars)])
        total_sq = "Total sum of Squares: {:.2f}".format(St)
        res_std_err = "Residual Standard Error: {:.2f}".format(np.sqrt(ssr))
        coeff_det = "Coefficient of Determination: {:.2f}".format(r_squared)
        corr_coef = "Correlation Coefficient: {:.2f}".format(r)
        predicted_values = "Predicted Values: \n" + "\n".join(["{:.2f}".format(val) for val in y_pred])

        result_text = "\n".join([equation, total_sq, res_std_err,coeff_det, corr_coef])

        result_frame = tk.Frame(self.content_frame, bg="black")
        result_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.result_label = tk.Label(result_frame, text=result_text, wraplength=600, fg="white", bg="black")
        self.result_label.grid(row=0, column=0, padx=10, pady=(0, 10))

        predicted = tk.Text(result_frame, wrap="word", font=("Courier New", 12), bg="black", fg="white", height=6, bd=1, padx=1, pady=10)
        predicted.insert(tk.END, predicted_values)
        predicted.config(state="disabled")
        predicted.grid(row=1, column=0, padx=10, pady=(0, 10))

        plt.figure(figsize=(6, 6))
        plt.scatter(y, y_pred, color='blue')
        plt.plot([min(y), max(y)], [min(y), max(y)], color='red')  # Diagonal line
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.title('Actual vs Predicted')
        plt.grid(True)
        plt.show()

# Initialize root window
root = tk.Tk()
root.config(bg="black")
style = ttk.Style()
style.configure('SideMenu.TButton', foreground='black', background='white')

# Initialize the application
app = SideMenu(root)

# Run the main event loop
root.mainloop()