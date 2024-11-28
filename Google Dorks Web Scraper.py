"""
MIT License

Copyright (c) 2024 LightSmith Empire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
import urllib.parse
import webbrowser
import pyperclip

# Function to ask for API Key and Search Engine ID
def ask_for_api_credentials():
    global API_KEY, SEARCH_ENGINE_ID
    API_KEY = simpledialog.askstring("API Key", "Enter your Google Custom Search API Key:")
    if not API_KEY:
        messagebox.showerror("Error", "API Key is required!")
        window.quit()
        return

    SEARCH_ENGINE_ID = simpledialog.askstring("Search Engine ID", "Enter your Google Custom Search Engine ID:")
    if not SEARCH_ENGINE_ID:
        messagebox.showerror("Error", "Search Engine ID is required!")
        window.quit()
        return

# Your ASCII art (modified) - add it as a string
ascii_art = """
.____    .__       .__     __   _________       .__  __  .__      ___________       __                            
|    |   |__| ____ |  |___/  |_/   _____/ _____ |__|/  |_|  |__   \_   _____/ _____/  |_  ________________________|__| ______ ____  
|    |   |  |/ ___\|  |  \   __\_____  \ /     \|  \   __\  |  \   |    __)_ /    \   __\/ __ \_  __ \____ \_  __ \  |/  ___// __ \ 
|    |___|  / /_/  >   Y  \  | /        \  Y Y  \  ||  | |   Y  \  |        \   |  \  | \  ___/|  | \/  |_> >  | \/  |\___ \\  ___/ 
|_______ \__\___  /|___|  /__|/_______  /__|_|  /__||__| |___|  / /_______  /___|  /__|  \___  >__|  |   __/|__|  |__/____  >\___  >
        \/ /_____/      \/            \/      \/              \/          \/     \/          \/      |__|                 \/     \/  
"""

# Function to perform the search using Google Custom Search API
def perform_search(query, selected_dorks):
    search_query = query
    for dork, entry in selected_dorks.items():
        var, input_entry = entry  # Unpack the tuple
        if var.get():  # If the checkbox is selected, append the input value
            search_query += f" {dork}{input_entry.get()}"  # Get the input value

    # URL encode the search query
    encoded_query = urllib.parse.quote(search_query)

    # Call the Google Custom Search API
    url = f"https://www.googleapis.com/customsearch/v1?q={encoded_query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Display the results in a scrollable window
        if 'items' in data:
            result_window = tk.Toplevel(window)
            result_window.title("Search Results")

            # Create a canvas and scrollbar for scrolling
            canvas = tk.Canvas(result_window, bg="black")
            scrollbar = tk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=scrollbar.set)

            result_frame = tk.Frame(canvas, bg="black")
            canvas.create_window((0, 0), window=result_frame, anchor="nw")

            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)

            result_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            # Function to open links on left-click
            def open_link(event, url):
                webbrowser.open(url)

            # Function to copy link on right-click
            def copy_link(event, url):
                pyperclip.copy(url)
                messagebox.showinfo("Copied", "Link has been copied to clipboard.")

            # Add the search results with clickable and copyable links
            for i, item in enumerate(data['items']):
                result_label = tk.Label(result_frame, text=f"{i + 1}. {item['title']}", font=('Arial', 12, 'bold'), fg="green", bg="black")
                result_label.pack(pady=2, anchor="w")

                link_label = tk.Label(result_frame, text=item['link'], font=('Arial', 10), fg='green', cursor="hand2", bg="black")
                link_label.pack(pady=2, anchor="w")
                
                # Bind left-click to open link and right-click to copy the link
                link_label.bind("<Button-1>", lambda e, url=item['link']: open_link(e, url))
                link_label.bind("<Button-3>", lambda e, url=item['link']: copy_link(e, url))

                snippet_label = tk.Label(result_frame, text=item['snippet'], font=('Courier New', 10), wraplength=400, fg="green", bg="black")
                snippet_label.pack(pady=5, anchor="w")

        else:
            messagebox.showinfo("No Results", "No results found for your search.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to start the search based on the input and selected dorks
def on_search():
    query = search_entry.get()
    selected_dorks = {dork: entry for dork, entry in dorks.items() if entry[0].get()}
    perform_search(query, selected_dorks)

# Main Tkinter window setup
window = tk.Tk()
window.title("LightSmith Enterprise Dork Scraper")
window.geometry("1000x600")
window.configure(bg="black")  # Set background color to black

# Ask the user for API credentials before proceeding
ask_for_api_credentials()

# Create a label to display the ASCII art at the top of the window
ascii_label = tk.Label(window, text=ascii_art, font=('Courier New', 8), fg="lightgreen", bg="black", justify="left")
ascii_label.pack(pady=10)

# Canvas and Scrollbar for the main page (search input and dorks)
main_canvas = tk.Canvas(window, bg="black")
main_scrollbar = tk.Scrollbar(window, orient="vertical", command=main_canvas.yview)
main_canvas.configure(yscrollcommand=main_scrollbar.set)

# Frame to hold search bar, dorks, and button
main_frame = tk.Frame(main_canvas, bg="black")

# Create a window inside the canvas to scroll
main_canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Pack the scrollbar and canvas
main_scrollbar.pack(side="right", fill="y")
main_canvas.pack(side="left", fill="both", expand=True)

# Bind configure event to update scroll region
main_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
)

# Entry box and button for search query (in a frame for horizontal layout)
search_frame = tk.Frame(main_frame, bg="black")
search_frame.pack(pady=20)

# Entry box for the search query
search_entry = tk.Entry(search_frame, font=('Courier New', 12), width=50, bg="black", fg="lightgreen")
search_entry.pack(side="left", padx=10)

# Search button next to the entry box
search_button = tk.Button(search_frame, text="Scrape", font=('Courier New', 12), command=on_search, bg="black", fg="lightgreen")
search_button.pack(side="left")

# Dictionary to store checkboxes and input entries for Google dorks
dorks = {}

# Example Google dorks with checkboxes and input fields (Restored List)
dorks_list = [
    ("filetype:pdf", "PDF Filetype"),
    ("intitle:index.of", "Index of Pages"),
    ("inurl:admin", "Admin Pages"),
    ("inurl:login", "Login Pages"),
    ("inurl:wp-admin", "WordPress Admin"),
    ("site:gov", "Government Sites"),
    ("site:edu", "Educational Sites"),
    ("intitle:protected", "Password-Protected Pages"),
    ("inurl:backup", "Backup Files"),
    ("intext:username", "Pages with Username"),
    ("intext:password", "Pages with Password"),
    ("inurl:php?id=", "PHP ID Vulnerabilities"),
    ("inurl:download", "Download Pages"),
    ("intitle:search", "Search Pages"),
    ("intitle:login", "Login Pages"),
    ("filetype:xls", "Excel Files"),
    ("filetype:doc", "Word Documents"),
    ("filetype:ppt", "PowerPoint Files"),
    ("inurl:phpmyadmin", "PHPMyAdmin Pages"),
    ("intitle:admin", "Admin Pages"),
    ("inurl:/login", "Login Pages with Slash"),
    ("inurl:/admin", "Admin Pages with Slash"),
    ("intitle:site:inurl:", "Site and URL Dork"),
    ("intext:password filetype:log", "Password Logs")
]

# Add checkboxes and input fields for each dork
for dork, label in dorks_list:
    var = tk.BooleanVar()
    entry = tk.Entry(main_frame, font=('Courier New', 12), bg="black", fg="lightgreen")
    checkbox = tk.Checkbutton(main_frame, text=label, variable=var, fg="green", bg="black")
    checkbox.pack(anchor="w")
    entry.pack(pady=5)
    dorks[dork] = (var, entry)

# Start Tkinter event loop
window.mainloop()
