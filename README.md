## LET: Lego-External-Tools
Display and change your location with an external overlay for multiple Lego games.  
Now with a studs/money editor.  
Video demonstration (very old version): https://youtu.be/WJvRg-DrFjM  

### Setup
1) Install python and run: ```pip install dearpygui pywin32```
2) Install PyMeow module: https://github.com/qb-0/pyMeow
3) Launch your Lego game, and make sure the game is not in fullscreen mode.
4) In your Lego game, go to a place where you can move your character (basically don't stay on the main menu).
5) Run the script: ```py app.py```
<details>
  <summary>How to launch my game in windowed mode?</summary>
  <h2>LEGO® City Undercover & LEGO® STAR WARS™: The Force Awakens & LEGO® The Incredibles & LEGO® DC Super-Villains</h2> In the game options, enable Windowed mode.<br>
  <h2>LEGO® Batman™ 2: DC Super Heroes & LEGO® The Lord of the Rings™ & LEGO® Marvel™ Super Heroes & The LEGO® Movie - Videogame</h2> The only way is to use third party software.<br>
  1) Download and launch <a href="https://sourceforge.net/projects/dxwnd/">DXWnd</a><br>
  2) Press "Edit", then "Add" and select the path of the .exe of the game.<br>
  3) Configure the game in DXWnd so that the game displays at the correct size.<br>
  4) Launch the game.
</details>

### Supported Games
|Game|Teleportation|Money editor
|-|-|-|
LEGO® Batman™: The Videogame|✅|✅
LEGO® Star Wars™ III - The Clone Wars|✅|-
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
