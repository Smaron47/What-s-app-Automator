# What-s-app-Automator
The WhatsApp Bulk Message Sender is a desktop GUI tool built with Tkinter and Selenium that automates sending text messages and multimedia (images/videos) via WhatsApp Web. Users can input multiple phone numbers, compose a message, attach files, preview attachments, and dispatch in bulk—while tracking failed deliveries.
# WhatsApp Bulk Message Sender

---

## Table of Contents

1. Project Overview
2. Features
3. Technology Stack & Dependencies
4. Installation & Setup
5. Application Structure
6. Function Documentation

   * `get_user_data_dir()`
   * `send_messages()`
   * `attach_and_send_files()`
   * `send_images()`
   * `update_preview_images()`
   * `load_image()`
7. GUI Layout & Workflow
8. Error Handling
9. Security Considerations
10. Keywords
11. Author & License

---

## 1. Project Overview

The **WhatsApp Bulk Message Sender** is a desktop GUI tool built with Tkinter and Selenium that automates sending text messages and multimedia (images/videos) via WhatsApp Web. Users can input multiple phone numbers, compose a message, attach files, preview attachments, and dispatch in bulk—while tracking failed deliveries.

## 2. Features

* **Bulk Text Messaging**: Send the same text to multiple recipients sequentially.
* **Media Attachments**: Attach images and videos, preview thumbnails before sending.
* **Automatic WhatsApp Login**: Reuses the user’s Chrome profile to maintain session.
* **Failure Tracking**: Captures and lists phone numbers that failed to send.
* **Configurable Delays**: Randomized timing to mimic human behavior.

## 3. Technology Stack & Dependencies

* **Python 3.8+**
* **Tkinter** (built-in): GUI framework
* **Selenium**: Web automation
* **Pillow (PIL)**: Image loading & resizing
* **ChromeDriver**: Controls Chrome via Selenium

Install required packages:

```bash
pip install selenium pillow
```

Ensure `chromedriver` matches your Chrome version and is in `PATH`.

## 4. Installation & Setup

1. Clone or download this script.
2. Install dependencies (see above).
3. Launch WhatsApp Web in Chrome and scan the QR code once to log in.
4. Run:

   ```bash
   python whatsapp_bulk_sender.py
   ```

## 5. Application Structure

```
whatsapp_bulk_sender.py    # Main script
README.md                  # This documentation
```

## 6. Function Documentation

### `get_user_data_dir()`

Returns the path to the default Chrome user data directory for the current OS user. Ensures Selenium uses the existing session to avoid re-authentication.

### `send_messages()`

1. Reads phone numbers from the Text widget (one per line).
2. Opens Chrome with the saved WhatsApp session.
3. For each number:

   * Navigates to the chat URL.
   * Locates the message input box via XPath.
   * Sends the text and presses ENTER.
   * Records failures into the "Failed Numbers" box.
4. Closes the browser when done.

### `attach_and_send_files()`

Opens a file dialog for users to pick one or more images/videos, appends their file paths to a global list, and calls `update_preview_images()` to show thumbnails.

### `send_images()`

1. Reads the same list of phone numbers.
2. Opens Chrome session as above.
3. For each number:

   * Attaches all selected media by simulating clicks on the Attach button and file inputs.
   * Adds a caption message if provided.
   * Clicks the Send button and handles any attachment-specific delays.
   * Records failures.
4. Clears the attachment list and previews, then quits the browser.

### `update_preview_images()`

Clears any existing thumbnail frame, then rebuilds it by loading each file path via `load_image()` and packing an image Label.

### `load_image(file_path)`

Uses Pillow to open an image file, resize it to 100×100 pixels, and convert it to a Tkinter-compatible `PhotoImage`.

## 7. GUI Layout & Workflow

1. **Phone Numbers**: Multi-line Text box to enter one number per line.
2. **Message Text**: Multi-line Text box for the message body.
3. **Attach Image/Video**: Button to select media files.
4. **Send Messages**: Sends text-only messages.
5. **Send Images**: Sends media with optional caption.
6. **Failed Numbers**: Read-only Text box listing any numbers that could not be reached.

## 8. Error Handling

* Wrapped Selenium interactions in `try/except` to continue on individual failures.
* Invalid numbers or network issues append to the failure list rather than crash.

## 9. Security Considerations

* **Session Safety**: Reusing Chrome’s profile keeps your cookies—make sure no untrusted code runs in your browser profile.
* **Data Privacy**: Phone numbers and messages are processed locally and not stored persistently.

## 10. Keywords

```
Python Tkinter WhatsApp Web automation
bulk messaging Selenium
media attachment preview Pillow
Chrome profile reuse
error tracking GUI tool
Python Tkinter WhatsApp Web automation
bulk messaging Selenium
media attachment preview Pillow
Chrome profile reuse
error tracking GUI tool
```

## 11. Author & License

**Author:** Smaron Biswas
**Date:** 2025
**License:** MIT License
