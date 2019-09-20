
from temp_final import MAX31865
import RPi.GPIO as IO
def temperature_read():

    cs_pins = [24]
    clock_pin = 23
    data_in_pin = 21
    data_out_pin = 19
    #units = "k"

    # Configure RTDs
    rtds = []
    address = int(0x80)    # RTD control register, see datasheet for details
    data =  int(0xC2)      # RTD control register data, see datasheet for details
    for cs_pin in cs_pins:
        rtds.append(MAX31865(cs_pin, clock_pin, data_in_pin, data_out_pin, address, data))  
    for rtd in rtds:        
        rtd.write()

    # Run main program    
    running = True
    while(running):
        try:
            for rtd in rtds:
                code = rtd.get_data()
                tempC = rtd.convert(code)
                return tempC                
            #time.sleep(1)
        except KeyboardInterrupt:
            running = False


