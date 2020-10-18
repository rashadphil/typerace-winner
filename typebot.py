import pyautogui, time, pytesseract
from PIL import Image


def process():
    time.sleep(3)
    img = pyautogui.screenshot(region=(730, 938, 1246, 256))
    img.save("words.png")
    text = pytesseract.image_to_string(Image.open("words.png"))
    result = text.replace("\n", " ")
    if result[0] == "l": #fix errors
        result = "I" + result[1:]
    result = result.replace("|", "I")
    time.sleep(2)
    print(result)
    pyautogui.typewrite(result)


process()
