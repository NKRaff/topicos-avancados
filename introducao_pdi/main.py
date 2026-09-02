import cv2

img = cv2.imread('ifpe_logomarca.png', cv2.IMREAD_COLOR)

# Blue
for i in range(0, 60):
  for j in range(0, 60):
    img[i, j] = [255, 0, 0]

# Green
for i in range(60, 120):
  for j in range(60, 120):
    img[i, j] = [0, 255, 0]

# Red
for i in range(120, 180):
  for j in range(120, 180):
    img[i, j] = [0, 0, 255]

# Orange
for i in range(0, 90):
  for j in range(120, 210):
    img[i, j] = [20, 102, 204]

cv2.imwrite('logo_modificado.png', img)