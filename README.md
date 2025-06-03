## LET: Lego-External-Tools
Display and change your location with an external overlay for multiple Lego games.  
Now with a studs/money editor.  
Video demonstration (very old version): https://youtu.be/WJvRg-DrFjM  

### Setup
1) Install python and run: ```pip install dearpygui pywin32```
2) Install PyMeow module: https://github.com/qb-0/pyMeow
3) Launch your Lego game, and make sure the game is not in fullscreen mode if you want to see the overlay.
4) In your Lego game, go to a place where you can move your character (basically don't stay on the main menu).
5) Run the script: ```py app.py```
<details>
  <summary>How to launch my game in windowed fullcreen if the game has not a windowed option?</summary>
  The only way is to use third party software. Like <a href="https://www.special-k.info/">Special K</a> or <a href="https://sourceforge.net/projects/dxwnd/">DXWnd</a>.<br>
</details>

### Supported Games
|Game|Teleportation|Money editor
|-|-|-|
LEGO® Star Wars™ - The Complete Saga|✅|✅
LEGO® Indiana Jones™: The Original Adventures|✅|✅
LEGO® Batman™: The Videogame|✅|✅
LEGO® Star Wars™ III - The Clone Wars|✅|✅
LEGO® Batman™ 2: DC Super Heroes|✅|-
LEGO® The Lord of the Rings™|✅|-
LEGO® City Undercover|✅|✅
LEGO® Marvel™ Super Heroes|✅|-
The LEGO® Movie - Videogame|✅|-
LEGO® STAR WARS™: The Force Awakens|✅|-
The LEGO® NINJAGO® Movie Video Game|✅|-
LEGO® The Incredibles|✅|-
LEGO® DC Super-Villains|✅|-

Only official Steam versions work.

### Planned changes
- Support more games
- Make it easier to access the window
- Support multiple characters
