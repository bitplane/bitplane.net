words.cast: $(wildcard src/*) build/binary
	asciinema rec words.cast -c './src/script.sh' --overwrite

clean:
	rm build/* words.cast

build/factor.ascii: build/factor
	xxd -b build/factor | cut -d ' ' -f 2-8 | tr -d ' ' | uniq > build/factor.ascii

build/factor.bin: src/factor.asm
	nasm -f bin src/factor.asm -o build/factor.bin

build/factor: src/factor.asm
	nasm -f elf32 src/factor.asm -o build/factor.o
	ld -m elf_i386 build/factor.o -o build/factor

