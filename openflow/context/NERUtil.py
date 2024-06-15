from PIL import Image
import pytesseract
from datetime import datetime
import pyautogui

def image_to_text(img):
    return pytesseract.image_to_string(img)

def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return pyautogui.screenshot(f"{timestamp}.png")
