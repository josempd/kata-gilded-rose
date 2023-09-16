from typing import List

SELL_IN_RATE_CHANGE = 0
SELL_IN_CONCERT_HIGH_THRESHOLD = 11
SELL_IN_CONCERT_LOW_THRESHOLD = 6
MIN_QUALITY = 0
MAX_QUALITY = 50
LEGENDARY_QUALITY = 80

class UpdateSellIn:
    @staticmethod
    def update(sell_in):
        return sell_in - 1

class DecreaseQuality:
    @staticmethod
    def decrease(quality):
        return max(quality - 1, 0)

    @staticmethod
    def decrease_by_two(quality):
        return max(quality - 2, 0)

    @staticmethod
    def decrease_by_four(quality):
        return max(quality - 4, 0)

class IncreaseQuality:
    @staticmethod
    def increase(quality):
        return min(quality + 1, MAX_QUALITY)

    @staticmethod
    def increase_by_two(quality):
        return min(quality + 2, MAX_QUALITY)

    @staticmethod
    def increase_by_three(quality):
        return min(quality + 3, MAX_QUALITY)

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
        self.sell_in = UpdateSellIn.update(self.sell_in)
        if self.sell_in < SELL_IN_RATE_CHANGE:
            self.quality = DecreaseQuality.decrease_by_two(self.quality)
        else:
            self.quality = DecreaseQuality.decrease(self.quality)

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = UpdateSellIn.update(self.sell_in)
        if self.sell_in < SELL_IN_RATE_CHANGE:
            self.quality = DecreaseQuality.decrease_by_four(self.quality)
        else:
            self.quality = DecreaseQuality.decrease_by_two(self.quality)
    
class LegendaryItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
       self.quality = LEGENDARY_QUALITY
    
class AgedItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = UpdateSellIn.update(self.sell_in)
        self.quality = IncreaseQuality.increase(self.quality)
        if self.sell_in < SELL_IN_RATE_CHANGE:
            self.quality = IncreaseQuality.increase(self.quality)
    
class ConcertItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in = UpdateSellIn.update(self.sell_in)
        self.quality = IncreaseQuality.increase(self.quality)
        if self.sell_in < SELL_IN_CONCERT_HIGH_THRESHOLD and self.sell_in >= SELL_IN_CONCERT_LOW_THRESHOLD:
            self.quality = IncreaseQuality.increase(self.quality)
        if self.sell_in < SELL_IN_CONCERT_LOW_THRESHOLD:
            self.quality = IncreaseQuality.increase_by_two(self.quality)
        if self.sell_in < SELL_IN_RATE_CHANGE:
            self.quality = MIN_QUALITY