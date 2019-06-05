import unittest
# introduction of mocking in python
# https://www.toptal.com/python/an-introduction-to-mocking-in-python
# https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/
# https://docs.python.org/3/library/unittest.html

from utilities.dbutil import MongoDbUtil
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError

class TestDbUtilMethods(unittest.TestCase):
    """
    create test cases while subclassing unitest.TestCase
    https://docs.python.org/3/library/unittest.html
    call in ModulRoot(ExamStudyCodes)
    python3 -m unittest utilities/unittests_dbutil.py -v
    """
    # skeleton method called before the test cases
    def setUp(self):
        user = "xxxx"
        password = "xxxx"
        port = "27017"
        host = "127.0.0.1"
        dbname = "xxxx"
        self.db = MongoDbUtil.getDB(user, password, dbname)

    # skeleton method called after the test cases
    def tearDown(self):
        self.db = None

    # test case
    # it always return a connection with
    def test_db_type(self):
        self.assertTrue(self.isMongoDB(self.db))

    # test case
    def test_data_fetch(self):
        observed_type = ""
        entry = {}
        try:
            entry = self.db['111111_heartrate'].find_one()
        except ServerSelectionTimeoutError:
            observed_type =""

        heartrate = entry.get('heartrate', None)
        # get the name of the type object, or some_instance.__class__.__name__
        observed_type = type(heartrate).__name__
        expected_type = 'int'
        self.assertEqual(observed_type, expected_type, msg="Failed to fetch hearrate from mongodb!")

    # private methode not beginning with test_ will not be called automatically
    def isMongoDB(self, obj):
        return isinstance(obj, Database)

    # def suite(self):
    #     suite = unittest.TestSuite()
    #     # 'test_getDB' is the method name to be tested
    #     suite.addTest(TestDbUtilMethods('test_getDB'))
    #     return suite

# use it in the command line
# python3 unittest/unittests_dubutil.py
# if __name__ == '__main__':
#    unittest.main()











