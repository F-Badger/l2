CC = gcc
CFLAGS = -I$(INCDIR)
SRCDIR = src
INCDIR = include
OBJDIR = obj
BINDIR = bin

.PHONY: all debug clean run-status run-config run-tester help

all: $(BINDIR)/status $(BINDIR)/config $(BINDIR)/tester $(OBJDIR)/status.o $(OBJDIR)/config.o $(OBJDIR)/tester.o $(OBJDIR)/common.o

$(OBJDIR)/%.o: $(SRCDIR)/%.c $(INCDIR)/common.h
	$(CC) $(CFLAGS) $< -c -o $@

$(BINDIR)/%: $(OBJDIR)/%.o $(OBJDIR)/common.o
	$(CC) $(CFLAGS) $^ -o $@

debug: CFLAGS += -g -o0
debug: clean all

clean:
	rm -f $(OBJDIR)/* $(BINDIR)/*

run-status: $(BINDIR)/status
	./$(BINDIR)/status

run-config: $(BINDIR)/config
	./$(BINDIR)/config

run-tester: $(BINDIR)/tester
	./$(BINDIR)/tester

help:
	echo "Help Manual"
