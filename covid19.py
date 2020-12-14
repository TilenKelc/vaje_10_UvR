obiski = [("Ana", "kava"), ("Berta", "kava"), ("Cilka", "telovadba"),
          ("Dani", "zdravnik"), ("Ana", "zdravnik"), ("Cilka", "kava"),
          ("Ema", "telovadba"), ("Fanči", "telovadba"),
          ("Greta", "telovadba")]


def osebe(obiski):
    nov = []
    # for osebe,aktivnosti in obiski:
    #     nov.append(osebe)
    # return set(nov)
    return set([osebe for osebe, aktivnosti in obiski if osebe not in nov])


def aktivnosti(obiski):
    nov = []
    return set([aktivnosti for osebe, aktivnosti in obiski if aktivnosti not in nov])


def udelezenci(aktivnost, obiski):
    # ud = []
    # for osebe,aktivnosti in obiski:
    #      if aktivnost == aktivnosti:
    #         ud.append(osebe)
    #
    # return set(ud)
    return set([osebe for osebe, aktivnosti in obiski if aktivnost == aktivnosti])


def po_aktivnostih(obiski):
    dict = {}
    for osebe, aktivnosti in obiski:
        dict[aktivnosti] = set(udelezenci(aktivnosti, obiski))
    return dict


def skupine(obiski):
    s = []
    dict = po_aktivnostih(obiski)
    return [osebe for osebe in dict.values() if osebe not in s]

    # s =[]
    # dict = po_aktivnostih(obiski)
    # for osebe in dict.values():
    #     s.append(osebe)
    # return s


def okuzeni(skupine, nosilci):
    okuzeni = []
    if len(nosilci) == 0:
        return set(okuzeni)
    for skupina in skupine:

        for nosilec in nosilci:
            if nosilec in skupina:
                okuzeni += skupina

    return set(okuzeni).difference(nosilci)


def zlati_prinasalec(skupine):
    max = 0

    dictoseb = {}

    sett = set()
    for skupina in skupine:
        sett.update(skupina)

    for oseba in sett:
        okuzeniii = okuzeni(skupine, [oseba])
        st_okuzenih = len(okuzeniii)

        if st_okuzenih >= max:
            max = st_okuzenih
            dictoseb[oseba] = st_okuzenih

    najosebe = []
    maks = 0

    for oseba, st_okuz in dictoseb.items():
        if st_okuz >= maks:
            maks = st_okuz

    for oseba, st_okuz in dictoseb.items():
        if st_okuz == maks:
            najosebe.append(oseba)

    najosebe.sort()
    return najosebe[0]


def korakov_do_vseh(skupine, prvi):

    zenske = skupine.copy()
    okuzeni = {prvi}
    korak = 0
    dolzina = 0

    while zenske:
        if len(zenske) != dolzina:
            dolzina = len(zenske)
        else:
            return None

        korak += 1
        okuzene_skupine_zensk = []

        for skupina in zenske[::-1]:
            for oseba in skupina:
                if oseba in okuzeni:
                    okuzene_skupine_zensk.append(skupina)
                    zenske.remove(skupina)
                    break

        for skupina in okuzene_skupine_zensk:
            okuzeni.update(skupina)

    return korak


import unittest
import random
import ast


class TestObvezna(unittest.TestCase):
    ime = "".join(random.choice("qwertyuiop") for _ in range(10))
    aktivnost = "".join(random.choice("asdfghjkl") for _ in range(10))
    rnd_obiski = [(ime, aktivnost)]

    obiski = [("Ana", "kava"), ("Berta", "kava"), ("Cilka", "telovadba"),
              ("Dani", "zdravnik"), ("Ana", "zdravnik"), ("Cilka", "kava"),
              ("Ema", "telovadba")]

    def test_osebe(self):
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema"}, osebe(self.obiski))
        self.assertEqual({self.ime}, osebe(self.rnd_obiski))
        self.assertEqual(set(), osebe([]))

    def test_aktivnosti(self):
        self.assertEqual({"zdravnik", "kava", "telovadba"}, aktivnosti(self.obiski))
        self.assertEqual({self.aktivnost}, aktivnosti(self.rnd_obiski))
        self.assertEqual(set(), aktivnosti([]))

    def test_udelezenci(self):
        self.assertEqual({"Ana", "Berta", "Cilka"}, udelezenci("kava", self.obiski))
        self.assertEqual(set(), udelezenci("sprehod", self.obiski))
        self.assertEqual({self.ime}, udelezenci(self.aktivnost, self.rnd_obiski))
        self.assertEqual(set(), udelezenci(self.aktivnost, []))

    def test_po_aktivnostih(self):
        self.assertEqual({
            "kava": {"Ana", "Berta", "Cilka"},
            "zdravnik": {"Ana", "Dani"},
            "telovadba": {"Cilka", "Ema"}},
            po_aktivnostih(self.obiski))
        self.assertEqual({self.aktivnost: {self.ime}}, po_aktivnostih(self.rnd_obiski))

    def test_skupine(self):
        def form(s):
            return sorted(s, key=lambda x: "-".join(sorted(x)))

        self.assertEqual(
            form([{"Ana", "Berta", "Cilka"}, {"Dani", "Ana"}, {"Cilka", "Ema"}]),
            form(skupine(self.obiski)))

        self.assertEqual(
            form([{self.ime}]),
            form(skupine([(self.ime, self.aktivnost)])))

    def test_okuzeni(self):
        skupine = [{"Ana", "Berta", "Cilka"}, {"Dani", "Ana"}, {"Cilka", "Ema"}, {"Fanči"}]

        self.assertEqual({"Berta", "Cilka", "Dani"},
                         okuzeni(skupine, {"Ana"}))
        self.assertEqual({"Ana", "Berta", "Ema"},
                         okuzeni(skupine, {"Cilka"}))
        self.assertEqual({"Ana", "Cilka"},
                         okuzeni(skupine, {"Ema", "Dani"}))
        self.assertEqual({"Ana", "Ema"},
                         okuzeni(skupine, {"Cilka", "Berta"}))
        self.assertEqual({"Berta", "Cilka", "Dani"},
                         okuzeni(skupine, {"Ana", "Ema"}))
        self.assertEqual({"Cilka"},
                         okuzeni(skupine, {"Ema"}))
        self.assertEqual(set(),
                         okuzeni(skupine, {"Fanči"}))
        self.assertEqual(set(),
                         okuzeni(skupine, set()))
        self.assertEqual({self.ime},
                         okuzeni([{self.ime, self.aktivnost}], {self.aktivnost}))

    def test_zlati_prinasalec(self):
        self.assertEqual(
            "Ana",
            zlati_prinasalec([{"Ana", "Berta", "Cilka"}, {"Dani", "Ana"}, {"Cilka", "Ema"}, {"Cilka"}]))
        self.assertEqual(
            "Cilka",
            zlati_prinasalec([{"Fanči", "Berta", "Cilka"}, {"Dani", "Fanči"}, {"Cilka", "Ema"}, {"Cilka"}]))
        self.assertEqual(
            "Cilka",
            zlati_prinasalec([{"Fanči", "Berta", "Cilka"}, {"Dani", "Fanči"}, {"Cilka", "Ema"}, {"Fanči"}]))

    def test_korakov_do_vseh(self):
        skupine = [{"Cilka", "Ema", "Jana", "Saša"},
                   {"Ema"},
                   {"Fanči", "Greta", "Saša"},
                   {"Greta", "Nina"},
                   {"Greta", "Olga", "Rebeka"},
                   {"Micka", "Ana", "Klara"},
                   {"Fanči", "Iva", "Berta", "Špela"},
                   {"Klara", "Cilka", "Dani"},
                   {"Petra", "Dani", "Lara", "Špela"}]
        self.assertEqual(5, korakov_do_vseh(skupine, "Ana"))
        self.assertEqual(4, korakov_do_vseh(skupine, "Klara"))
        self.assertEqual(4, korakov_do_vseh(skupine, "Dani"))
        self.assertEqual(3, korakov_do_vseh(skupine, "Ema"))

        skupine.append({"Tina"})
        self.assertIsNone(korakov_do_vseh(skupine, "Ema"))
        self.assertIsNone(korakov_do_vseh(skupine, "Tina"))
        skupine[-1].add("Urša")
        skupine[-1].add("Vesna")
        skupine.append({"Zala", "Žana"})
        self.assertIsNone(korakov_do_vseh(skupine, "Ema"))
        self.assertIsNone(korakov_do_vseh(skupine, "Tina"))


class TestOneLineMixin:
    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__, "r", encoding="utf-8").read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        func
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "preberi_zapiske", "osebe", "aktivnosti", "udelezenci",
            "po_aktivnostih", "skupine", "okuzeni", "zlati_prinasalec",
            "korakov_do_vseh"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")


class TestDodatna(unittest.TestCase, TestOneLineMixin):
    def test_oneline(self):
        for func in (osebe, aktivnosti, udelezenci, po_aktivnostih, skupine):
            self.assert_is_one_line(func)


class TestIzziv(unittest.TestCase, TestOneLineMixin):
    def test_oneline(self):
        for func in (okuzeni, zlati_prinasalec):
            self.assert_is_one_line(func)


if __name__ == "__main__":
    unittest.main()
