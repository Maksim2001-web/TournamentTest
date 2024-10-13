import runner_and_tournament as rnt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        vs = {'Usain': 10, 'Andre': 9, 'Nick': 3}
        self.runners = {n: rnt.Runner(name=n, speed=v) for n, v in vs.items()}

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    def test_tournament(self):
        tour = rnt.Tournament(90, self.runners['Usain'], self.runners['Nick'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Nick'])

    def test_tournament_2(self):
        tour = rnt.Tournament(90, self.runners['Andre'], self.runners['Nick'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Nick'])

    def test_tournament_3(self):
        tour = rnt.Tournament(90, self.runners['Usain'], self.runners['Andre'], self.runners['Nick'])
        all_results = tour.start()
        self.assertTrue(all_results[3], self.runners['Nick'])

if __name__ == '__main__':
    unittest.main()


