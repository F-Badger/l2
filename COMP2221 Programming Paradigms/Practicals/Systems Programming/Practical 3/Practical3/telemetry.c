#include <stdio.h>

struct Telemetry {
	float temperature;
	int battery;
	int GPSlockstate;
};

union FloatBytes {
	unsigned char bytes[4];
	float f;
};

int main() {
	struct Telemetry a = {16.4, 55, 0};

	printf("Telemetry packet:\nTemperature: %.2f\nBattery: %d\nGPS lock state: %d\n\n", a.temperature, a.battery, a.GPSlockstate);

	union FloatBytes b;
	b.f = 16.4;

	printf("Float value in b: %.2f\n", b.f);

	union FloatBytes c;

	for (int i = 0; i < 4; i++) {
		c.bytes[i] = b.bytes[i];
	}

	printf("Float value in c from copying bytes from b: %.2f\n", c.f);

	return 0;
}
