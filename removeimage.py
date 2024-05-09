import os
import shutil
import re

def find_used_icons(lua_file):
    used_icons = set()
    with open(lua_file, 'r') as f:
        for line in f:
            match = re.search(r"image\s*=\s*'([^']+\.png)'", line)
            if match:
                icon_path = match.group(1)
                used_icons.add(icon_path)
    return used_icons

def move_unused_icons(icon_folder, lua_file, destination_folder):
    used_icons = find_used_icons(lua_file)
    all_icons = [f for f in os.listdir(icon_folder) if f.endswith('.png')]
    unused_icons = set(all_icons) - used_icons
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    print("Used icons:", used_icons)
    print("All icons:", all_icons)
    print("Unused icons:", unused_icons)
    
    for icon in unused_icons:
        icon_path = os.path.join(icon_folder, icon)
        destination_path = os.path.join(destination_folder, icon)
        shutil.move(icon_path, destination_path)
        print(f"Moved {icon} to {destination_folder}")



# Kullanım örneği
icon_folder = "" # icon klasörü
lua_file = "\items.lua" # lua klasörü 
destination_folder = "" # çıkarılan iconların klasörü

move_unused_icons(icon_folder, lua_file, destination_folder)