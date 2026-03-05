<<<<<<< HEAD
import matplotlib.pyplot as plt

f = open("groupchat.txt", "r", encoding="utf-8")
z = f.read()
f.close()

number = {}

for i in z.splitlines():
    if ":" in i:
        name = i.split(":", 1)[0]

        if name in number:
            number[name] += 1
        else:
            number[name] = 1

print(number)

names = list(number.keys())
counts = list(number.values())

plt.bar(names, counts)
plt.xlabel("Person")
plt.ylabel("Number of Messages")
plt.title("WhatsApp Chat Analysis")
plt.show()
=======
import matplotlib.pyplot as plt

f = open("groupchat.txt", "r", encoding="utf-8")
z = f.read()
f.close()

number = {}

for i in z.splitlines():
    if ":" in i:
        name = i.split(":", 1)[0].strip()

        if name in number:
            number[name] += 1
        else:
            number[name] = 1

print(number)

names = list(number.keys())
counts = list(number.values())

plt.bar(names, counts)
plt.xlabel("Person")
plt.ylabel("Number of Messages")
plt.title("WhatsApp Chat Analysis")
plt.show()
>>>>>>> 3dffd07cfde143da69f20387972a923981707b44
