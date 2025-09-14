from classes import Item, RefrigeratedContainer, HazardousMaterialContainer, CargoHold

# Create items
apple = Item("Apple Box", 10, 0.5, 0.3, 0.2, category="perishable", value=100)
battery = Item("Lithium Battery", 15, 0.4, 0.4, 0.3, category="hazardous", value=500)

# Create containers
refrigerated = RefrigeratedContainer("Refrigerated-01", 100, 10, min_temp=5)
hazardous = HazardousMaterialContainer("Hazardous-01", 200, 15, hazard_classes=["hazardous"])

# Add items
refrigerated.add_item(apple)
hazardous.add_item(battery)

# Create cargo hold
cargo = CargoHold("Main CargoHold", 1000, 100)
cargo.add_item(refrigerated)
cargo.add_item(hazardous)

# Print reports
print(apple)
print(battery)
print(refrigerated)
print(hazardous)
print(cargo)
print(cargo.get_efficiency_report())
