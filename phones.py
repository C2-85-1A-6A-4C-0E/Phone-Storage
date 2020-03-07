import matplotlib.pyplot as plt
filename = "Phones - Form Responses 1.csv"

with open(filename) as file:
    raw = file.read()

rows = [i for i in raw.split('\n') if len(i) > 0]
data = [i.split(',') for i in rows]

girlfront = guyfront = girlback = guyback = 0

for datum in data:
    if datum[-1] == "Mens":
        if datum[-2] == "Back pocket":
            guyback += 1
        elif datum[-2] == "Front pocket":
            guyfront += 1
    elif datum[-1] == "Womens":
        if datum[-2] == "Back pocket":
            girlback += 1
        elif datum[-2] == "Front pocket":
            girlfront += 1

plt.pie([girlfront, girlback], labels=["Front", "Back"], startangle=90)
plt.title("Women's pants")
plt.savefig("Womens.png")
plt.clf()

plt.pie([guyfront, guyback], labels=["Front", "Back"], startangle=90)
plt.title("Men's pants")
plt.savefig("Mens.png")
plt.clf()

if __name__ == "__main__":
    print("Finished")