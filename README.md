Overview
Google Dork Web Scraper is a simple Python-based tool that allows users to easily perform customized Google searches using a list of pre-defined Google dorks. The tool is designed to make searching for specific information and vulnerabilities straightforward, by enhancing search queries with various dork parameters. The results are displayed in a user-friendly interface with clickable links and the option to copy URLs.


Features: 

-Graphical interface.

-Perform advanced Google searches using Google Dorks.

-Display search results with clickable links.

-Option to copy the link to the clipboard.

-Customizable search with checkboxes for various dork options.

-Scrollable interface for results display.


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
