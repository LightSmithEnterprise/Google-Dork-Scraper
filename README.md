Google Dork Web Scraper


Overview
Google Dork Web Scraper is a Python-based tool that allows users to perform customized Google searches using a list of pre-defined Google dorks. The tool allows users to search for specific information and vulnerabilities using search queries enhanced with various dork parameters. Results are displayed in a user-friendly interface with clickable links and options to copy URLs.

Features: /n
-Graphical interface./n
-Perform advanced Google searches using Google Dorks./n
-Display search results with clickable links./n
-Option to copy the link to the clipboard./n
-Customizable search with checkboxes for various dork options./n
-Scrollable interface for results display./n

Requirements:
-Python 3
-Tkinter (for the graphical interface)
-requests library (for making HTTP requests)
-pyperclip library (for clipboard functionality)

Setup Instructions:
To use this tool, you will need to set up a Google Custom Search Engine (CSE). Here are the steps to create a Custom Search Engine:
1) Go to the Google Programmable Search Engine page.
2) Sign in with your Google account.
3) Follow the instructions to create your own search engine.

Once your search engine is created, you'll receive two keys:
-API Key: Required for making requests to the Google Custom Search API.
-Search Engine ID (CX): Identifies your specific search engine.

Configuration:
You will need to copy and paste the API_KEY and SEARCH_ENGINE_ID into the inputs when you run the program.

This project is licensed under the MIT License. See the LICENSE file for details.
