import cv2

src = "staredad.jpg"
dest = "newimg.jpg"
scale_percentage_h = 50
scale_percentage_w = 40

img = cv2.imread(src, cv2.IMREAD_UNCHANGED)

new_width = int(img.shape[1] * scale_percentage_w / 100)
new_height = int(img.shape[0] * scale_percentage_h / 100)

dsize = (new_width, new_height)

output = cv2.resize(img, dsize)

cv2.imshow("title", img)
cv2.imwrite(dest, output)

cv2.waitKey(0)
