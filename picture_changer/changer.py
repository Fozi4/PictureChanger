import cv2, os

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError("Image is not found")
    return cv2.resize(img,(400,400))

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

def subtract_image(img1,img2):
    return cv2.subtract(img1,img2)

def blur_image(img):
    return cv2.GaussianBlur(img,(5,5), 50)

def save_output(name, img):
    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite(f"outputs/{name}.jpg", img)

def show(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    path = input("Enter full image path (e.g. C:/Users/user/Desktop/photo.jpg): ")
    try:
        img1 = load_image(path)
        result = img1.copy()
    except FileNotFoundError:
        print("Image not found.")
        return
    run = True
    while run:
        start = input("What would you like to do with image? (gray, colored, colormaped, subtracted, blurred, sobel, s to stop): ").lower()
        match start:
            case "gray":
                result = gray_image(img1)
            case "colored":
                result = colored_image(img1)
            case "colormaped":
                result = colormap_image(img1)
            case "subtracted":
                colored = colored_image(img1)
                result = subtract_image(colored, img1)
            case "blurred":
                result =blur_image(img1)
            case "sobel":
                gray = gray_image(img1)
                result = apply_sobel(gray)
            case "s":
                run = False
                continue
            case _:
                print("Choose from the available options.")
                continue
            
        if result is not None:
            show(start.capitalize(), result)
            save = input("Do you want to save the result? (yes/no): ").lower()
            if save == "yes":
                name = input("Enter filename (without extension): ")
                save_output(name, result)


main()
