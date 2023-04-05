from teapot_manager import TeapotManager

teapot = TeapotManager()

print(teapot)

print("-------------------")

teapot.pour_water()
print(teapot)

print("-------------------")

teapot.make_coffee()

print("-------------------")

teapot.turn_on()
print(teapot)
teapot.ten_min_later()
print(teapot)

print("-------------------")

teapot.make_coffee()

print("-------------------")

print(teapot)

print("-------------------")

teapot.turn_on()
