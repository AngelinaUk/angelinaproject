# Makefile for System Information Utility
# Author: Angelina Botez
# License: GNU General Public License v3.0

CC = gcc
CFLAGS = -Wall -Wextra -O2
TARGET = sysinfo
SOURCE = sysinfo.c

.PHONY: all clean install uninstall

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)

clean:
	rm -f $(TARGET)

install: $(TARGET)
	install -m 0755 $(TARGET) /usr/local/bin/

uninstall:
	rm -f /usr/local/bin/$(TARGET)

help:
	@echo "Available targets:"
	@echo "  make          - Build the sysinfo program"
	@echo "  make clean    - Remove compiled binary"
	@echo "  make install  - Install to /usr/local/bin (requires sudo)"
	@echo "  make uninstall- Remove from /usr/local/bin (requires sudo)"
	@echo "  make help     - Show this help message"
