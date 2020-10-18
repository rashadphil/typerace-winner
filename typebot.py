import pyautogui, time, pytesseract
from PIL import Image


def process():
    found_3 = False #find 3 seconds
    three_img = Image.open("3.png")
    print("Searching for ':03'")
    while not found_3:
        if pyautogui.locateOnScreen(three_img):
            found_3 = True
            print("FOUND':03'")

    img = pyautogui.screenshot(region=(730, 960, 1246, 300))
    img.save("words.png")
    text = pytesseract.image_to_string(Image.open("words.png"))
    result = clean_errors(text)
    print(result)
    time.sleep(2.5)
    pyautogui.press(result[0].upper()) #because of glitch sometimes
    pyautogui.typewrite(result[1:])

def clean_errors(text):
    text = text.replace("\n", " ")
    if text[0] == "l": #fix errors
        text = "I" + text[1:]
    text = text.replace("|", "I")
    text = text.replace("[", "I")

    if text[1].isalpha() and text[1].upper() == text[1]: #means OCR detected the cursor as an I
        text = text[1:]

    end_idx = text.find("change display format")
    text = text[:end_idx].rstrip()
    return text

process()


