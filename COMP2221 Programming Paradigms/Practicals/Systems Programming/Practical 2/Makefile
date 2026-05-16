CC = gcc

# Final program name
TARGET = program

all: $(TARGET)

$(TARGET): main.o reader.o
	$(CC) $^ -o $@

reader.o: reader.c reader.h
	$(CC) -c $<

main.o: main.c reader.h
	$(CC) -c $<

clean:
	rm -f *.o $(TARGET)


