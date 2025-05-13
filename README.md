# Book-extension

# Development Setup and Implementation Instructions

## Prerequisites:
- Python 3.x installed
- Flask and necessary libraries installed:
  ```bash
  pip install Flask PyMuPDF ebooklib flask-cors
  ```
- Chrome, Edge, or Firefox browser

## Backend Server Setup:
1. Navigate to the backend server directory and run the server:
   ```bash
   python server.py
   ```
   The server will run on `http://localhost:5000`.

## Extension Setup:
1. Open the browser and navigate to `chrome://extensions/` (or the equivalent for Edge/Firefox).
2. Enable `Developer Mode` (for Chrome/Edge).
3. Click `Load unpacked` and select the extension folder.
4. The extension will be loaded, and its icon will appear in the browser toolbar.

## Testing the Extension:
1. Click the extension icon to open the popup.
2. Upload a PDF or EPUB file.
3. The server will process the file and open the `viewer.html` page.
4. The pages will be displayed in a two-page book-like view.

## Additional Notes:
- The extension communicates with the backend server via HTTP requests.
- Ensure the server is running before interacting with the extension.
- Debugging can be done through the browser's developer console and the terminal running the Flask server.
