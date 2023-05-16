# Oksuzova T. io-z21
nzk = 2108
c11 = nzk % 11  # 7 => Define a class of sports equipment that consists of at least 5 fields.

class SportsEquipment:
    def __init__(self, name: str, price: float, count: int, country: str, color: str):
        self.price = price
        self.count = count
        self.country = country
        self.color = color
        self.name = name

    def __repr__(self):
        return f"name: {self.name}\nprice: {self.price}\ncount: {self.count}\ncountry: {self.country}\ncolor: {self.color}"

class Catalog:
    def __init__(self):
        self.items = []
        self.prices = []
        self.counts = []
        self.countries = []
        self.colors = []
        self.names = []

    def set_items(self, *args):
        for i in args:
            self.items.append(i)
        return self.items

    def price_mass(self):
        for i in self.items:
            self.prices.append(i.price)
        return self.prices

    def counts_mass(self):
        for i in self.items:
            self.counts.append(i.count)
        return self.counts

    def countries_mass(self):
        for i in self.items:
            self.countries.append(i.country)
        return self.countries

    def colors_mass(self):
        for i in self.items:
            self.colors.append(i.color)
        return self.colors

    def names_mass(self):
        for i in self.items:
            self.names.append(i.name)
        return self.names

class Sort:
    def __init__(self):
        self.ascending_sort = []
        self.descending_sort = []

    def ascending(self, mass: list):
        mass.sort()
        return mass

    def descending(self, mass: list):
        mass.sort(reverse=True)
        return mass

def main():
    # creating items
    item1 = SportsEquipment("skipping rope", 10, 20, "China", "white")
    item2 = SportsEquipment("massage roller", 25, 20, "Ukraine", "black")
    item3 = SportsEquipment("hoop", 20, 20, "USA", "red")
    item4 = SportsEquipment("yoga mat", 30, 20, "Poland", "grey")
    item5 = SportsEquipment("ball", 15, 20, "Ukraine", "blue")
    catalog = Catalog()
    sort = Sort()

    # creating massive of items
    catalog.set_items(item1, item2, item3, item4, item5)

    names = catalog.names_mass()
    prices = catalog.price_mass()

    print(f"Massive of names: {names}")
    print(f"Ascending sort by names: {sort.ascending(names)}")

    print(f"Massive of prices: {prices}")
    print(f"Descending sort of prices: {sort.descending(prices)}")

if __name__ == '__main__':
    main()

