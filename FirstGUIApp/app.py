# help make gui
import tkinter as tk 
# filedialog helps pick the apps, text helps make text
from tkinter import filedialog, Text 
# run the apps that we are adding to the app 
import os 

# similar to html, the whole app, whenever you want to add a button, 
# frame or something like that then you would add it to this root
root = tk.Tk() 
# add chosen files to this array
apps = []

# if the specified path refers to a file
if os.path.isfile('./save.txt'): 
	with open('save.txt', 'r') as f: 
		# reads the file 'save.txt'
		tempApps = f.read()
		tempApps = tempApps.split(',')
		apps = [x for x in tempApps if x.strip()]

# the function for opening files
def addApp(): 
	# returns all the widgets inside the frame, in this case all the labels
	for widget in frame.winfo_children(): 
		# destroys the widget
		widget.destroy() 
	# initial directory is the place you are starting you file search from, in this case the C:/, 
	# the title "Select File" is the name of the windows explorer app that opens 
	# the filetypes are the options for the filter of filetypes, * = everything 
	# the filename variable will return the absolute path of the file selected
	filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
	filetypes=(("executables", "*.exe"), ("all files", "*.*")))
	if filename: 
		apps.append(filename)


	# loops through all the apps inside the array "apps" and adds a label to the frame with the text
	# of the path of the app
	for app in apps: 
		# makes a label and attaches it to the frame, this is also automatically centered
		label = tk.Label(frame, text=app, bg="gray")
		label.pack()

def runApps(): 
	# loops through all the paths of apps selected 
	for app in apps: 
		# opens the selected apps, os.startfile only requires the path to a file in order to open it 
		os.startfile(app) 

# creates a canvas but does not attach it to root
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# attaches the canvas to the root, the canvas also makes the GUI larger since canvas is big
canvas.pack() 

# bg = background
frame = tk.Frame(root, bg="white") 
# relx and y leaves a specified about of space
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1) 

# fg = color of text
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp) 
# attaches to root
openFile.pack() 

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack() 

for app in apps: 
	label = tk.Label(frame, text=app)
	label.pack()

# runs the root, the GUI, makes it appear
root.mainloop() 

# the with statement returns an object as a specific name and then closes it when the code finishes
with open('save.txt', 'w') as f: 
	for app in apps: 
		f.write(app + ',')