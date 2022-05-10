import cv2
imagen = cv2.imread('imagen.PNG')
image = cv2.medianBlur(imagen,5)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 50, 300)
#cv2.imshow('imagen Bordes',canny)
#canny = cv2.dilate(canny, None, iterations=1)
#canny = cv2.erode(canny, None, iterations=1)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#_,contornos,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APROX_SIMPLE)# OpenCV 3
contornos,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4
#cv2.drawContours(image, contornos, -1, (0,255,0), 2)
for c in contornos:
  #epsilon = 0.015*cv2.arcLength(c,True) # valor inexacto
  epsilon = 0.020 * cv2.arcLength(c, True)
  vertices = cv2.approxPolyDP(c,epsilon,True)
  #print(len(vertices))
  x,y,w,h = cv2.boundingRect(vertices)
  if len(vertices)==3:
    cv2.putText(image,'Triangulo', (x,y-5),0,0.60,(0,200,0),2)
  if len(vertices)==4:
    aspect_ratio = float(w)/h
    print('aspect_ratio= ', aspect_ratio)
    if aspect_ratio == 1:
      cv2.putText(image,'Cuadrado', (x,y-5),0,0.60,(0,255,0),2)
    else:
      cv2.putText(image,'Rectangulo', (x,y-5),0,0.60,(0,255,0),2)
  if len(vertices)==5:
    cv2.putText(image,'Pentagono', (x,y-5),0,0.60,(0,255,0),2)
  if len(vertices)==6:
    cv2.putText(image,'Hexagono', (x,y-5),0,0.60,(0,255,0),2)
  if len(vertices)==7:
    cv2.putText(image,'Poligono N lados', (x,y+100),0,0.60,(0,255,0),2)
  if len(vertices)>7:
    cv2.putText(image,'Circulo', (x,y+100),0,0.60,(0,255,0),2)
  cv2.drawContours(image, [vertices], 0, (0,255,0),2)
  cv2.imshow('Imagen',image)
  cv2.waitKey(0)