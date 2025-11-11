CC=gcc
CFLAGS=-I.

all: main.c helper.o
	$(CC) -o  program  main.c helper.o $(C_FLAGS)

helper.o:
	$(CC) -c helper.c helper.h $(CFLAGS)

clean:
	rm *.o program
