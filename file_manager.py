from curses import window
from re import L
from tkinter import *
import shutil
import os
from tkinter import filedialog
import easygui
from tkinter import messagebox as mb


# Opens file directory GUI, path is stored.
def open_window():

    open = easygui.fileopenbox()
    return open


# Open function
def open_file():

    # Calls GUI and stores path.
    window = open_window()

    try:
        # Opens file chosen.
        os.startfile(window)
    except:
        # If no file is present, gives error.
        mb.showinfo('confirmation', "File not found!")


# Copy/paste function
def copy_file():

    source = open_window()

    # Calls GUI and stores requested directory.
    destination = filedialog.askdirectory()

    # This copies the chose file, and pastes it in the directory requested.
    shutil.copy(source, destination)

    # Creates message box to alert success.
    mb.showinfo('confirmation', 'File Copied!')


# Delete function
def delete_file():

    del_file = open_window()

    # Checks file validity, deletes if valid.
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found!")


# Rename function
def rename_file():

    orig_file = open_window()

    # Saves directory path.
    path = os.path.dirname(orig_file)

    # Splits extension (.py) and root (file_manager) so the extension can be kept the same.
    extension = os.path.splitext(orig_file)[1]
    print("Enter a new name for the file: ")
    rename = input('')

    # Joins the previously split extension and root.
    path2 = os.path.join(path, rename+extension)
    print(path2)

    os.rename(orig_file, path2)
    mb.showinfo('confirmation', "File has been renamed...")


# Move file fuctional
def move_file():

    file = open_window()
    destination = filedialog.askdirectory()

    # Check for valid destination.
    if file == destination:
        mb.showinfo('confirmation', 'Cannot move to same address...')
    else:
        # Shutil utilizes os.rename, so if the import is a problem, utizile os function.
        shutil.move(file, destination)
        mb.showinfo('confirmation', 'File successfully moved!')


# Create folder function
def create_folder():

    folder_path = filedialog.askdirectory()
    print("Name the new folder...")
    folder_name = input('')

    path = os.path.join(folder_path, folder_name)
    os.mkdir(path)
    mb.showinfo('confirmation', 'Folder created!')


# Delete folder function
def del_folder():

    folder_path: filedialog.askdirectory()
    os.rmdir(folder_path)
    mb.showinfo('confirmation', 'Folder deleted!')


# Lists all files in folder
def file_list():

    folder_path = filedialog.askdirectory()
    list = sorted(os.listdir(folder_path))

    print(f'{folder_path} contains the files:')
    i = 0
    while(i < len(list)):
        print(list[i]+'\n')
        i += 1
