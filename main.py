import tkinter as tk
from tkinter import ttk
import os
from models import Vehicle

inventory = [
    # A
    Vehicle("Audi", "A4", 2010, "2.0 TDI", 185000, "Quattro", 6100),
    Vehicle("Audi", "A3", 2015, "1.6 TDI", 120000, "Предно", 9500),
    Vehicle("Audi", "A6", 2012, "3.0 TDI", 230000, "Quattro", 11500),
    Vehicle("Audi", "Q7", 2017, "3.0 TFSI", 95000, "Quattro", 28000),
    # B
    Vehicle("BMW", "M5", 2018, "4.4 V8", 75000, "xDrive", 55000),
    Vehicle("BMW", "320i", 2013, "2.0i", 145000, "Задно", 10500),
    Vehicle("BMW", "X5", 2015, "3.0d", 180000, "xDrive", 21000),
    Vehicle("BMW", "530d", 2011, "3.0d", 240000, "Задно", 9800),
    # C
    Vehicle("Chevrolet", "Corvette", 2021, "6.2 V8", 15000, "Задно", 75000),
    Vehicle("Chevrolet", "Camaro", 2017, "2.0 Turbo", 65000, "Задно", 22000),
    Vehicle("Chevrolet", "Cruze", 2014, "1.6i", 115000, "Предно", 5500),
    Vehicle("Chevrolet", "Spark", 2012, "1.0i", 90000, "Предно", 3200),
    # D
    Vehicle("Dacia", "Duster", 2019, "1.5 dCi", 90000, "4x4", 12000),
    Vehicle("Dacia", "Logan", 2015, "1.2 16V", 140000, "Предно", 4500),
    Vehicle("Dacia", "Sandero", 2018, "0.9 TCe", 75000, "Предно", 7200),
    Vehicle("Dacia", "Jogger", 2022, "1.0 TCe", 35000, "Предно", 16500),
    # E
    Vehicle("Eagle", "Talon", 1998, "2.0 Turbo", 210000, "AWD", 4500),
    Vehicle("Eagle", "Vision", 1995, "3.5 V6", 180000, "Предно", 2500),
    Vehicle("Eagle", "Summit", 1994, "1.5i", 160000, "Предно", 1200),
    Vehicle("Eagle", "Premier", 1992, "3.0 V6", 220000, "Предно", 1000),
    # F
    Vehicle("Ford", "Mustang", 2016, "5.0 V8", 85000, "Задно", 30000),
    Vehicle("Ford", "Focus", 2012, "1.6 TDCi", 165000, "Предно", 4800),
    Vehicle("Ford", "Fiesta", 2015, "1.0 EcoBoost", 95000, "Предно", 5900),
    Vehicle("Ford", "Kuga", 2018, "2.0 TDCi", 110000, "AWD", 14500),
    # G
    Vehicle("Genesis", "G70", 2020, "3.3T", 40000, "AWD", 38000),
    Vehicle("Genesis", "G80", 2019, "3.8 V6", 60000, "AWD", 29000),
    Vehicle("Genesis", "GV80", 2021, "3.0D", 45000, "AWD", 52000),
    Vehicle("Genesis", "G90", 2022, "3.5T V6", 20000, "AWD", 78000),
    # H
    Vehicle("Honda", "Civic", 2017, "1.5 Turbo", 110000, "Предно", 15000),
    Vehicle("Honda", "Accord", 2014, "2.2 i-DTEC", 175000, "Предно", 11200),
    Vehicle("Honda", "CR-V", 2016, "2.0 i-VTEC", 130000, "AWD", 16800),
    Vehicle("Honda", "Jazz", 2013, "1.3 i-VTEC", 98000, "Предно", 5400),
    # I
    Vehicle("Infiniti", "Q50", 2015, "3.7 V6", 145000, "Задно", 16500),
    Vehicle("Infiniti", "FX35", 2008, "3.5 V6", 210000, "AWD", 7500),
    Vehicle("Infiniti", "QX70", 2016, "3.0d V6", 125000, "AWD", 22500),
    Vehicle("Infiniti", "G35", 2006, "3.5 V6", 195000, "Задно", 5800),
    # J
    Vehicle("Jaguar", "XF", 2014, "3.0 V6", 160000, "AWD", 18000),
    Vehicle("Jaguar", "XJ", 2012, "3.0 D", 190000, "Задно", 14500),
    Vehicle("Jaguar", "F-Type", 2016, "3.0 V6", 55000, "Задно", 39000),
    Vehicle("Jaguar", "F-Pace", 2018, "2.0 D", 105000, "AWD", 27500),
    # K
    Vehicle("Kia", "Stinger", 2019, "3.3T V6", 55000, "AWD", 32000),
    Vehicle("Kia", "Ceed", 2015, "1.6 CRDi", 140000, "Предно", 6800),
    Vehicle("Kia", "Sportage", 2017, "1.7 CRDi", 115000, "Предно", 13400),
    Vehicle("Kia", "Rio", 2014, "1.2 CVVT", 95000, "Предно", 5100),
    # L
    Vehicle("Lexus", "IS 300h", 2016, "2.5 Hybrid", 120000, "Задно", 22000),
    Vehicle("Lexus", "RX 450h", 2015, "3.5 V6 Hyb", 150000, "AWD", 24500),
    Vehicle("Lexus", "GS 300", 2008, "3.0 V6", 210000, "Задно", 6900),
    Vehicle("Lexus", "LS 460", 2012, "4.6 V8", 165000, "Задно", 18500),
    # M
    Vehicle("Mercedes", "W211 E500", 2004, "5.0 V8", 280000, "Задно", 8500),
    Vehicle("Mercedes", "W204 C220", 2009, "2.2 CDI", 195000, "Задно", 6400),
    Vehicle("Mercedes", "W221 S350", 2011, "3.0 CDI", 220000, "Задно", 12500),
    Vehicle("Mercedes", "W164 ML320", 2007, "3.0 CDI", 250000, "4MATIC", 5900),
    # N
    Vehicle("Nissan", "GT-R", 2012, "3.8 V6", 65000, "AWD", 60000),
    Vehicle("Nissan", "Qashqai", 2015, "1.5 dCi", 135000, "Предно", 10500),
    Vehicle("Nissan", "Juke", 2014, "1.6 DIG-T", 110000, "Предно", 7800),
    Vehicle("Nissan", "Almera", 2006, "1.5i", 180000, "Предно", 1800),
    # O
    Vehicle("Opel", "Insignia", 2018, "2.0 CDTI", 130000, "Предно", 14000),
    Vehicle("Opel", "Astra H", 2007, "1.7 CDTI", 210000, "Предно", 2400),
    Vehicle("Opel", "Corsa D", 2010, "1.2i", 145000, "Предно", 3300),
    Vehicle("Opel", "Zafira B", 2009, "1.9 CDTI", 190000, "Предно", 2900),
    # P
    Vehicle("Porsche", "911 Carrera", 2020, "3.0T", 25000, "Задно", 110000),
    Vehicle("Porsche", "Cayenne", 2013, "3.0 TDI", 175000, "AWD", 21500),
    Vehicle("Porsche", "Panamera", 2014, "3.0 D", 160000, "Задно", 24000),
    Vehicle("Porsche", "Macan", 2016, "2.0T", 110000, "AWD", 31000),
    # Q
    Vehicle("Qoros", "3 Sedan", 2015, "1.6 Turbo", 95000, "Предно", 7000),
    Vehicle("Qoros", "3 Hatch", 2014, "1.6i", 110000, "Предно", 5800),
    Vehicle("Qoros", "5 SUV", 2016, "1.6 Turbo", 85000, "Предно", 9500),
    Vehicle("Qoros", "7 SUV", 2020, "1.6T", 45000, "Предно", 15500),
    # R
    Vehicle("Renault", "Kadjar", 2018, "1.5 dCi K9K", 65000, "Предно", 16000),
    Vehicle("Renault", "Clio", 2015, "1.2 16V", 125000, "Предно", 5200),
    Vehicle("Renault", "Megane", 2012, "1.5 dCi", 185000, "Предно", 4600),
    Vehicle("Renault", "Captur", 2017, "0.9 TCe", 85000, "Предно", 9800),
    # S
    Vehicle("Subaru", "Impreza WRX", 2011, "2.5 Turbo", 155000, "AWD", 19000),
    Vehicle("Subaru", "Forester", 2014, "2.0D", 165000, "AWD", 11200),
    Vehicle("Subaru", "Outback", 2013, "2.5i", 180000, "AWD", 9500),
    Vehicle("Subaru", "Legacy", 2010, "2.0i", 200000, "AWD", 5400),
    # T
    Vehicle("Toyota", "RAV4", 2022, "2.5 Hybrid", 45000, "AWD", 33000),
    Vehicle("Toyota", "Corolla", 2015, "1.4 D-4D", 130000, "Предно", 9200),
    Vehicle("Toyota", "Avensis", 2011, "2.0 D-4D", 195000, "Предно", 5800),
    Vehicle("Toyota", "Yaris", 2014, "1.33 Dual-VVT", 105000, "Предно", 6400),
    # U
    Vehicle("UAZ", "Patriot", 2017, "2.7i", 80000, "4x4", 9000),
    Vehicle("UAZ", "Hunter", 2015, "2.7i", 60000, "4x4", 6500),
    Vehicle("UAZ", "Bukhanka", 2010, "2.7i", 110000, "4x4", 4800),
    Vehicle("UAZ", "452", 1995, "2.4i", 150000, "4x4", 2000),
    # V
    Vehicle("Volkswagen", "Passat B6", 2007, "2.0 FSI", 134054, "4Motion", 4300),
    Vehicle("Volkswagen", "Golf 5", 2005, "1.9 TDI", 210000, "Предно", 3200),
    Vehicle("Volkswagen", "Polo", 2010, "1.2 TSI", 145000, "Предно", 4500),
    Vehicle("Volkswagen", "Tiguan", 2012, "2.0 TDI", 165000, "4Motion", 9800),
    # W
    Vehicle("Wiesmann", "MF5", 2010, "4.4 V8", 30000, "Задно", 150000),
    Vehicle("Wiesmann", "MF3", 2005, "3.2i", 45000, "Задно", 95000),
    Vehicle("Wiesmann", "MF4", 2008, "4.8 V8", 35000, "Задно", 120000),
    Vehicle("Wiesmann", "GT MF4", 2012, "4.4 V8", 20000, "Задно", 165000),
    # X
    Vehicle("Xpeng", "P7", 2023, "Електрически", 12000, "AWD", 45000),
    Vehicle("Xpeng", "G3", 2021, "Електрически", 35000, "Предно", 24000),
    Vehicle("Xpeng", "P5", 2022, "Електрически", 25000, "Предно", 29000),
    Vehicle("Xpeng", "G9", 2023, "Електрически", 15000, "AWD", 58000),
    # Y
    Vehicle("Yugo", "Florida", 1999, "1.3", 95000, "Предно", 1500),
    Vehicle("Yugo", "Koral", 1990, "1.1", 110000, "Предно", 800),
    Vehicle("Yugo", "Tempo", 1995, "1.1", 85000, "Предно", 950),
    Vehicle("Yugo", "Skala", 1988, "1.3", 130000, "Предно", 700),
    # Z
    Vehicle("Zastava", "101", 1985, "1.1", 120000, "Предно", 2500),
    Vehicle("Zastava", "750", 1978, "0.8", 90000, "Задно", 3500),
    Vehicle("Zastava", "Skala 55", 1992, "1.1", 140000, "Предно", 1100),
    Vehicle("Zastava", "10", 2006, "1.2i", 160000, "Предно", 1800)
]

current_displayed_data = inventory.copy()


def get_header():
    header = "{:<14} | {:<14} | {:<6} | {:<14} | {:>9} | {:<10} | {:>9} EUR"
    return header.format("Марка", "Модел", "Година", "Двигател", "Пробег", "Задвижване", "Цена")


def display_data(data):
    global current_displayed_data
    current_displayed_data = data

    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)

    total_val = sum(c.price for c in data)
    text_area.insert(tk.END,
                     f"--- ОБЩА ПАЗАРНА СТОЙНОСТ: {total_val:,} EUR (Двойно кликване върху кола за снимка) ---\n\n".replace(
                         ',', ' '))

    text_area.insert(tk.END, get_header() + "\n")
    text_area.insert(tk.END, "-" * 98 + "\n")

    if not data:
        text_area.insert(tk.END, "\n(Няма намерени автомобили по тези критерии)")
    else:
        for car in data:
            row_fmt = "{:<14} | {:<14} | {:<6} | {:<14} | {:>9} | {:<10} | {:>9} EUR"
            text_area.insert(tk.END,
                             row_fmt.format(car.brand, car.model, car.year, car.engine, car.mileage, car.drivetrain,
                                            car.price) + "\n")

    text_area.config(state=tk.DISABLED)


def open_car_details(event):
    click_pos = text_area.index(f"@{event.x},{event.y}")
    line_num = int(click_pos.split('.')[0])
    data_index = line_num - 5

    if 0 <= data_index < len(current_displayed_data):
        car = current_displayed_data[data_index]

        detail_window = tk.Toplevel(root)
        detail_window.title(f"Детайли за {car.brand} {car.model}")
        detail_window.geometry("450x450")
        detail_window.resizable(False, False)

        info_text = f"Марка: {car.brand}\nМодел: {car.model}\nГодина: {car.year} г.\nДвигател: {car.engine}\nПробег: {car.mileage} км\nЗадвижване: {car.drivetrain}\nЦена: {car.price} EUR"
        lbl_info = tk.Label(detail_window, text=info_text, font=("Arial", 11, "bold"), justify=tk.LEFT)
        lbl_info.pack(pady=15, padx=20, anchor="w")

        image_filename = f"{car.brand.lower()}.png"
        img_frame = tk.Frame(detail_window, width=400, height=220, bg="#dcdcdc", relief=tk.SUNKEN, bd=2)
        img_frame.pack(pady=10)
        img_frame.pack_propagate(False)

        if os.path.exists(image_filename):
            try:
                car_img = tk.PhotoImage(file=image_filename)
                lbl_img = tk.Label(img_frame, image=car_img, bg="#dcdcdc")
                lbl_img.image = car_img
                lbl_img.pack(fill=tk.BOTH, expand=True)
            except Exception:
                lbl_error = tk.Label(img_frame, text="Грешка при зареждане на изображението", fg="red", bg="#dcdcdc")
                lbl_error.pack(expand=True)
        else:
            lbl_placeholder = tk.Label(img_frame,
                                       text=f"[ Снимка на {car.brand} ]\n(Поставете файл '{image_filename}' в папката)",
                                       font=("Arial", 10, "italic"), fg="#666666", bg="#dcdcdc")
            lbl_placeholder.pack(expand=True)


def apply_sort(event=None):
    sort_option = sort_combobox.get()
    if sort_option == "Марка (A-Z)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.brand)
    elif sort_option == "Марка (Z-A)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.brand, reverse=True)
    elif sort_option == "Цена (най-ниска първо)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.price)
    elif sort_option == "Цена (най-висока първо)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.price, reverse=True)
    elif sort_option == "Пробег (най-малък първо)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.mileage)
    elif sort_option == "Пробег (най-голям първо)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.mileage, reverse=True)
    elif sort_option == "Година (най-стара първо)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.year)
    elif sort_option == "Година (най-нова първо)":
        sorted_data = sorted(current_displayed_data, key=lambda x: x.year, reverse=True)
    else:
        sorted_data = current_displayed_data
    display_data(sorted_data)


def search_all_fields(event=None):
    search_query = search_entry.get().strip().lower()
    if not search_query:
        display_data(inventory)
        apply_sort()
        return
    filtered_cars = []
    for car in inventory:
        car_info = f"{car.brand} {car.model} {car.year} {car.engine} {car.mileage} {car.drivetrain} {car.price}".lower()
        if search_query in car_info:
            filtered_cars.append(car)
    display_data(filtered_cars)
    apply_sort()


def on_hover(event):

    text_area.tag_remove("hover_row", "1.0", tk.END)

    click_pos = text_area.index(f"@{event.x},{event.y}")
    line_num = int(click_pos.split('.')[0])
    data_index = line_num - 5

    if 0 <= data_index < len(current_displayed_data):
        start_index = f"{line_num}.0"
        end_index = f"{line_num}.end"
        text_area.tag_add("hover_row", start_index, end_index)

def on_leave(event):
    text_area.tag_remove("hover_row", "1.0", tk.END)

root = tk.Tk()
root.title("Складова наличност на автокъща HundredCars")
root.geometry("980x650")

try:
    app_icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(False, app_icon)
except Exception:
    pass

top_frame = tk.Frame(root)
top_frame.pack(pady=20)

tk.Label(top_frame, text="Супер търсачка:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
search_entry = tk.Entry(top_frame, width=35)
search_entry.grid(row=0, column=1, padx=5)
search_entry.bind('<KeyRelease>', search_all_fields)

tk.Label(top_frame, text="Сортирай по:", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=(30, 5))

sort_options = ["Марка (A-Z)", "Марка (Z-A)", "Цена (най-ниска първо)", "Цена (най-висока първо)",
                "Пробег (най-малък първо)", "Пробег (най-голям първо)", "Година (най-стара първо)",
                "Година (най-нова първо)"]

sort_combobox = ttk.Combobox(top_frame, values=sort_options, state="readonly", width=25)
sort_combobox.grid(row=0, column=3, padx=5)
sort_combobox.current(0)
sort_combobox.bind("<<ComboboxSelected>>", apply_sort)

text_area = tk.Text(root, width=110, height=32, font=("Consolas", 10), state=tk.DISABLED, bg="#f4f4f4", cursor="hand2")
text_area.pack(padx=10, pady=10)

text_area.tag_config("hover_row", background="#e0f7fa")

text_area.bind("<Double-Button-1>", open_car_details)
text_area.bind("<Motion>", on_hover)
text_area.bind("<Leave>", on_leave)

display_data(inventory)
apply_sort()
root.mainloop()