def se_napadata(top1, top2):
    if (top1[0] == top2[0] or top1[1] == top2[1]) and top1 != top2:
        return True
    else:
        return False

def napadeni(top, topovi):
    temp = []
    for t in topovi:
        if (top[0] == t[0] or top[1] == t[1]) and top != t:
            temp.append(t)
    return temp

def napadenost(top, topovi):
    return len(napadeni(top, topovi))

def varen(top, topovi):
    if topovi:
        for t in topovi:
            if ((top[0] == t[0] or top[1] == t[1]) and top != t):
                return False
            else:
                return True
    else:
        return True

def vse_varno(topovi):
    for top in topovi:
        if not varen(top, topovi):
            return False
    else:
        return True

def najbolj_napaden(topovi):
    if topovi:
        temp = []
        for t1 in topovi:
            count = 0
            for t2 in topovi:
                if se_napadata(t1, t2):
                    count += 1
            temp = temp + [count]
        if max(temp):
            return topovi[temp.index(max(temp))]
    return None


def direkten_napad(top1, top2, topovi):
    if top1[1] == top2[1] and top1 != top2:
        while True:
            if ord(top1[0]) <= ord(top2[0]):
                top1 = chr(ord(top1[0]) + 1) + top1[1]
            else:
                top1 = chr(ord(top1[0]) - 1) + top1[1]
            if top1 in topovi and top1 != top2:
                return False
            elif top1 == top2:
                return True
    elif top1[0] == top2[0] and top1 != top2:
        while True:
            if ord(top1[1]) <= ord(top2[1]):
                top1 = top1[0] + chr(ord(top1[1]) + 1)
            else:
                top1 = top1[0] + chr(ord(top1[1]) - 1)
            if top1 in topovi and top1 != top2:
                return False
            elif top1 == top2:
                return True
    else:
        return False


# ------------ #

import unittest


class TestObvezna(unittest.TestCase):
    def test_se_napadate(self):
        self.assertTrue(se_napadata("a4", "d4"))
        self.assertTrue(se_napadata("e8", "c8"))
        self.assertTrue(se_napadata("e8", "e5"))
        self.assertTrue(se_napadata("f4", "f6"))

        self.assertFalse(se_napadata("f4", "g8"))
        self.assertFalse(se_napadata("g8", "f4"))
        self.assertFalse(se_napadata("c3", "c3"))

    def test_napadeni(self):
        self.assertEqual(["c1", "c8", "c6", "a3", "h3"],
                         napadeni("c3", ["c1", "c3", "d6", "c8", "c6", "e5", "a3", "h3"]))
        self.assertEqual(["c1", "c8", "c6", "a3", "h3"],
                         napadeni("c3", ["c1", "c3", "c8", "c6", "a3", "h3"]))
        self.assertEqual(["c3", "c4", "c5", "a1"],
                         napadeni("c1", ["c1", "c3", "c4", "c5", "a1"]))
        self.assertEqual([], napadeni("a8", ["c1", "a8", "c6", "h3"]))
        self.assertEqual([], napadeni("a8", ["a8"]))

    def test_napadenost(self):
        self.assertEqual(5, napadenost("c3", ["c1", "c3", "d6", "c8", "c6", "e5", "a3", "h3"]))
        self.assertEqual(5, napadenost("c3", ["c1", "c3", "c8", "c6", "a3", "h3"]))
        self.assertEqual(0, napadenost("a8", ["c1", "a8", "c6", "h3"]))
        self.assertEqual(0, napadenost("a8", ["a8"]))

    def test_varen(self):
        self.assertFalse(varen("c3", ["c1", "d6", "c8", "c6", "e5", "a3", "h3"]))
        self.assertFalse(varen("c3", ["c1", "c8", "c6", "a3", "h3"]))
        self.assertTrue(varen("a8", ["c1", "c6", "h3"]))
        self.assertTrue(varen("a8", []))

    def test_najbolj_napaden(self):
        self.assertEqual("c5", najbolj_napaden(["a5", "c5", "f5", "c6", "c8", "d3", "f7"]))
        self.assertEqual("f5", najbolj_napaden(["a5", "e5", "f5", "c6", "c8", "d3", "f7"]))

        self.assertIsNone(najbolj_napaden(["a5", "c6", "e8", "d3"]))
        self.assertIsNone(najbolj_napaden([]))

        self.assertEqual("a5", najbolj_napaden(["a5", "a6"]))
        self.assertEqual("a6", najbolj_napaden(["a6", "a5"]))

    def test_vse_varno(self):
        self.assertFalse(vse_varno(["a5", "c5", "f5", "c6", "c8", "d3", "f7"]))
        self.assertTrue(vse_varno(["a5", "c6", "e8", "d3"]))
        self.assertTrue(vse_varno(["a5", "c6", "e8", "d3"]))


class TestDodatna(unittest.TestCase):
    def test_direkten_napad(self):
        pozicija = ["a5", "c5", "f5", "c6", "c8", "d3", "f7"]

        self.assertFalse(direkten_napad("a5", "a5", pozicija))

        self.assertFalse(direkten_napad("a5", "c8", pozicija))
        self.assertFalse(direkten_napad("c8", "a5", pozicija))
        self.assertTrue(direkten_napad("f5", "f7", pozicija))
        self.assertTrue(direkten_napad("f7", "f5", pozicija))

        self.assertTrue(direkten_napad("a5", "c5", pozicija))
        self.assertTrue(direkten_napad("c5", "a5", pozicija))
        self.assertTrue(direkten_napad("c5", "f5", pozicija))
        self.assertTrue(direkten_napad("f5", "c5", pozicija))
        self.assertFalse(direkten_napad("f5", "a5", pozicija))
        self.assertFalse(direkten_napad("a5", "f5", pozicija))

        self.assertTrue(direkten_napad("c5", "c6", pozicija))
        self.assertTrue(direkten_napad("c6", "c5", pozicija))
        self.assertTrue(direkten_napad("c6", "c8", pozicija))
        self.assertTrue(direkten_napad("c8", "c6", pozicija))
        self.assertFalse(direkten_napad("c8", "c5", pozicija))
        self.assertFalse(direkten_napad("c5", "c8", pozicija))
        self.assertFalse(direkten_napad("c5", "c8", pozicija))


if __name__ == "__main__":
    unittest.main()
