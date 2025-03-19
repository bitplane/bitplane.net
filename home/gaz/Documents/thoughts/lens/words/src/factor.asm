section .text
global _start

_start:
    mov eax, 1984      ; Factor this number
    mov ebx, 2         ; Start divisor

factor_loop:
    test eax, 1        ; Check if even
    jnz next_factor    ; If odd, move on
    shr eax, 1         ; Divide by 2 (right shift)
    push eax           ; Store quotient
    call print_num     ; Print "2"
    pop eax
    jmp factor_loop

next_factor:
    inc ebx            ; Try next odd divisor
    cmp ebx, eax       ; If divisor > number, done
    jg done

    mov edx, 0         ; Clear remainder
    div ebx            ; Divide eax by ebx
    test edx, edx      ; If remainder != 0, try next
    jnz next_factor

    push eax
    call print_num     ; Print found prime factor
    pop eax
    jmp factor_loop

done:
    mov eax, 1         ; Exit syscall
    int 0x80

print_num:
    ; Minimal routine to print number (could be optimized further)
    ret
