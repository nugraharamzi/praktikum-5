


img_contrass = np.zeros(img.shape, dtype= np.uint8) #Membuat variabel img_contrass untuk menampung hasil

def contrass(nilai): #Melakukan penambahan contrass dengan nilai yg menjadi parameter
    for y in range(0, img_hight):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue))/3
            gray += nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)
            
#Menampilkan beberapa hasil dengan nilai contrass 50 dan 100
contrass(20)
plt.imshow(img_contrass)
plt.title("contrass 20")
plt.show()
contrass(100)
plt.imshow(img_contrass)
plt.title("contrass 100")
plt.show()

img_contrasrgb = np.zeros(img.shape, dtype= np.uint8)

#fungsi rgb
def rgbcontrass(nilai):
    for y in range(0, img_hight):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                        red = 255
            if red < 0:
                        red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                        green = 255
            if green < 0:
                        green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                        blue = 255
            if blue < 0:
                        blue = 0
            img_contrasrgb[y][x] = (red, green, blue)
            
rgbcontrass(50)
plt.imshow(img_contrasrgb)
plt.title("contrass 50")
plt.show()
rgbcontrass(100)
plt.imshow(img_contrasrgb)
plt.title("contrass 100")
plt.show()

img_brightness = np.zeros(img.shape, dtype = np.uint8) #Membuat variabel img_brightness untuk menampung hasil

def brighter(nilai): #Melakukan penambahan brightness dengan nilai yg menjadi parameter
    for y in range(0, img_height):
        for x in range(0, img_width):
            red= img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray= (int(red)+ int(green)+int(blue))/3
            gray += nilai
            if gray > 255:
                gray= 255
            if gray<0:
                gray=0
            img_brightness[y][x] = (gray, gray, gray)

#menampilkan gambar dengan beberapa hasil dengan nilai brightness -100 dan 100
brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()

brighter(25)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()


img_autocontrass = np.zeros(img.shape, dtype=np.uint8)

def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)

autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")
plt.show()