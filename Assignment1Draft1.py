#Input
length = float(input("Enter the length of the barge in meters: "))
breadth = float(input("Enter the breadth of the barge in meters: "))
height = float(input("Enter the height of the barge in meters: "))

#Process
surfaceArea = 2*(length*height)+2*(breadth*height)+(length*breadth)
mass = surfaceArea * 1.06
draft = mass / (length*breadth)

#Output
print("\n--- Barge Calculation Results ---")
print(f"Length: {length} meters")
print(f"Breadth: {breadth} meters")
print(f"Height: {height} meters")

print(f"\nSurface Area: {surfaceArea:.2f} square meters")
print(f"Mass: {mass:.2f} kg")
print(f"Draft: {draft:.2f} meters")