import os

try:
    os.mkdir('input')
    os.mkdir('output')

except:
    pass

try:
    for msm in os.listdir("input/"):

        running = True

        print('fixing '+msm)
        with open("input/"+msm,'rb') as f:

            msmake = open("output/"+msm,'wb')

            one = f.read(4)
            onebckw = one[::-1]
            two = f.read(4)
            twobckw = two[::-1]

            msmake.write(onebckw)
            msmake.write(twobckw)

            msmake.write(f.read(192))

            intropart = f.read(4)
            introbckw = intropart[::-1]

            brokenpart = f.read(24)
            fixenpart = b'\xCD\xCC\x8C\x3F\x00\x00\x60\x40\x66\x66\xA6\x3F\xCD\xCC\xCC\x3D\x00\x00\x00\x00\x00\x00\x1C\x21'

            msmake.write(introbckw)
            msmake.write(fixenpart)

            while running==True:
                msmcontent = f.read(4)
                if msmcontent == b'':
                    break

                backwardsmsm = msmcontent[::-1]

                msmake.write(backwardsmsm)

except FileNotFoundError:
    input('You need msms, dummy!!!!! ')