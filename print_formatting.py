def celsius_to_fahrenheit(degree):
    return degree*1.8 + 32

cels = range(-20,44,5)
fahrs = [celsius_to_fahrenheit(cel) for cel in cels]

for i,_ in enumerate(cels):
    cel = cels[i]
    fahr = round(fahrs[i])
    print(f'Temperatura {cel:=+7d}C to {fahr:_^+10d}F')

