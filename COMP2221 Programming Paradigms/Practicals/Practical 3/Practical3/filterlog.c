#include <stdio.h>
#include <string.h>

int main (int argc, char **argv) {
	if (argc < 3) {
		printf("Usage: %s <keyword> <outputfile> [file]", argv[0]);
		return 1;
	}
	char *keyword = argv[1];
	char *outfile = argv[2];

	FILE *out = fopen(outfile, "w");

	FILE *input = stdin;

	if (argc == 4) {
		char *infile = argv[3];
		input = fopen(infile, "r");
	}

    	char line[1024];

    	while (fgets(line, sizeof(line), input)) {
        	if (strstr(line, keyword)) {
            		fputs(line, out);
        	}
    	}

    	fclose(out);

	if (input != stdin) {
	fclose(input);
}
	return 0;
}
