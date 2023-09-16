import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = []
        self.gilded_rose = GildedRose(self.items)

    def test_generic_item(self):
        self.items.append(Item("foo", 0, 0))
        self.gilded_rose.update_quality()
        self.assertEqual("foo", self.items[0].name)
        self.assertEqual(-1, self.items[0].sell_in)
        self.assertEqual(0, self.items[0].quality)

    def test_aged_brie_quality_increase(self):
        self.items.append(Item("Aged Brie", 1, 1))
        self.gilded_rose.update_quality()
        self.assertEqual("Aged Brie", self.items[0].name)
        self.assertEqual(0, self.items[0].sell_in)
        self.assertEqual(2, self.items[0].quality)
        self.gilded_rose.update_quality()
        self.assertEqual("Aged Brie", self.items[0].name)
        self.assertEqual(-1, self.items[0].sell_in)
        self.assertEqual(4, self.items[0].quality)

    def test_sulfuras_static_quality(self):
        self.items.append(Item("Sulfuras, Hand of Ragnaros", 1, 80))
        self.gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", self.items[0].name)
        self.assertEqual(1, self.items[0].sell_in)
        self.assertEqual(80, self.items[0].quality)

    def test_concert_quality_gap_1(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 7, 10))
        self.gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", self.items[0].name)
        self.assertEqual(6, self.items[0].sell_in)
        self.assertEqual(12, self.items[0].quality)
        self.gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", self.items[0].name)
        self.assertEqual(5, self.items[0].sell_in)
        self.assertEqual(14, self.items[0].quality)
        self.gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", self.items[0].name)
        self.assertEqual(4, self.items[0].sell_in)
        self.assertEqual(17, self.items[0].quality)
        for _ in range(4):
            self.gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", self.items[0].name)
        self.assertEqual(0, self.items[0].sell_in)
        self.assertEqual(29, self.items[0].quality)
        self.gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", self.items[0].name)
        self.assertEqual(-1, self.items[0].sell_in)
        self.assertEqual(0, self.items[0].quality)

if __name__ == '__main__':
    unittest.main()
