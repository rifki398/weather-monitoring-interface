import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  
from var.data import my_var

def launch(weather,my_map):
    # ROOT
    root = tk.Tk()
    root.title("Weather Monitoring")
    root.geometry("860x580")

    # Variable
    temp = "-"
    city_name = "-"
    humidity = "-"
    pressure = "-"
    feels_temp = "-"
    sea_level = "-"
    ground_level = "-"

    # Frame untuk header
    header = Frame(root)
    header.pack(pady=(5, 2))

    label_red = Label(header, text="Weather ", font=("Arial", 24, "bold"), fg="red")
    label_red.pack(side="left")

    label_black1 = Label(header, text="Monitoring ", font=("Arial", 24, "bold"), fg="black")
    label_black1.pack(side="left")

    label_black2 = Label(header, text="Interface", font=("Arial", 24, "bold"), fg="black")
    label_black2.pack(side="left")

    separator = Frame(root, bg="black", height=2)
    separator.pack(fill="x", pady=(0,5), padx=14)

    author = Label(root, text="By: Moh Rifqy Risqullah", font=("Arial", 8))
    author.pack(anchor="e", padx=14, pady=(0,8))

    fill_area = Frame(root)
    fill_area.pack(pady=(5,2),fill="x",padx=14)

    city_name = StringVar()

    city_label = Label(fill_area, text="City name:", font=("Arial", 11), fg="black")
    city_label.pack(side="left")

    entry = Entry(fill_area, textvariable=city_name, font=("Arial", 10))
    entry.pack(side="left")

    def submit():
        weather.run(city_name.get())
        my_map.run(my_var.lon, my_var.lat)

        weather_label.config(text=f"Weather: {my_var.weather} ({my_var.weather_description})")
        city_label.config(text=f"Location: {my_var.city} ({my_var.lat},{my_var.lon})")
        temp_label.config(text=f"Temperature: {my_var.temp}\u00b0C")
        feels_temp_label.config(text=f"Feels like temp. : {my_var.feels_like}\u00b0C")
        pressure_label.config(text=f"Avg. Pressure: {my_var.pressure} hPa")
        humidity_label.config(text=f"Humidity: {my_var.humidity} %")
        sea_label.config(text=f"Sea Lvl. Pressure: {my_var.sea_level} hPa")
        ground_label.config(text=f"Ground Lvl. Pressure: {my_var.ground_level} hPa")

        try:
            for widget in container_right.winfo_children():
                widget.destroy()

            # Ganti path ini dengan lokasi file map kamu
            map_img = Image.open("picture/map_osm.png")
            map_img = map_img.resize((340, 340))
            map_photo = ImageTk.PhotoImage(map_img)

            Label(container_right, text="Map View", font=("Arial", 13, "bold")).pack()
            map_label = Label(container_right, image=map_photo)
            map_label.image = map_photo  # penting agar tidak hilang
            map_label.pack(pady=10)
        except Exception as e:
            Label(container_right, text=f"[Error load map]\n{e}", fg="red").pack(pady=10)

    btn = Button(fill_area, text="Search", command=submit)
    btn.pack(side="left",padx=4)

    # Information body
    container = Frame(root)
    container.pack(fill="both", expand=True, padx=14, pady=(18,0))
    container.columnconfigure(0, weight=1, uniform="group1")
    container.columnconfigure(1, weight=1, uniform="group1")

    container_left = Frame(container, width=400, height=400)
    container_left.grid(row=0, column=0, sticky="nsew", padx=(0,10))

    container_right = Frame(container, width=400, height=400)
    container_right.grid(row=0, column=1, sticky="nsew")

    # Tambahkan label untuk identifikasi
    Label(container_left, text="Weather Information", font=("Arial", 13, "bold")).pack()
    Label(container_right, text="Map View", font=("Arial", 13, "bold")).pack()

    information = Frame(container_left)
    information.pack(fill='both',expand=True,pady=15)

    weather_label = Label(information, text="Weather: -", font=("Arial", 11))
    weather_label.pack(anchor="w",pady=(2,5))
    city_label = Label(information, text="Location: -", font=("Arial", 11))
    city_label.pack(anchor="w",pady=(2,5))
    temp_label = Label(information, text=f"Temperature: {temp}\u00b0C", font=("Arial", 11))
    temp_label.pack(anchor="w",pady=(2,5))
    feels_temp_label = Label(information, text=f"Feels like temp.: {feels_temp}\u00b0C", font=("Arial", 11))
    feels_temp_label.pack(anchor="w",pady=(2,5))
    pressure_label = Label(information, text=f"Avg. Pressure: {pressure} hPa", font=("Arial", 11))
    pressure_label.pack(anchor="w",pady=(2,5))
    humidity_label = Label(information, text=f"Humidity: {humidity} %", font=("Arial", 11))
    humidity_label.pack(anchor="w",pady=(2,5))
    sea_label = Label(information, text=f"Sea Lvl. Pressure: {sea_level} hPa", font=("Arial", 11))
    sea_label.pack(anchor="w",pady=(2,5))
    ground_label = Label(information, text=f"Ground Lvl. Pressure: {ground_level} hPa", font=("Arial", 11))
    ground_label.pack(anchor="w",pady=(2,5))

    root.mainloop()
