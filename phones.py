import matplotlib.pyplot as plt
filename = "Phones - Form Responses 1.csv"

with open(filename) as file:
    raw = file.read()

rows = [i for i in raw.split('\n') if len(i) > 0]
data = [i.split(',') for i in rows]

girlfront = guyfront = girlback = guyback = girlother = guyother = 0

for datum in data:
    if datum[-1] == "Mens":
        if datum[-2] == "Back pocket":
            guyback += 1
        elif datum[-2] == "Front pocket":
            guyfront += 1
        elif datum[-2] == "Other pocket":
            guyother += 1
    elif datum[-1] == "Womens":
        if datum[-2] == "Back pocket":
            girlback += 1
        elif datum[-2] == "Front pocket":
            girlfront += 1
        elif datum[-2] == "Other pocket":
            girlother += 1

plt.pie([girlfront, girlback, girlother], labels=["Front", "Back", "Other"], startangle=90, autopct='%1.2f%%')
plt.title("Women's pants")
plt.savefig("Womens.png")
plt.clf()

plt.pie([guyfront, guyback, guyother], labels=["Front", "Back", "Other"], startangle=90, autopct='%1.2f%%')
plt.title("Men's pants")
plt.savefig("Mens.png")
plt.clf()

right = [0,0,0,0]
left = [0,0,0,0]
key = ["Pants pocket", "Coat/Jacket pocket", "Purse/Handbag", "Other"]

for datum in data:
    try:
        place = key.index(datum[1])
    except ValueError:
        place = 3
    if datum[2] == "Left":
        left[place] += 1
    elif datum[2] == "Right":
        right[place] += 1

for l, r, title in zip(left, right, key):
    plt.pie([l,r], labels=["Left","Right"], startangle=90, colors=["green","red"], autopct='%1.2f%%')
    plt.title(title)
    plt.savefig(title.split('/')[0] +".png")
    plt.clf()

if __name__ == "__main__":
    print("Finished")