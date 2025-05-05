

import os
import random
import string
import time
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


from PIL import Image, ImageTk



BASE_URL = "https://web.whatsapp.com/"
CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

# Get the current user's profile name
user_profile_name = os.path.basename(os.path.expanduser("~"))

sleep_duration = random.uniform(4, 7)

# Create a list to store the loaded images for display
loaded_images = [] 




# Function to get the user data directory path
def get_user_data_dir():
    user_data_dir = f"C:\\Users\\{user_profile_name}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    return user_data_dir

# Initialize the Tkinter app
app = tk.Tk()
app.title("WhatsApp Bulk Message Sender")
app.geometry("400x600")


# Function to send messages
def send_messages():
    numbers = number_entry.get("1.0", tk.END).strip().split("\n")
    message = message_entry.get("1.0", tk.END).strip()
    user_data_dir = get_user_data_dir()
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(BASE_URL)
    time.sleep(10)
    browser.maximize_window()

    for number in numbers:
        if number:
            try:
                phone = number
                browser.get(CHAT_URL.format(phone=phone))
                time.sleep(sleep_duration)

                inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                input_box = WebDriverWait(browser, 60).until(
                    expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
                )
                time.sleep(1)
                input_box.send_keys(message)
                time.sleep(sleep_duration)
                input_box.send_keys(Keys.ENTER)
                time.sleep(sleep_duration)
            except:
                # If sending failed, append the number to the failed numbers text box
                failed_numbers_text.insert(tk.END, f"{number}\n")
    browser.quit()

file_paths_to_send = []

# Function to attach and send images or videos
def attach_and_send_files():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        # Add selected file paths to the list
        file_paths_to_send.extend(file_paths)
        update_preview_images()

# Function to send images
def send_images():
    numbers = number_entry.get("1.0", tk.END).strip().split("\n")
    user_data_dir = get_user_data_dir()
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    message = message_entry.get("1.0", tk.END).strip()
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(BASE_URL)
    time.sleep(10)
    browser.maximize_window()

    for number in numbers:
        if number:
            try:
                phone = number
                browser.get(CHAT_URL.format(phone=phone))
                time.sleep(sleep_duration)
                
                for file_path in file_paths_to_send:
                    attachment_box = WebDriverWait(browser, 60).until(
                        expected_conditions.presence_of_element_located((By.XPATH, '//div[@title="Attach"]'))
                    )
                    attachment_box.click()
                    time.sleep(sleep_duration)
                    file_input = WebDriverWait(browser, 60).until(
                        expected_conditions.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
                    )
                    file_input.send_keys(file_path)
                    time.sleep(sleep_duration)
                    if len(file_paths_to_send) > 1:
                        i=1
                        while i < len(file_paths_to_send):
                            try:
                                    #print("Done 1",i)
                                    addfile_button=  WebDriverWait(browser, 60).until(
                                    expected_conditions.presence_of_element_located((By.XPATH, '//input[@accept="*"]'))
                                    )
                                    addfile_button.send_keys(file_paths_to_send[i])
                                    sleep(1)
                                    i += 1
                                
                            except:
                                i += 1
                                
                                #print("Not working the fucking multiple images")    
                    
                    try:
                        addfile_button1=  WebDriverWait(browser, 60).until(
                        expected_conditions.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]'))
                        )
                        addfile_button1.send_keys(message)
                        addfile_button1.send_keys(Keys.ENTER)
                        sleep(1)
                    except:
                        pass
                        #print("Not working in the fucking Message")    
                    #print("Sending to the user..... ")
                    send_button = WebDriverWait(browser, 60).until(
                        expected_conditions.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]'))
                    )
                    send_button.click()
                    #
                    # 
                    #print("Image sent successfully")
                    time.sleep(sleep_duration)
                    break
            except:
                # If sending failed, append the number to the failed numbers text box
                failed_numbers_text.insert(tk.END, f"{number}\n")
    
    file_paths_to_send.clear()  # Clear the list after sending all images
    update_preview_images()  # Clear the image previews
    browser.quit()

# Function to update the image previews
def update_preview_images():
    global preview_frame  # Access the global variable
    try:
        if preview_frame:
            preview_frame.destroy()  # Clear the existing preview frame
    except:
        pass
    
    if file_paths_to_send:
        preview_frame = tk.Frame(app)
        preview_frame.pack()
        for file_path in file_paths_to_send:
            image = load_image(file_path)
            if image:
                loaded_images.append(image)  # Store the loaded image
                label = tk.Label(preview_frame, image=image)
                label.image = image  # Keep a reference to the image
                label.pack(side=tk.LEFT)

# Function to load and convert images using Pillow (PIL)
def load_image(file_path):
    try:
        img = Image.open(file_path)
        img = img.resize((100, 100))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        return photo
    except Exception as e:
        #print(f"Error loading image: {e}")
        return None




# Create and pack widgets
number_label = tk.Label(app, text="Enter Phone Numbers (One per line):")
number_label.pack()

number_entry = tk.Text(app, height=6, width=30)
number_entry.pack()

message_label = tk.Label(app, text="Enter Message:")
message_label.pack()

message_entry = tk.Text(app, height=6, width=30)
message_entry.pack()

button_row = tk.Frame(app)
button_row.pack()

attach_button = tk.Button(button_row, text="Attach Image/Video", command=attach_and_send_files)
attach_button.pack(side=tk.LEFT)

send_button = tk.Button(button_row, text="Send Messages", command=send_messages)
send_button.pack(side=tk.RIGHT)

# Create a button to send images
send_images_button = tk.Button(app, text="Send Images", command=send_images)
send_images_button.pack()

# Initialize the image preview frame
preview_frame = tk.Frame(app)
preview_frame.pack()





failed_label = tk.Label(app, text="Failed Numbers list: ")
failed_label.pack()

# Create a text box to display failed numbers
failed_numbers_text = tk.Text(app, height=6, width=30)
failed_numbers_text.pack()







app.mainloop()
