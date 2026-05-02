from deep_translator import GoogleTranslator

traductor = GoogleTranslator(source='en', target='es')

file = 'c03.rst'
fileo = 'c03N.rst'

filin = open(file, 'r')
filon = open(fileo, 'w')

datos = filin.readlines()

n = len(datos)

i=0
while i < n:
  ss = datos[i]
  ss = ss.replace('\n', '')
  if ss[:2] == '$$':
    i = i+1
    ss1 = ss
    while i < n:
      ss = datos[i]
      ss = ss.replace('\n', '')
      if len(ss) > 0:
        ss1 = ss1 + ss
        i = i+1
      else:
        break
    print(ss1) 
    filon.write(ss1+'\n\n')
    ss2 = ss1[2:]
    texto_espanol = traductor.translate(ss2)
    filon.write(texto_espanol+'\n\n')
    print('\n' + texto_espanol)
    i = i+1
    print(ss)
  i = i+1

filon.close()
