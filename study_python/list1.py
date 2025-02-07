# 列表 list 1


bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # trek
print(bicycles[3].title())  # Specialized
print(bicycles[-1])  # specialized
print(bicycles[-4])  # trek
message2 = (
    "My first bicycle was a " + bicycles[0].title() + "."
)  # My first bicycle was a Trek.
print(message2)  # ['honda', 'yamaha', 'suzuki']

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles[0] = "ducati"
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
motorcycles.append("ducati2")
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'ducati2']
motorcycles.insert(0, "ducati3")
print(motorcycles)  # ['ducati3', 'ducati', 'yamaha', 'suzuki', 'ducati2']
del motorcycles[0]
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'ducati2']

popped_motorcycle = motorcycles.pop()
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
print(popped_motorcycle)  # ducati2

first_owned = motorcycles.pop(0)
print(
    "the first motocycle I owned was a " + first_owned.title() + "."
)  # the first motocycle I owned was a Ducati.
print(motorcycles)  # ['yamaha', 'suzuki']

motorcycles.remove("yamaha")
print(motorcycles)  # ['suzuki']

too_expensive = "suzuki"
motorcycles.remove(too_expensive)
print(
    "\nA " + too_expensive.title() + " is too expensive for me."
)  # A Suzuki is too expensive for me.
print(motorcycles)  # []
