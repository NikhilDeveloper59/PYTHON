# Binary File Handling (Image/PDF etc.)

# Copy image


with open("photo.jpg",'rb') as f1:
    data = f1.read()

with open("photo.jpg",'wb') as f2:
    f2.write(data)

print("Image copied successfully ✅")