import tkinter as tk
from tkinter import filedialog
import pygame
import os
root=tk.Tk()
root.title("Music Player")
root.geometry("500x300")
pygame.mixer.init()
songs=[]
current=""
paused=False
def load_songs():
    global current
    root.directory=filedialog.askdirectory()
    for song in os.listdir(root.directory):
        name, ext =os.path.splitext(song)
        if ext==".mp3" or ext==".mpeg":
            songs.append(song)
    for song in songs:
        songlist.insert("end",song)
    songlist.selection_set(0)
    current=songs[songlist.curselection()[0]]
def play_music():
    global current,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True
def next_music():
    global current,paused
    try:
        songlist.selection_clear(0,'end')
        songlist.selection_set(songs.index(current)+1)
        current=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
def previous_music():
    global current,paused
    try:
        songlist.selection_clear(0,'end')
        songlist.selection_set(songs.index(current)-1)
        current=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
menu_list=tk.Menu(root)
root.config(menu=menu_list)
organize_menu=tk.Menu(menu_list,tearoff=False)
organize_menu.add_command(label='Select Folder',command=load_songs)
menu_list.add_cascade(label="Organize",menu=organize_menu)
songlist=tk.Listbox(root,bg="black",fg="white",width=100,height=15)
songlist.pack()
play_button=tk.PhotoImage(file='play.png')
pause_button=tk.PhotoImage(file='pause.png')
next_button=tk.PhotoImage(file='next.png')
previous_button=tk.PhotoImage(file='previous.png')
control_frame=tk.Frame(root)
control_frame.pack()
play_btn=tk.Button(control_frame,image=play_button,borderwidth=0,command=play_music)
pause_btn=tk.Button(control_frame,image=pause_button,borderwidth=0,command=pause_music)
next_btn=tk.Button(control_frame,image=next_button,borderwidth=0,command=next_music)
previous_btn=tk.Button(control_frame,image=previous_button,borderwidth=0,command=previous_music)
play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
next_btn.grid(row=0,column=3,padx=7,pady=10)
previous_btn.grid(row=0,column=0,padx=7,pady=10)

root.mainloop()