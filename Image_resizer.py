import cv2

img = input("enter image with path and with extention: ")
new_image = input("enter you new image name: ")

try:
    ex = img.split(".")[1]
except:
    print("enter image correctly with extension or path.")


enter_width = int(input("enter width: "))
enter_height = int(input("enter height: "))

image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
resized_image = cv2.resize(image, (enter_width, enter_height)) 

# cv2.imshow("Image", resized_image)

try:
    new_ig = new_image.split(".")[1]
    new_ig = new_image
    cv2.imwrite(f"{new_ig}", resized_image)
except:
    new_ig = new_image
    cv2.imwrite(f"{new_ig}.{ex}", resized_image)

cv2.waitKey(0)
