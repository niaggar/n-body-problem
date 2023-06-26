
def save_data_to_csv(name, data):
    with open(f"{name}.csv", "w") as file:
        file.write("x,y\n")
        for d in data:
            file.write(f"{d['x']},{d['y']}\n")
    
    print(f"Data saved to {name}.csv")