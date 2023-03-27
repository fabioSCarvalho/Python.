# um programa que receba um valor em metro e exiba convertido em centimetros e milimetros
medida = float(input('Digite uma distacia em metros: : '))

centimetros = medida * 100
milimetros = medida * 1000
hm = medida / 100
dam = medida / 1000
km = medida / 1000000

print('{:.2f} metros concertido em Km é {:.6f}'.format(medida, km))
print('{:.2f} metros convertido em hm é {:.4f}'.format(medida, hm))
print('{:.2f} metros convertido em dam é {:.3f}'.format(medida, dam))
print('{:.2f} metros convertido em centimetros é {:.02f}'.format(medida, centimetros))
print('{:.2f} metros convertido em milimetros é {:.02f}'.format(medida, milimetros))