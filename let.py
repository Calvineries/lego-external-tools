from tkinter import *
import psutil
import pymem
import threading
import time
import keyboard

def create_overlay():
    root = Tk()
    root.title("overlay")
    root.overrideredirect(True)
    root.attributes("-transparentcolor", "red")
    root.config(bg="red")
    root.wm_attributes("-topmost", 1)

    labels = [Label(root, text="", fg="green", bg="black", font=("Arial", 25)) for _ in range(3)]
    for i, label in enumerate(labels):
        label.place(x=0, y=i*50)

    l_key = Label(root, text="Press RSHIFT to open GUI", fg="white", bg="black", font=("Arial", 8))
    l_key.place(x=0, y=150)
    l_ver = Label(root, text="1.0.3", fg="white", bg="black", font=("Arial", 7))
    l_ver.place(x=0, y=175)

    def update_labels():
        while True:
            base = memory.read_longlong(baseDll + coordinates)
            coords = [memory.read_float(base + vecOrigin + offset) for offset in (0x0, 0x4, 0x8)]
            for i, coord in enumerate(coords):
                labels[i].config(text=f"{['X', 'Y', 'Z'][i]}: {round(coord, 1)}")
            time.sleep(0.1)

    def opengui():
        global opened, gui, t_coords
        if opened:
            gui.destroy()
        else:
            gui = Toplevel(root)
            gui.geometry("150x150+0+200")
            gui.resizable(False, False)
            gui.wm_attributes("-topmost", 1)
            gui.config(bg="black")
            t_coords = [Text(gui, height=1, width=8, fg="green", bg="black", font=("Arial", 25), insertbackground="white") for _ in range(3)]
            for t_coord in t_coords:
                t_coord.pack()
            Button(gui, text="Teleport", command=lambda:set_coordinates(*[float(t.get("1.0", END)) for t in t_coords])).pack(side=LEFT)
            Button(gui, text="Fill", command=fill).pack(side=LEFT)
        opened = not opened

    def check_rshift():
        global opened
        opened = False
        while True:
            if keyboard.is_pressed('right shift'):
                opengui()
                while keyboard.is_pressed('right shift'):
                    time.sleep(0.1)
            time.sleep(0.1)

    threading.Thread(target=update_labels, daemon=True).start()
    threading.Thread(target=check_rshift, daemon=True).start()
    root.mainloop()

def set_game():
    global memory, baseDll, coordinates, vecOrigin

    games = {
        #"LEGOBatman.exe": (0x006B264C, 0x5C), //useless, no open world
        "LEGOBatman2.exe": (0x00F9A550, 0x70),
        "LEGOlotr.exe": (0x011BD93C, 0x70),
        "LEGOLCUR_DX11.exe": (0x01C77C78, 0x90),
        "LEGOMARVEL.exe": (0x015B0884, 0x70),
        "legoemmet.exe": (0x016DAC00, 0x70),
        "LEGOSWTFA_DX11.EXE": (0x027AB148, 0x90),
        "LEGO The Incredibles_DX11.exe": (0x02752DC0, 0x90),
        "LEGO DC Super-villains_DX11.exe": (0x02D9F4B0, 0x90)
    }

    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] in games:
            memory = pymem.Pymem(proc.info["name"])
            baseDll = pymem.process.module_from_name(memory.process_handle, proc.info["name"]).lpBaseOfDll
            coordinates, vecOrigin = games[proc.info["name"]]
            break
    else:
        print("[ERROR] No compatible games are currently running. Check the Github page for more information.")

def fill():
    try:
        base = memory.read_longlong(baseDll + coordinates)
        coords = [round(memory.read_float(base + vecOrigin + offset), 1) for offset in (0x0, 0x4, 0x8)]
        for t_coord, coord in zip(t_coords, coords):
            t_coord.delete("1.0", END)
            t_coord.insert(END, coord)
    except Exception:
        pass

def set_coordinates(wx: float, wy: float, wz: float):
    try:
        base = memory.read_longlong(baseDll + coordinates)
        for offset, value in zip((0x0, 0x4, 0x8), (wx, wy, wz)):
            memory.write_float(base + vecOrigin + offset, value)
    except Exception:
        pass

set_game()
create_overlay()
