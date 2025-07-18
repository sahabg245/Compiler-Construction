global _main
extern _printf
extern _exit

section .data
    fmt_int db "%d", 10, 0
    fmt_str db "%s", 10, 0
    msg db "Operation result stored", 10, 0
    str1 db "Result is greater than 40", 10, 0

section .bss
    res resb 4

section .text
_main:
    push ebp
    mov ebp, esp
    sub esp, 64

    mov eax, 23
    mov ebx, 54
    mov ecx, 0
    mov eax, eax
    imul eax, 4
    mov edx, eax
    mov ecx, edx
    mov dword dword [ebp-4], 0
    mov dword dword [ebp-8], 0
    mov eax, eax
    add eax, ebx
    mov dword dword [ebp-12], eax
    mov eax, dword [ebp-12]
    mov dword dword [ebp-16], eax
    mov eax, eax
    add eax, ebx
    mov dword dword [ebp-20], eax
    mov eax, dword [ebp-20]
    mov dword dword [ebp-24], eax
    ; unhandled op: <
    cmp dword dword [ebp-28], 0
    je L1
    mov eax, dword dword [ebp-8]
    add eax, dword dword [ebp-16]
    mov dword dword [ebp-32], eax
    mov eax, dword [ebp-32]
    mov dword dword [ebp-8], eax
    mov eax, dword dword [ebp-4]
    add eax, 1
    mov dword dword [ebp-36], eax
    mov eax, dword [ebp-36]
    mov dword dword [ebp-4], eax
    jmp L2
    L1:
    L2:
    mov eax, ecx
    cmp eax, 40
    setg al
    movzx eax, al
    mov dword dword [ebp-40], eax
    cmp dword dword [ebp-40], 0
    je L3
    push str1
    push fmt_str
    call _printf
    add esp, 8
    mov eax, dword dword [ebp-24]
    push eax
    push fmt_int
    call _printf
    add esp, 8
    jmp L4
    L3:
    L4:

    ; Program exit
    push msg
    push fmt_str
    call _printf
    add esp, 8
    mov esp, ebp
    pop ebp
    push 0
    call _exit
