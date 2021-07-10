class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s], 占地:%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return "户型: %s\n总面积: %.2f平米 [剩余: %.2f]\n家具:%s" \
               % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        print("要添加 %s" % item)


bed = HouseItem("舒服的席梦思", 4)
print(bed)

my_home = House("3室2厅",120)
print(my_home)