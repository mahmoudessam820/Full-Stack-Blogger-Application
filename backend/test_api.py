#----------------------------------------------------------------#
# Imports
#----------------------------------------------------------------#
import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from model import setup_db


#----------------------------------------------------------------#
# Unittest Setup
#----------------------------------------------------------------#
class ArticleTestCase(unittest.TestCase):
    """This class represents the Articles test case."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.user_name = 'postgres'
        self.password = 1234
        self.host = 'localhost:5432'
        self.database_name = 'blogger'
        self.database_path = "postgres://{}:{}@{}/{}".format(
            self.user_name, self.password, self.host, self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

#----------------------------------------------------------------#
# Test Cases
#----------------------------------------------------------------#
    def test_get_all_articles(self):
        req = self.client().get('/articles')
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)

    def test_add_new_article(self):
        body = {
            "title": "web app",
            "body": "This is a very basic query to display all data from a table. Notice that this query only has one character after SELECT: '*' (this denotes all columns). Therefore, you don't need to list the names of the columns. Of course, remember to write FROM and the name of the table from which you want to retrieve data. In this example"
        }
        req = self.client().post('/new', json=body)
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['Message'], 'Article added')

    def test_update_article(self):
        body = {
            "title": "About HTML",
            "body": "In this article we will talk about html"
        }
        req = self.client().put('/update/8', json=body)
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['Message'], 'Article Update')

    def test_del_one_article(self):
        req = self.client().delete('/delete/3')
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['Success'], True)
        self.assertEqual(data['Message'], 'Article Deleted')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
