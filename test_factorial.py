import unittest
from main import check_straight
from main import check_3ofa_kind
from main import check_royal_flush
from main import play_cards


class MyTestCase(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)
        self.assertEqual(check_straight('S10', 'SJ', 'SQ'), 12)
        self.assertEqual(check_straight('S2', 'S3', 'S4'), 4)
        self.assertEqual(check_straight('SJ', 'SQ', 'SK'), 13)


    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S8', 'S8', 'S8'), 8)
        self.assertEqual(check_3ofa_kind('S2', 'S2', 'S2'), 2)
        self.assertEqual(check_3ofa_kind('SK', 'SK', 'SK'), 13)
        self.assertEqual(check_3ofa_kind('SA', 'SA', 'SA'), 14)
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S7'), 0)
        self.assertEqual(check_3ofa_kind('S2', 'SA', 'S4'), 0)


    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('S6', 'S6', 'S2'), 0)
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_royal_flush('SQ', 'SK', 'SA'), 14)


    def test_play_cards(self):
        #ROyal flush
        self.assertEqual(play_cards('SQ', 'SK', 'SA', 'S2', 'S3', 'S4'), -1)
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'SQ', 'SK', 'SA'), 1)
        self.assertEqual(play_cards('SQ', 'SK', 'SA', 'SQ', 'SK', 'SA'), 0)

        #straights
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S8', 'S9', 'S10'), 1)
        self.assertEqual(play_cards('S8', 'S9', 'S10', 'S5', 'S6', 'S7'), -1)
        self.assertEqual(play_cards('S10', 'SJ', 'SQ', 'S10', 'SJ', 'SQ'), 0)

        # 3 of a kind
        self.assertEqual(play_cards('SK', 'SK', 'SK', 'SJ', 'SJ', 'SJ'), -1)
        self.assertEqual(play_cards('SJ', 'SJ', 'SJ', 'SK', 'SK', 'SK'), 1)
        self.assertEqual(play_cards('SK', 'SK', 'SK', 'SK', 'SK', 'SK'), 0)

        # straight vs 3 of a kind
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S8', 'S8', 'S8'), -1)
        self.assertEqual(play_cards('S8', 'S8', 'S8', 'S5', 'S6', 'S7'), 1)

        # draws
        self.assertEqual(play_cards('S2', 'S4', 'S5', 'S3', 'S7', 'S9'), 0)
        self.assertEqual(play_cards('S2', 'S3', 'S6', 'S5', 'S7', 'S10'), 0)


if __name__ == '__main__':
    unittest.main()



