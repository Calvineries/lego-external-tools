import pyMeow as pm
import dearpygui.dearpygui as dpg
from gui import *
import threading
import win32api
import ctypes
import os

class Colors:
    red = pm.get_color("#FF0000")
    orange = pm.get_color("orange")
    green = pm.get_color("#00FF00")
    white = pm.get_color("white")
    blue = pm.get_color("#0000FF")
    light_blue = pm.get_color("#00FFFF")
    hud = pm.get_color("#f5f5ff")
    hud_fade = pm.fade_color(pm.get_color("black"), 0.6)

def detect_current_game():
    games = {
        "LEGOBatman.exe": (0x006B264C, 0x5C, 0x006AF8B0), 
        "LEGOCloneWars.exe": (0x00BBEA18, 0x74, 0x0), 
        "LEGOBatman2.exe": (0x00F9A550, 0x70, 0x0),
        "LEGOlotr.exe": (0x011BD93C, 0x70, 0x0),
        "LEGOLCUR_DX11.exe": (0x01C77C78, 0x90, 0x01C7E640),
        "LEGOMARVEL.exe": (0x015B0884, 0x70, 0x0),
        "legoemmet.exe": (0x016DAC00, 0x70, 0x0),
        "LEGOSWTFA_DX11.exe": (0x027AB148, 0x90, 0x0),
        "LEGONINJAGO_DX11.exe": (0x024AA8F8, 0x90, 0x0),
        "LEGO The Incredibles_DX11.exe": (0x02752DC0, 0x90, 0x0),
        "LEGO DC Super-villains_DX11.exe": (0x02D9F4B0, 0x90, 0x0)
    }
    for k, v in games.items():
        if pm.process_exists(k):
            return k, v[0], v[1], v[2]
    return None

def get_coords():
    current_game = detect_current_game()
    memory = pm.open_process(current_game[0])
    baseDll = pm.get_module(memory, current_game[0])    
    local_b = pm.r_int64(memory, baseDll["base"] + current_game[1])
    return pm.r_vec3(memory, local_b + current_game[2])

def get_studs():
    current_game = detect_current_game()
    if current_game:
        if current_game[3]:
            memory = pm.open_process(current_game[0])
            baseDll = pm.get_module(memory, current_game[0])    
            base = pm.r_int64(memory, baseDll["base"] + current_game[3])
            return pm.r_uint64(memory, base)

def set_studs(amount):
    current_game = detect_current_game()
    memory = pm.open_process(current_game[0])
    baseDll = pm.get_module(memory, current_game[0])    
    base = pm.r_int64(memory, baseDll["base"] + current_game[3])
    pm.w_int64(memory, base, amount)

def teleport(x, y, z):
    current_game = detect_current_game()
    memory = pm.open_process(current_game[0])
    baseDll = pm.get_module(memory, current_game[0])    
    local_b = pm.r_int64(memory, baseDll["base"] + current_game[1])
    pm.w_vec3(memory, local_b + current_game[2], pm.vec3(x, y, z))



def start():
    gui.init_menu()
    threading.Thread(target=main, name='main', daemon=True).start()
    dpg.start_dearpygui()

def main():
    current_game = detect_current_game()

    if not current_game:
        ctypes.windll.user32.MessageBoxW(0, "No compatible games are currently running. Check the Github page for more information.", "Error.", 48)
        os._exit(0)
    pm.overlay_init(fps=60)


    while pm.overlay_loop():
        pos = get_coords()
        pm.begin_drawing()

        x_size = pm.measure_text(f"X: {str(round(pos['x'], 1))}", 24)
        pm.draw_rectangle_rounded(5, 5, x_size + 15, 30, 0.2, 4, Colors.hud_fade)
        pm.draw_rectangle_rounded_lines(5, 5, x_size + 15, 30, 0.2, 4, Colors.white, 2)
        pm.draw_text(f"X: {round(pos['x'], 1)}", 12, 11, 24, Colors.hud)

        y_size = pm.measure_text(f"Y: {str(round(pos['y'], 1))}", 24)
        pm.draw_rectangle_rounded(5, 42, y_size + 15, 30, 0.2, 4, Colors.hud_fade)
        pm.draw_rectangle_rounded_lines(5, 42, y_size + 15, 30, 0.2, 4, Colors.white, 2)
        pm.draw_text(f"Y: {round(pos['y'], 1)}", 12, 48, 24, Colors.hud)

        z_size = pm.measure_text(f"Z: {str(round(pos['z'], 1))}", 24)
        pm.draw_rectangle_rounded(5, 79, z_size + 15, 30, 0.2, 4, Colors.hud_fade)
        pm.draw_rectangle_rounded_lines(5, 79, z_size + 15, 30, 0.2, 4, Colors.white, 2)
        pm.draw_text(f"Z: {round(pos['z'], 1)}", 12, 85, 24, Colors.hud)

        pm.end_drawing()


if __name__ == "__main__":
    gui = GUI()
    start()