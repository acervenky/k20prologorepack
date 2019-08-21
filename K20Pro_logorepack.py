import io

offset0 = 0x4000
offset1 = 0x5000
offset2 = 0x74000
offset3 = 0xD2F000
offset4 = 0x146A000

outpt = open("logo_k20pro.img", "wb")

emptyContent =  [0 for i in range(0x17c1000)]

mi9offset = [0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
                0x3B, 0x07, 0x00, 0x00, 0x40, 0x07, 0x00, 0x00, 0xEF, 0x05, 0x00, 0x00,
                0x2F, 0x0D, 0x00, 0x00, 0x3B, 0x07, 0x00, 0x00, 0x6A, 0x14, 0x00, 0x00,
                0xEf, 0x05]


outpt.write(bytearray(emptyContent))

outpt.seek(offset0)
outpt.write(bytearray(mi9offset))

outpt.seek(offset1)
img = open("locked.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset2)
img = open("fastboot.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset3)
img = open("unlocked.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset4)
img = open("error.bmp", "rb")
outpt.write(img.read())

outpt.close()
