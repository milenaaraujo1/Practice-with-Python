from time import sleep

def maior(* num):
  tam = len(num)
  maximo = max(num)
  print(f'Analisando os valores passados....')
  for c in num:
    print(f'{c}', end=' ', flush=True)
    sleep(0.5)
  print(f'\nTemos {tam} valores e o maior é {maximo}')
  print('-=' * 25)



maior(2, 3, 5, 6)
maior(3, 6, 8)
maior(10, 5, 6, 9, 11, 1)
maior(5, 25, 21, 10)