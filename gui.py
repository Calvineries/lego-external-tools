import dearpygui.dearpygui as dpg
import app


def fill():
    player_data = app.get_coords()
    dpg.set_value("c_x", value=round(player_data['x'],1))
    dpg.set_value("c_y", value=round(player_data['y'],1))
    dpg.set_value("c_z", value=round(player_data['z'],1))

def teleport():
    app.teleport(dpg.get_value("c_x"), dpg.get_value("c_y"), dpg.get_value("c_z"))

def studs():
    studs = app.get_studs()
    if studs == None:
        dpg.configure_item("money", show=False)
    else:
        return studs
def setstuds():
    amount = dpg.get_value("m_x")
    app.set_studs(int(amount))


class GUI():
    def init_menu(self) -> None:
        dpg.create_context()
        dpg.create_viewport(title="Lego External Tools", decorated=True, width=600, height=400)
        with dpg.window(tag='w_main'):
            with dpg.tab_bar():
                with dpg.tab(label='Teleport'):
                    dpg.add_input_float(step=0,label='X', tag='c_x', default_value=0.0)
                    dpg.add_input_float(step=0,label='Y', tag='c_y', default_value=0.0)
                    dpg.add_input_float(step=0,label='Z', tag='c_z', default_value=0.0)
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="Teleport", callback=teleport)
                        dpg.add_button(label="Fill", callback=fill)
                with dpg.tab(label='Money', tag='money'):
                    with dpg.group(horizontal=True):
                        dpg.add_input_text(tag='m_x', default_value=studs())
                        dpg.add_button(label="Set Studs", callback=setstuds)
                    with dpg.group(horizontal=True):
                        dpg.add_input_int(step=0, tag='m_y', default_value=0, show=False)
                        dpg.add_button(label="Set Bricks", callback=teleport, show=False)

                with dpg.tab(label='About'):
                    dpg.add_text("[Lego External Tools]")
                    dpg.add_text("Version: 2.0.1")
                    dpg.add_text("")
                    dpg.add_text("© Calvineries.")
                    dpg.add_text("")
                    dpg.add_text("github.com/Calvineries/lego-external-tools", color=(28, 47, 240))

        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core) 
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 20, 7 , category=dpg.mvThemeCat_Core) 
                dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 20 , category=dpg.mvThemeCat_Core) 

        dpg.bind_theme(global_theme)

        #dpg.show_style_editor()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("w_main", True)
