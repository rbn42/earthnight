# Earthnight
Nasa Earth Night Wallpaper for Virtual Desktops

# Dependencies
`wget` `imagemagick` `python-ewmh` `python-gobject`

# Generate wallpapers
```sh
python ./generate_wallpapers.py [display resolution][virtual desktop grid size]
#Example
python ./generate_wallpapers.py 1920x1080 4x4
```

# Display wallpapers
```sh
python ./main.py
```

#Name 4x4 Grids in Kwin
If you happen to use Kwin5 with 4x4 virtual desktops, you can name the virtual desktops by adding the following configuration to ~/.config/kwinrc.
```
[Desktops]
Name_1=Alaska
Name_10=South America
Name_11=South Africa
Name_12=Australia
Name_13=Antarctica
Name_14=Antarctica
Name_15=Antarctica
Name_16=Antarctica
Name_2=Greenland
Name_3=Europa
Name_4=Russia
Name_5=West Coast
Name_6=East Coast
Name_7=Africa
Name_8=Asia
Name_9=Pacific Ocean
Number=16
Rows=4
```
