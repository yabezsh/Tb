#!/usr/bin/env python

#N_4_mini1.  415-478
with open("MambaMasks_N_4_mini1.dat","w") as f:
    for i in range(415):
        f.write("0\n")
    for i in range(64):
        f.write("1\n")
    for i in range(33):
        f.write("0\n")

#N_4_mini6.  161-224
with open("MambaMasks_N_4_mini6.dat","w") as f:
    for i in range(161):
        f.write("0\n")
    for i in range(64):
        f.write("1\n")
    for i in range(287):
        f.write("0\n")

#N_3_mini1. 423 - 486.  453, 467 bad
with open("MambaMasks_N_3_mini1.dat","w") as f:
    for i in range(423):
        f.write("0\n")
    for i in range(453 - 423):
        f.write("1\n")
    f.write("0\n")
    for i in range( 467 - 454 ):
        f.write("1\n")
    f.write("0\n")
    for i in range(486 - 468):
        f.write("1\n")
    for i in range(512 - 486):
        f.write("0\n")

#N_3_mini6. 167-230
with open("MambaMasks_N_3_mini6.dat","w") as f:
    for i in range(167):
        f.write("0\n")
    for i in range(64):
        f.write("1\n")
    for i in range(512 - 167 - 64):
        f.write("0\n")


#N_6_mini1. 437-500.  498,500 bad
with open("MambaMasks_N_6_mini1.dat", "w") as f:
    for i in range(437):
        f.write("0\n")
    for i in range(61):
        f.write("1\n")
    f.write("0\n")
    f.write("1\n")
    f.write("0\n")
    for i in range(11):
        f.write("0\n")

#N_6_mini6. 180-243
with open("MambaMasks_N_6_mini6.dat","w") as f:
    for i in range(180):
        f.write("0\n")
    for i in range(64):
        f.write("1\n")
    for i in range(512-180-64):
        f.write("0\n")

#N_9.  	128 - 255: 221, 255 bad
#	384 - 466: 415, 419, 423, 427, 435 bad

with open("MambaMasks_N_9.dat","w") as f:
    for i in range(128):
        f.write("0\n")
    for i in range(221-128):
        f.write("1\n")
    f.write("0\n")
    for i in range(255-222):
        f.write("1\n")
    for i in range(384 - 255):
        f.write("0\n")
    for i in range(384,467):
        if i==415 or i==419 or i==423 or i==435:
            f.write("0\n")
        else:
            f.write("1\n")
    for i in range(467,512):
        f.write("0\n")

#N_8. 137 - 255: 230, 232 bad
#	384 - 469: 386, 394, 398, 406, 410 bad
with open("MambaMasks_N_8.dat","w") as f:
    for i in range(137):
        f.write("0\n")
    for i in range(137,256):
        if i==230 or i==232:
            f.write("0\n")
        else:
            f.write("1\n")
    for i in range(256,384):
        f.write("0\n")
    for i in range(384,470):
        if i==386 or i==394 or i==398 or i==406 or i==410:
            f.write("0\n")
        else:
            f.write("1\n")
    for i in range(470,512):
        f.write("0\n")

#N_7_mini2.  384-447: 417, 418, 419 bad
with open("MambaMasks_N_7_mini2.dat","w") as f:
    for i in range(384):
        f.write("0\n")
    for i in range(384, 448):
        if i==417 or i==418 or i==419:
            f.write("0\n")
        else:
            f.write("1\n")
    for i in range(448,512):
        f.write("0\n")

#N_4_mini7 -- 130-193
with open("MambaMasks_N_4_mini7.dat","w") as f:
    for i in range(130):
        f.write("0\n")
    for i in range(130,194):
        f.write("1\n")
    for i in range(194,512):
        f.write("0\n")


#N_6_mini7 -- 137-200. 159, 182 bad
with open("MambaMasks_N_6_mini7.dat","w") as f:
    for i in range(137):
        f.write("0\n")
    for i in range(137,201):
        if i==159 or i==182:
            f.write("0\n")
        else:
            f.write("1\n")
    for i in range(201,512):
        f.write("0\n")

#N_6_mini2 -- 390-453. 430, 434, 437 bad
with open("MambaMasks_N_6_mini2.dat","w") as f:
    for i in range(390):
        f.write("0\n")
    for i in range(390,454):
        if i==430 or i==434 or i==437:
            f.write("0\n")
        else:
            f.write("1\n")
    for i in range(454,512):
        f.write("0\n")

#N_3_mini7 -- 128-191, 132-191 good
with open("MambaMasks_N_3_mini7.dat","w") as f:
    for i in range(132):
        f.write("0\n")
    for i in range(132,192):
        f.write("1\n")
    for i in range(192,512):
        f.write("0\n")