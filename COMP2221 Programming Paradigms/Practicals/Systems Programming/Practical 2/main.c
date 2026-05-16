#include <stdio.h>
#include "reader.h"

int main(int argc, char **argv) {
	const char *token = (argc > 1) ? argv[1] : "OK";
	char buf[256];
	int count = 0;
	while (fgets(buf, sizeof buf, stdin)) {
		if (contains_token(buf, token)) count++;
	}
	printf("Lines containing '%s': %d\n", token, count);
	return 0;
}

