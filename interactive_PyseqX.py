import pyseq

hs = pyseq.HiSeq()

def interactive():

    module = input("Instrument? \nfpga \nlasers \nobjective \noptics \npump \
                    \nv10 \nv24 \nxstage \nystage \nzstage \ntemperature \ncam1 \ncam2 \n")
    
    classLookup = {'fpga': hs.f, 'ystage': hs.y, 'xstage': hs.x, 'lasers': hs.lasers, \
                   'zstage': hs.z, 'objective': hs.obj, 'optics': hs.optics, 'cam1': hs.cam1, 'cam2': hs.cam2, \
                    'pump': hs.p, 'v10': hs.v10, 'v24': hs.v24, 'temperature': hs.T}

    instrument = classLookup[module]

    initfirst = input('Initialize instrument first? y/n \n')
    if initfirst == 'y':
        instrument.initialize()
   
    while True:
        command = input("Command? \"exit\" to end program \n")
        if command == "exit":
            return
        instrument.command(command)

interactive()
                
                