import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the model and data (replace with your actual file paths)
df = pd.read_csv('D:\\datasets\\idataset3.csv')
df.drop(['Model'],axis=1,inplace=True)
df.drop(['Release Date'],axis=1,inplace=True)
df.replace(0, 1, inplace=True)
# ... (rest of your data preprocessing and model training code)
X = df.iloc[:,[0,1,2,4,3,5,6,7]]
y = df.iloc[:,[-1]]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=15)
reg = RandomForestRegressor()
reg.fit(X_train,y_train)

def predict_price():
    try:
        a = int(lowest_storage_entry.get())
        b = int(primary_camera_entry.get())
        c = int(front_camera_entry.get())
        d = processor_entry.get()
        e = int(battery_power_entry.get())
        f = int(core_entry.get())
        g = float(screen_size_entry.get())
        h = color_entry.get()

        ascii_concatenated_d = "".join(str(ord(char)) for char in d)
        ascii_concatenated_h = "".join(str(ord(char)) for char in h)

        prediction = reg.predict([[a, b, c, int(ascii_concatenated_d), e, f, g, int(ascii_concatenated_h)]])
        result_label.config(text=f"Predicted Price: {prediction[0]}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")


# Create the main window
window = tk.Tk()
window.title("iPhone Price Prediction")

# Input fields
lowest_storage_label = ttk.Label(window, text="Lowest Storage (GB):")
lowest_storage_label.grid(row=0, column=0, padx=5, pady=5)
lowest_storage_entry = ttk.Entry(window,width=30)
lowest_storage_entry.grid(row=0, column=1, padx=5, pady=5)

# ... (similarly create labels and entry fields for other features)
# ... (primary_camera, front_camera, processor, battery_power, core, screen_size, color)

primary_camera_label = ttk.Label(window, text="Primary Camera (MP):")
primary_camera_label.grid(row=1, column=0, padx=5, pady=5)
primary_camera_entry = ttk.Entry(window,width=30)
primary_camera_entry.grid(row=1, column=1, padx=5, pady=5)

front_camera_label = ttk.Label(window, text="Front Camera (MP):")
front_camera_label.grid(row=2, column=0, padx=5, pady=5)
front_camera_entry = ttk.Entry(window,width=30)
front_camera_entry.grid(row=2, column=1, padx=5, pady=5)


processor_label = ttk.Label(window, text="Processor:")
processor_label.grid(row=3, column=0, padx=5, pady=5)
processor_entry = ttk.Entry(window,width=30)
processor_entry.grid(row=3, column=1, padx=5, pady=5)

battery_power_label = ttk.Label(window, text="Battery Power (mAh):")
battery_power_label.grid(row=4, column=0, padx=5, pady=5)
battery_power_entry = ttk.Entry(window,width=30)
battery_power_entry.grid(row=4, column=1, padx=5, pady=5)

core_label = ttk.Label(window, text="Core:")
core_label.grid(row=5, column=0, padx=5, pady=5)
core_entry = ttk.Entry(window,width=30)
core_entry.grid(row=5, column=1, padx=5, pady=5)

screen_size_label = ttk.Label(window, text="Screen size(inches):")
screen_size_label.grid(row=6, column=0, padx=5, pady=5)
screen_size_entry = ttk.Entry(window,width=30)
screen_size_entry.grid(row=6, column=1, padx=5, pady=5)


color_label = ttk.Label(window, text="Colour:")
color_label.grid(row=7, column=0, padx=5, pady=5)
color_entry = ttk.Entry(window,width=30)
color_entry.grid(row=7, column=1, padx=5, pady=5)

# Predict button
predict_button = ttk.Button(window, text="Predict Price", command=predict_price)
predict_button.grid(row=8, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(window, text="")
result_label.grid(row=9, column=0, columnspan=2)


window.mainloop()