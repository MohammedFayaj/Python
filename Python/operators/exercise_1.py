distance = input('How far you want to travel?')
# Convert the distance to an integer.
travel_distance = int(distance)
if travel_distance <3:
    mode_of_transport = 'Please Walk'
elif travel_distance >= 3 and travel_distance < 300:
    mode_of_transport = 'Please drive'
else:
    mode_of_transport = 'Please fly'
print('Dude hello {} do as you like'.format(mode_of_transport))
