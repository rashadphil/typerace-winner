import pyautogui, time, pytesseract
from PIL import Image


def process():
    found_3 = False #find 3 seconds
    im = Image.open("3.png")
    while not found_3:
        time.sleep(0.6)
        if pyautogui.locateOnScreen(im, region= (1894, 510, 102, 100)):
            found_3 = True
    img = pyautogui.screenshot(region=(730, 938, 1246, 256))
    img.save("words.png")
    text = pytesseract.image_to_string(Image.open("words.png"))
    result = clean_errors(text)
    time.sleep(3)
    print(result)
    pyautogui.typewrite(result)

def clean_errors(text):
    text = text.replace("\n", " ")
    if text[0] == "l": #fix errors
        text = "I" + text[1:]
    text = text.replace("|", "I")
    text = text.replace("[", "I")
    return text

process()


