import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CarSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Search App")

        self.cars = [

             {"brand": "Toyota", "model": "Camry", "year": 2022, "price": 25000, "image_path": "toyota_camry.jpg"},
            {"brand": "Toyota", "model": "Corolla", "year": 2023, "price": 20000, "image_path": "toyota_corolla.jpg"},
            {"brand": "Toyota", "model": "RAV4", "year": 2021, "price": 28000, "image_path": "toyota_rav4.jpg"},
            {"brand": "Toyota", "model": "Highlander", "year": 2022, "price": 35000, "image_path": "toyota_highlander.jpg"},
            {"brand": "Toyota", "model": "Prius", "year": 2023, "price": 30000, "image_path": "toyota_prius.jpg"},
            
            {"brand": "Honda", "model": "Accord", "year": 2023, "price": 28000, "image_path": "honda_accord.jpg"},
            {"brand": "Honda", "model": "Civic", "year": 2022, "price": 22000, "image_path": "honda_civic.jpg"},
            {"brand": "Honda", "model": "CR-V", "year": 2021, "price": 30000, "image_path": "honda_cr-v.jpg"},
            {"brand": "Honda", "model": "Pilot", "year": 2023, "price": 35000, "image_path": "honda_pilot.jpg"},
            {"brand": "Honda", "model": "Odyssey", "year": 2022, "price": 40000, "image_path": "honda_odyssey.jpg"},
            
            {"brand": "Ford", "model": "Mustang", "year": 2021, "price": 35000, "image_path": "ford_mustang.jpg"},
            {"brand": "Ford", "model": "Explorer", "year": 2022, "price": 30000, "image_path": "ford_explorer.jpg"},
            {"brand": "Ford", "model": "Fusion", "year": 2023, "price": 25000, "image_path": "ford_fusion.jpg"},
            {"brand": "Ford", "model": "Escape", "year": 2022, "price": 28000, "image_path": "ford_escape.jpg"},
            {"brand": "Ford", "model": "F-150", "year": 2021, "price": 40000, "image_path": "ford_f150.jpg"},
            
            {"brand": "Mercedes", "model": "C-Class", "year": 2022, "price": 45000, "image_path": "mercedes_c-class.jpg"},
            {"brand": "Mercedes", "model": "E-Class", "year": 2023, "price": 55000, "image_path": "mercedes_e-class.jpg"},
            {"brand": "Mercedes", "model": "S-Class", "year": 2021, "price": 70000, "image_path": "mercedes_s-class.jpg"},
            {"brand": "Mercedes", "model": "GLC", "year": 2022, "price": 50000, "image_path": "mercedes_glc.jpg"},
            {"brand": "Mercedes", "model": "GLE", "year": 2023, "price": 65000, "image_path": "mercedes_gle.jpg"},
            {"brand": "Mercedes", "model": "E350", "year": 2023, "price": 60000, "image_path": "mercedes_e350.jpg"},

            {"brand": "BMW", "model": "530i Sedan", "year": 2024, "price": 57900, "image_path": "Bmw_Sedan.jpg"},
            # ... (your car details)
        ]

        self.create_widgets()

    def create_widgets(self):
        self.selected_car = tk.StringVar()

        self.search_entry = ttk.Combobox(self.root, textvariable=self.selected_car, font=('Helvetica', 24), justify='center')
        self.search_entry['values'] = [car['brand'] + ' ' + car['model'] + ' (' + str(car['year']) + ')' for car in self.cars]
        self.search_entry.pack(pady=(200, 10))

        self.search_button = ttk.Button(self.root, text="Search", command=self.display_selected_car)
        self.search_button.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.car_image_label = ttk.Label(self.root)
        self.car_image_label.pack(pady=10)

    def display_selected_car(self):
        selected_car_text = self.selected_car.get().strip()

        if not selected_car_text:
            self.result_label.config(text="Please select a car from the dropdown.")
            return

        selected_car = None

        for car in self.cars:
            car_info = f"{car['brand']} {car['model']} ({car['year']})"
            if selected_car_text == car_info:
                selected_car = car
                break

        if selected_car:
            image_path = selected_car.get("image_path", "default_image.jpg")  # Use a default image if not specified
            details = f"{selected_car['brand']} {selected_car['model']} ({selected_car['year']}, ${selected_car['price']})"
            
            self.result_label.config(text=details)
            self.display_image(image_path)
        else:
            self.result_label.config(text="Selected car not found.")

    def display_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((300, 200))
        photo = ImageTk.PhotoImage(image)

        # Keep a reference to avoid garbage collection
        self.car_image_label.image = photo
        self.car_image_label.config(image=photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = CarSearchApp(root)
    
    # Center the window on the screen
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry("+{}+{}".format(position_right, position_down))
    
    root.mainloop()
