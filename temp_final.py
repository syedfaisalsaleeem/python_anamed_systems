
import RPi.GPIO as IO
import time

class MAX31865(object):
    
    def __init__(self, cs_pin, clock_pin, data_in_pin, data_out_pin, address, data, units = "c", board = IO.BOARD):

        '''Initialize Soft (Bitbang) SPI bus
        Parameters:
        - cs_pin:    Chip Select (CS) / Slave Select (SS) pin (Any GPIO)  
        - clock_pin: Clock (SCLK / SCK) pin (Any GPIO)
        - data_in_pin:  Data input (SO / MOSI) pin (Any GPIO)
	      - data_out_pin: Data output (MISO) pin (Any GPIO)
        - units:     (optional) unit of measurement to return. ("c" (default) | "k" | "f")
        - board:     (optional) pin numbering method as per RPi.GPIO library (GPIO.BCM (default) | GPIO.BOARD)
        '''

        self.cs_pin = cs_pin
        self.clock_pin = clock_pin
        self.data_in_pin = data_in_pin
        self.data_out_pin = data_out_pin
        self.address = address           # address of the register to write/read
        #self.data = data                # data to write/read
        self.units = units
        self.data = data
        self.board = board

        # Initialize needed GPIO
        IO.setmode(self.board)
        IO.setup(self.cs_pin, IO.OUT)
        IO.setup(self.clock_pin, IO.OUT)
        IO.setup(self.data_in_pin, IO.IN)
        IO.setup(self.data_out_pin, IO.OUT)

        # Pull chip select high to make chip inactive
        IO.output(self.cs_pin, IO.HIGH)
        
    def get_data(self):
        '''Acqures raw RDT data.'''
        self.address = int(0x01)    #RTD MSBs
        MSB = self.read()
        self.address = int(0x02)    #RTD LSBs
        LSB = self.read()
        #print MSB
        #print LSB
        MSB = MSB<<8 
        raw = MSB+LSB
        #print raw
        #fault = raw & 1
        #print fault
        raw = raw>>1
        #print raw      
        #print self
        #self.checkErrors()        
        return raw

    def write(self):
        '''Writes 8 bit of data to the 8 bit address'''
        IO.output(self.cs_pin, IO.LOW)
        IO.output(self.clock_pin, IO.LOW)
	      
        # Write to address 
        for i in range(8):        
            #print address, data
            bit  = self.address>>(7 - i)
            bit = bit & 1 
            #GPIO.output(self.clock_pin, GPIO.LOW)
            IO.output(self.data_out_pin, bit)
            #if bit:
            #    GPIO.output(self.data_out_pin, GPIO.HIGH)
            #else:
            #    GPIO.output(self.data_out_pin, GPIO.LOW)
            IO.output(self.clock_pin, IO.HIGH)            
            IO.output(self.clock_pin, IO.LOW)
                
        for i in range(8):        
            bit  = self.data>>(7 - i)
            bit = bit & 1 
            #GPIO.output(self.clock_pin, GPIO.LOW)
            IO.output(self.data_out_pin, bit)
            #if bit:
            #    GPIO.output(self.data_out_pin, GPIO.HIGH)
            #else:
            #    GPIO.output(self.data_out_pin, GPIO.LOW)
            IO.output(self.clock_pin, IO.HIGH)
            IO.output(self.clock_pin, IO.LOW)
            #GPIO.output(self.data_out_pin, GPIO.LOW)
        
        IO.output(self.clock_pin, IO.HIGH)                      
        # Unselect the chip
        IO.output(self.cs_pin, IO.HIGH)
        

    def read(self):
        '''Reads 16 bits of the SPI bus from a self.address register & stores as an integer in self.data.'''
        bytesin = 0                
        
        # Select the chip
        IO.output(self.cs_pin, IO.LOW)
        # Assert clock bit
        IO.output(self.clock_pin, IO.LOW)
	      
        # Write to address 
        for i in range(8):        
            #print address, data
            bit  = self.address>>(7 - i)
            bit = bit & 1 
            #GPIO.output(self.clock_pin, GPIO.LOW)
            IO.output(self.data_out_pin, bit)
            #if bit:
            #    GPIO.output(self.data_out_pin, GPIO.HIGH)
            #else:
            #    GPIO.output(self.data_out_pin, GPIO.LOW)
            IO.output(self.clock_pin, IO.HIGH)
            IO.output(self.clock_pin, IO.LOW)
            #GPIO.output(self.data_out_pin, GPIO.LOW)
        
        # Read in 8 bits        
        for i in range(8):
            IO.output(self.clock_pin, IO.HIGH)
            bytesin = bytesin << 1
            if (IO.input(self.data_in_pin)):
                bytesin = bytesin | 1
            IO.output(self.clock_pin, IO.LOW)
        
        # Dsable clock                
        IO.output(self.clock_pin, IO.HIGH)
        # Unselect the chip
        IO.output(self.cs_pin, IO.HIGH)
        
        # Save data
        self.data = bytesin
        #print bytesin
        return self.data

    def checkErrors(self, data_32 = None):
    # Not finished yet
        '''Checks error bits to see if there are any SCV, SCG, or OC faults'''
        if data_32 is None:
            data_32 = self.data
        anyErrors = (data_32 & 0x10000) != 0    # Fault bit, D16
        noConnection = (data_32 & 1) != 0       # OC bit, D0
        shortToGround = (data_32 & 2) != 0      # SCG bit, D1
        shortToVCC = (data_32 & 4) != 0         # SCV bit, D2
        if anyErrors:
            if noConnection:
                raise MAX31865Error("No Connection")
            elif shortToGround:
                raise MAX31865Error("Thermocouple short to ground")
            elif shortToVCC:
                raise MAX31865Error("Thermocouple short to VCC")
            else:
                # Perhaps another SPI device is trying to send data?
                # Did you remember to initialize all other SPI devices?
                raise MAX31865Error("Unknown Error")

    def convert(self, raw):
        #Takes raw RTD data and returns RTD temperature in celsius as well as RTD resistance.
        RefR = 431 #RefR/2        
        R0 = raw * RefR / 32768
        #print(R0)
        if R0==0:
            temperature_data = ['']       
        else:         
            t = -247.29 + 2.3992*R0 + 0.00063962*R0*R0 + 1.0241E-6*R0*R0*R0
            temperature_data = [ '{:.1f}'.format(t)]
        #if R0==0:            
        #    return -1,0        
        #print temperature_data
        temperature_data = tuple('-' if x == '' else x for x in temperature_data)
        temperature_data = '\t'.join(temperature_data)                   
        #return raw, R0, t
        return temperature_data
    
    def to_c(self, celsius):
        '''Celsius passthrough for generic to_* method.'''
        return celsius

    def to_k(self, celsius):
        '''Convert celsius to kelvin.'''
        #return celsius + 273.15

    def to_f(self, celsius):
        '''Convert celsius to fahrenheit.'''
        #return celsius * 9.0/5.0 + 32

    def cleanup(self):
        '''Selective GPIO cleanup'''
        IO.setup(self.cs_pin, IO.IN)
        IO.setup(self.clock_pin, IO.IN)

class MAX31865Error(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)




