import cv2, os

def gray_image(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def colored_image(img):
    print("Available color mods: rgb, hsv, lab, ycrcb, xyz, luv")
    colored_input = input("Enter color mode: ").lower()
    color_modes = {
        "rgb": cv2.COLOR_BGR2RGB,
        "hsv": cv2.COLOR_BGR2HSV,
        "lab": cv2.COLOR_BGR2LAB,
        "ycrcb": cv2.COLOR_BGR2YCrCb,
        "xyz": cv2.COLOR_BGR2XYZ,
        "luv": cv2.COLOR_BGR2LUV
    }
    if colored_input in color_modes:
        return cv2.cvtColor(img, color_modes[colored_input])
    else:
        print("Invalid choice. Returning original image.")
        return img

def colormap_image(img):
    print("Available colormaps: Jet, Hot, Cool")
    cmap_input = input("Enter colormap type: ").upper()
    cmap_dict = {
        "JET": cv2.COLORMAP_JET,
        "HOT": cv2.COLORMAP_HOT,
        "COOL": cv2.COLORMAP_COOL
    }
    if cmap_input in cmap_dict:
        return cv2.applyColorMap(img, cmap_dict[cmap_input])
    else:
        print("Invalid choice. Returning oryginal img")
        return img

def apply_sobel(gray):
    x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    return cv2.magnitude(x, y)

def match_size_and_channels(img1, img2):
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    if len(img1.shape) == 2:
        img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    if len(img2.shape) == 2:
        img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    return img1, img2


def subtract(img):
    print("""
Choose image transformation before subtraction:
[1] Convert to Grayscale
[2] Apply Color Mode
[3] Apply Colormap
    """)
    choice = input("Choose: ")
    modified = None
    match choice:
        case "1":
            modified = gray_image(img)
        case "2":
            modified = colored_image(img)
        case "3":
            modified = colormap_image(img)
        case _:
            print("Invalid option. Returning original image.")
            return img
    
    img1, img2 = match_size_and_channels(modified, img)
    return subtract_image(img1, img2)

def subtract_image(img1,img2):
    return cv2.subtract(img1,img2)

def blur_image(img):
    return cv2.GaussianBlur(img,(5,5), 50)


def show(title,img):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()