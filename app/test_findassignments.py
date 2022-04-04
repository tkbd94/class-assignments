import unittest
import helpers

class TestFindAssignments(unittest.TestCase):
    def test_findAssignments_SomePass(self):
        assertRes = [
            {"Student": "Dewbury, Dniren", "Teacher": "Gibbs, Jessa", "Class": "08-2046381"}, 
            {"Student": "Catanheira, Marten", "Teacher": "Weekley, Tate", "Class": "57-9105495"}
            ]
        res = helpers.findAssignments('studentsTestData1.csv', 'teachers.parquet')
        self.assertEqual(res, assertRes)

    def test_FindAssignments_NonePass(self):
        assertRes = []
        res = helpers.findAssignments('studentsTestData2.csv', 'teachers.parquet')
        self.assertEqual(res, assertRes)

    def test_FindAssignments_AllPass(self):
        assertRes = [
            {"Student": "Dewbury, Dniren", "Teacher": "Gibbs, Jessa", "Class": "08-2046381"}, 
            {"Student": "Catanheira, Marten", "Teacher": "Weekley, Tate", "Class": "57-9105495"},
            {"Student": "Olivet, Shae", "Teacher":"Chasney, Trenna", "Class": "76-3364242"}
            ]
        res = helpers.findAssignments('studentsTestData3.csv', 'teachers.parquet')
        self.assertEqual(res, assertRes)