import math

def main():
    cans = [[6.83,10.16, "#1 Picnic"],[7.78,11.91, "#1Tall"],[8.73,11.59, "#2"],[10.32,11.91, "#2.5"],[10.79,17.78, "#3 Cylinder"],[13.02,14.29,"#5"],[5.40,8.89,"#6Z"],[6.83,7.62,"#8Z Short"],[15.72,17.78,"#10"],[6.83,12.38,"#211"],[7.62,11.27,"#300"],[8.10,11.11,"#303"]]
    
    for can in cans:
        radius = can[0]
        height = can[1]
        name = can[2]
        
        volume = cylinder_volume(radius, height)
        surface_area = cylinder_surface_area(radius,height)
        storage_efficiency = cylinder_storage_efficiency(volume,surface_area)
    
        print(f'{name} {storage_efficiency:.1f}')

def cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume
            
def cylinder_surface_area(radius,height):
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2 
    return surface_area

def cylinder_storage_efficiency(volume,surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency


          
main()