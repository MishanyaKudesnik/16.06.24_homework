a = input()
b = []
for word in a:
  b.append(word)
count_gl = 0
count_sogl = 0
for i in range(0, len(b)):
  if ( b[i] == 'а' or b[i] == 'е' or b[i] == 'ё' or b[i] == 'и' or b[i] == 'о' or b[i] == 'у' or b[i] == 'ы' or b[i] == 'э' or b[i] == 'ю' or b[i] == 'я' or b[i] == 'А' or b[i] == 'Е' or b[i] == 'Ё' or b[i] == 'И' or b[i] == 'О' or b[i] == 'У' or b[i] == 'Ы' or b[i] == 'Э' or b[i] == 'Ю' or b[i] == 'Я'):
    count_gl += 1
  else:
    count_sogl += 1
print('Гласных: ', count_gl, ' Согласных: ',  count_sogl)
  
