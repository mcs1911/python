def maior(* n):
    mai = 0
    for i in range(0, len(n)):
        if n[i] == 0:
            mai = n[i]
        else:
            if n[i] > mai:
                mai = n[i]
    print(f'{n} O maior número encontrado na sequência de {len(n)} números é {mai}')

maior(4, 6, 6, 8, 3)
maior(9, 33, 2)
maior()    
maior(6)
maior(1, 2)     