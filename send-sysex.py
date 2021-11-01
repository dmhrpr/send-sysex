import mido
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    Tk().withdraw()
    output = midi_output()
    send_sysex(output)

# Retrieves available midi devices, returns chosen device name
def midi_output():
    try:
        outputs = mido.get_output_names()
        for x in outputs:
            print(f'{outputs.index(x)} {x}')
        select_output = input('Select midi output (#): ')
        return outputs[int(select_output)]
    except:
        print('Midi output cannot be found. Please try again.')
        quit()

# Opens GUI window to choose .syx file, sends file to chosen midi device
def send_sysex(output):
    port = mido.open_output(output)
    y = 0
    while y < 1:
        select_sysex = askopenfilename()
        try:
            if select_sysex.split('.')[1] != 'syx':
                print('Please choose a sysex file (.syx)')
            else:
                y = 1
        except:
            quit()
    sysex = mido.read_syx_file(select_sysex)
    for z in sysex:
        port.send(z)

if __name__ == '__main__':
    main()
