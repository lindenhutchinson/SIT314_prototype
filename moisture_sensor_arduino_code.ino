
#define sensorPower 7
#define sensorPin A0
#define sixHoursInMilliseconds 21600000

void setup()
{
	pinMode(sensorPower, OUTPUT);

	// Initially keep the sensor OFF
	digitalWrite(sensorPower, LOW);
	Serial.begin(9600);
}

void loop()
{
	// only check the sensor every 6 hours
	if (millis() % sixHoursInMilliseconds == 0)
	{
		// output the probe resistance to serial console
		Serial.println(readSensor());
	}
}

int readSensor()
{
	digitalWrite(sensorPower, HIGH); // Turn the sensor ON
	delay(10);						 // Allow power to settle
	int val = analogRead(sensorPin); // Read the analog value form sensor
	digitalWrite(sensorPower, LOW);	 // Turn the sensor OFF
	return val;						 // Return analog moisture value
}