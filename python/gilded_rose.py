from typing import List

class GildedRose(object):

    def __init__(self, items: List["Item"]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            classified_item = self._item_classification(item)
            classified_item.update()
            item.sell_in = classified_item.sell_in
            item.quality = classified_item.quality
                    
    def _item_classification(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return LegendaryItem(item.name, item.sell_in, item.quality)
        elif "Conjured" in item.name:
            return ConjuredItem(item.name, item.sell_in, item.quality)
        elif "Aged" in item.name:
            return AgedItem(item.name, item.sell_in, item.quality)
        elif "concert" in item.name:
            return ConcertItem(item.name, item.sell_in, item.quality)
        else:
            return GenericItem(item.name, item.sell_in, item.quality) 

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
class GenericItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality -1
            self.quality = self.quality -1
        else:
            self.quality = self.quality - 1
        if self.quality < 0:
            self.quality = 0

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality -1
            self.quality = self.quality -1
            self.quality = self.quality -1
            self.quality = self.quality -1    
        else:
            self.quality = self.quality - 1
            self.quality = self.quality - 1
        if self.quality < 0:
            self.quality = 0
    
class LegendaryItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
       self.quality = 80
    
class AgedItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in - 1
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 0:
                self.quality = self.quality + 1
    
class ConcertItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = self.sell_in - 1
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                self.quality = self.quality + 1
            if self.sell_in < 6:
                self.quality = self.quality + 1
            if self.sell_in < 0:
                self.quality = 0