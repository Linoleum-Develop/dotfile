# Author        : Sebastian Dreyer
# EMail         : sdreyerb@gmail.com
# Enterprise    : Linolium - Develop
# Date          : 11 - 19 - 2021
#  _ _ _ _
# |       |
# |       |
# |       |
# |       |  I N O L E U M
# |       |
# |       |     D E V E L O P      
# |       |_ _ _ _ _ _ 
# |                   |
# |                   |
# |_ _ _ _ _ _ _ _ _ _|
#
# Configuration for Qtile windows manager



## Imports packege
import os
import re
import socket
import subprocess
from libqtile import hook
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile, bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

## Programs choice
mod = "mod4"            #Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"    #Terminal emulator of your choice
myBrowser = "firefox"   #Browser of your choice
myAppLuncher = "rofi"   #Application launcher of your choice
myEditor = "code"       #Source code editor of your choice
myFM = "thunar"		#File manager app 

## Keybinding
keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), lazy.layout.section_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), lazy.layout.section_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), lazy.layout.section_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), lazy.layout.shrink(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), lazy.layout.grow(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc="toggle window between minimum and maximus sizes"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip window focus to other window"),

    # Switch focus to specific monitor (out of three)
    Key([mod], "a", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    Key([mod], "s", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
    Key([mod], "d", lazy.to_screen(2), desc='Keyboard focus to monitor 3'),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),    
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Change terminal for "alacrity" //
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    # Set application launcher
    Key([mod], "v", lazy.spawn(myAppLuncher + " -show run"), desc="Launch rofi"),
    # Set Browser
    Key([mod], "b", lazy.spawn(myBrowser), desc="launch browser selection"),
    # Set Editor
    Key([mod], "c", lazy.spawn(myEditor), desc="launch editor selection"),
    # Set File Manager
    Key([mod], "f", lazy.spawn(myFM), desc="launch file manager selection"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Auxiliar app launcher
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

##Device shortcut
    #Key([], "XF86AudioRaiseVolume",
    #    lazy.spawn("amixer -q set Master 3dB+")),
    #Key([], "XF86AudioLowerVolume",
    #    lazy.spawn("amixer -q set Master 3dB-")),
    #Key([], "XF86AudioMute",
    #    lazy.spawn("amixer -D pulse set Master toggle")),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("light -U 5")),
]    

## Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

## color palette

colors = [["#000000", "#000000"], # 0 Background
          ["#668DDA", "#668DDA"], # 1 Foreground
          ["#C70039", "#C70039"], # 2 Icons active color
          ["#B3C6ED", "#B3C6ED"], # 3 Icons inactive color
          ["#C70039", "#C70039"], # 4 Border color for icons or widget
          ["#C70039", "#C70039"], # 5 Widget icons foreground
          ["#E6ECF9", "#E6ECF9"], # 6 window name
          ["#B3C6ED", "#B3C6ED"], # 7 background for inactive screens
          ["#FFFFFF", "#FFFFFF"]  # 8 Icons remarks
]

## Layout default configuration
layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": colors[2],
                "border_normal": colors[3]
}

layouts = [
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme, ratio=0.60),
    layout.MonadWide(**layout_theme, ratio=0.65),
    layout.Max(**layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

##Windows icon and layout
groups = [Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadtall"),
          Group("", layout="monadwide")
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

##Prompt presentation
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

## Default widget settings
widget_defaults = dict(
    font="UbuntuMono Nerd Font Mono",
    fontsize = 12,
    padding = 2,
    background = colors[0],
    foreground = colors[1]
)
extension_defaults = widget_defaults.copy()
icon_size=20
def init_widgets_list():
    widgets_list = [
            widget.Sep(
                       padding = 10,
                       foreground = colors[0],
                       background = colors[0]
                       ),
            widget.GroupBox(
                       fontsize = icon_size,
                       padding_y = 2,
                       padding_x = 4,
                       borderwidth = 2,
                       active = colors[2],
                       inactive = colors[3],
                       disable_drag = True,
                       rounded = False,
                       highlight_color = colors[2],
                       highlight_method = "border",
                       this_current_screen_border = colors[2],
                       this_screen_border = colors [2],
                       other_current_screen_border = colors[1],
                       other_screen_border = colors[1],
                       foreground = colors[1],
                       background = colors[0]
                       ),
            widget.CurrentLayout(),
            widget.Prompt(
                       prompt = prompt,
                       padding = 10,
                       foreground = colors[1],
                       background = colors[0]
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = colors[0]
                       ),
            widget.WindowName(
                       foreground = colors[3],
                       background = colors[0],
                       padding = 0
                       ),
            widget.Sep(
                       linewidth = 2,
                       padding = 6,
                       foreground = colors[5],
                       background = colors[0]
                       ),
            widget.Memory(
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty" + ' -e htop')},
                       format="Mem {MemUsed: .0f}MB \n{MemPercent}%",
                       measure_mem="M",
                       ),   
            widget.CPU(
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty" + ' -e htop')},
                       format="CPU {freq_current}GHz \n{load_percent}%",
                       padding = 2
                       ),
            widget.Sep(
                       linewidth = 2,
                       padding = 6,
                       foreground = colors[5],
                       background = colors[0]
                       ),
            widget.TextBox(
                       text = " ",
                       fontsize = icon_size,
                       padding = 2,
                       foreground = colors[5],
                       background = colors[0]
                       ),
            widget.Clock(
                        format=" %a-%d/%m/%y",
                        padding = 2,
                        ), 
            widget.TextBox(
                       text = " ",
                       fontsize = icon_size,
                       padding = 2,
                       foreground = colors[5],
                       background = colors[0]
                       ),
            widget.Clock(
                        format=" %H:%M ",
                        padding = 2,
                        ),
            widget.Sep(
                       linewidth = 2,
                       padding = 6,
                       foreground = colors[5],
                       background = colors[0]
                       ),            
            widget.TextBox(
                       text = "",
                       fontsize = icon_size,
                       padding = 2,
                       foreground = colors[5],
                       background = colors[0]
                       ),
            widget.Backlight(
                    backlight_name="radeon_bl0",
                ),            
            widget.Systray(),
            widget.Sep( 
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[0],
                    background = colors[0]
            ),
            widget.QuickExit(
                    default_text="⏻",
                    fontsize=icon_size,
                    countdown_format="{}",
                    foreground= colors[5]
                ),
            widget.Sep( 
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[0],
                    background = colors[0] 
            ),      
        ]
    return widgets_list

##Windows config on diferent monitor
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    #del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=28)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=28)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=28))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

## Startup programs
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
