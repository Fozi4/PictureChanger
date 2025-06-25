from filters import *

def load_image(path):
    img = cv2.imread(path)
    global original
    original = img
    if img is None:
        raise FileNotFoundError("Image is not found")
    return cv2.resize(img,(400,400))

def save_output(name, img):
    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite(f"outputs/{name}.jpg", img)
    
def main():
    path = input("Enter full image path (e.g. C:/Users/user/Desktop/photo.jpg): ")
    try:
        img1 = load_image(path)
        result = img1.copy()
    except FileNotFoundError:
        print("Image not found.")
        return
        
    options = {
    1: lambda img: gray_image(img),
    2: lambda img: colored_image(img),
    3: lambda img: colormap_image(img),
    4: lambda img: subtract(img),
    5: lambda img: blur_image(img),
    6: lambda img: apply_sobel(gray_image(img)),
    7: lambda img: original.copy()
    }
    while True:
        print("""
Choose operation:
[1] Convert to Grayscale
[2] Apply Color Mode
[3] Apply Colormap
[4] Subtract
[5] Blur Image
[6] Apply Sobel
[7] Reset to original
[0] Exit
        """)
        
        try:
            choose = int(input(""))
        except ValueError:
            print("Please enter a number")
        if choose == 0:
            print("Exiting")
            break
        if choose not in options:
            print("Invalid choice. Try again.")
            continue
        
        result = options[choose](result)
        
        if result is not None:
            show("img",result)
            save = input("Do you want to save the result? (yes/no): ").lower()
        
        if save == "yes":
            name = input("Enter filename (without extension): ")
            save_output(name, result)
         
main()
