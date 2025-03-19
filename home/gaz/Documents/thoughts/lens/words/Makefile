all: factor.bin

clean:
	rm *.o *.bin factor

factor.bin: factor.asm
	nasm -f bin -o factor.bin factor.asm

factor: factor.asm
	nasm -f elf32 factor.asm -o factor.o
	ld -m elf_i386 factor.o -o factor

