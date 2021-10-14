#
# class House:
#     doors: int
#     color: str
#
#     def __init__(self, doors: int, color: str) -> None:
#         self.doors = doors
#         self.color = color
#
#     def change_color(self, new_color: str) -> None:
#         if new_color == self.color:
#             print("Nowy kolor nie może być taki sam jak obecny")
#             return
#         self.color = new_color
#
#     def __str__(self) -> str:
#         return f"Ilosc drzwi: {self.doors}, kolor elewacji: {self.color}"
#
#     def __len__(self) -> int:
#         return 20
#
# green_house: House = House(doors=30, color="green")
# print(green_house.doors)
# print(green_house.color)
# print(green_house)
#
# blue_house: House = House(doors=10, color="blue")
# print(blue_house)
# print(len(blue_house))
