int SCAN_ENTER = 0x5a; int SCAN_BREAK = 0xf0;
int breakActive = 0;
int clockPin = 3; // Clock is only output. 
int dataPin = 2; // The data pin is bi-directional
				// But at the moment we are only interested in receiving   
int ledPin = 13;  // When a SCAN_ENTER scancode is received the LED blink
int clockValue = 0; byte dataValue;
byte scanCodes[10] = {0x45,0x16,0x1e,0x26,0x25,0x2e,0x36,0x3d,0x3e,0x46}; char characters[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
int quantityCodes = 10;
char buffer[64] = {};	// This saves the characters (for now only numbers) 
int bufferPos = 0; 
int bufferLength = 64;


void setup() {
	pinMode(dataPin, INPUT);                                               
	pinMode(clockPin, INPUT);                                              
	pinMode(ledPin, OUTPUT);                                               
	Serial.begin(9600);                                                    
}

void loop() {
	dataValue = dataRead();                                                
	// If there is a break code, skip the next byte                        
	if (dataValue == SCAN_BREAK) {                                         
		breakActive = 1;                                                     
	}                                                                      
	// Translate the scan codes to numbers                                 
	// If there is a match, store it to the buffer                         
	for (int i = 0; i < quantityCodes; i++) {      	                       
		byte temp = scanCodes[i];                                            
		if(temp == dataValue){                                               
			if(!breakActive == 1){                                             
				buffer[bufferPos] = characters[i];                               
				bufferPos++;                                                     
			}                                                                  
		}                                                                    
	}                                                                      
	//Serial.print('*'); // Output an asterix for every byte               
	// Print the buffer if SCAN_ENTER is pressed.                          
	if(dataValue == SCAN_ENTER){                                           
		//Serial.print("\nbuffer: ");                                          
		// Read the buffer                                                   
		int i=0;																		                         
		if (buffer[i] != 0) {                                                
			while(buffer[i] != 0) {                                            
				Serial.print( buffer[i] );                                       
				buffer[i] = 0;                                                   
				i++;                                                             
			}                                                                  
		}                                                                    
		Serial.print("\n");                                          
		bufferPos = 0;                                                       
		// Blink the LED	                                                   
		digitalWrite(ledPin, HIGH);                                          
		delay(300);                                                          
		digitalWrite(ledPin, LOW);                                           
	}                                                                      
	// Reset the SCAN_BREAK state if the byte was a normal one             
	if(dataValue != SCAN_BREAK){                                           
		breakActive = 0;                                                     
	}                                                                      
	dataValue = 0;                                                         
}

int dataRead() {
	byte val = 0;                                                          
	// Skip start state and start bit                                      
	while (digitalRead(clockPin));  // Wait for LOW.                       
	// clock is high when idle                                             
	while (!digitalRead(clockPin)); // Wait for HIGH.                      
	while (digitalRead(clockPin));  // Wait for LOW.                       
	for (int offset = 0; offset < 8; offset++) {                           
		while (digitalRead(clockPin));         // Wait for LOW               
		val |= digitalRead(dataPin) << offset; // Add to byte                
		while (!digitalRead(clockPin));        // Wait for HIGH              
	}                                                                      
// Skipping parity and stop bits down here.                            
	while (digitalRead(clockPin));           // Wait for LOW.              
	while (!digitalRead(clockPin));          // Wait for HIGH.             
	while (digitalRead(clockPin));           // Wait for LOW.              
	while (!digitalRead(clockPin));          // Wait for HIGH.             
	return val;                                                            
}
