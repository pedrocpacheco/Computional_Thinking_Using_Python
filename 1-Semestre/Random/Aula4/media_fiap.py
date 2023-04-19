def media_chekpoint(cp1, cp2, cp3):
  if(cp1 < cp2 and cp1 < cp3):
    media = (cp2 + cp3) / 2
  elif(cp2 < cp1 and cp2 < cp3):
    media = (cp1 + cp3) / 2
  else:
    media = (cp1 + cp2) / 2
  return media

def media_total(nota_cp, nota_gl, nota_ch):
  media = (int(nota_cp) * 0.2) + (int(nota_gl) * 0.3) + (int(nota_ch) *  0.5)
  return media

cp1 = int(input("Qual a sua nota no Chekpoint 1? "))
cp2 = int(input("Qual a sua nota no Chekpoint 2? "))
cp3 = int(input("Qual a sua nota no Chekpoint 3? "))

nota_gl = int(input("Qual a sua nota no Global Solution? "))
nota_ch = int(input("Qual a sua nota no Challenge? "))

print(media_total(media_chekpoint(cp1, cp2, cp3), nota_gl, nota_ch))
