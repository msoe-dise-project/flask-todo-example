import argparse
import datetime as dt
import os
import random
import sys
import unittest

import requests

BASE_URL_KEY = "BASE_URL"

class TodoServiceTests(unittest.TestCase):
    def get_url(self):
        return os.path.join(os.environ[BASE_URL_KEY], "v1/todos")

    def test_insert(self):
        obj = {
            "description" : "Write some tests",
            "due_date" : (dt.datetime.now() + dt.timedelta(days=1)).isoformat(),
        }
                
        response = requests.post(self.get_url(), json=obj)
        
        self.assertEqual(response.status_code, 201)
        
    def test_list(self):
        for item_id in range(1, 6):
            obj = {
                "description" : "Write some tests",
                "due_date" : (dt.datetime.now() + dt.timedelta(days=1)).isoformat(),
            }

            response = requests.post(self.get_url(), json=obj)

            self.assertEqual(response.status_code, 201)

        url = os.path.join(self.get_url())
        response = requests.get(self.get_url())

        self.assertEqual(response.status_code, 200)

        todo_items = response.json()

        self.assertGreaterEqual(len(todo_items["todo_items"]), 5)

    def test_get(self):
        obj = {
            "description" : "Write some tests",
            "due_date" : (dt.datetime.now() + dt.timedelta(days=1)).isoformat(),
        }

        response = requests.post(self.get_url(), json=obj)
        self.assertEqual(response.status_code, 201)
        obj = response.json()
        item_id = obj["item_id"]

        url = os.path.join(self.get_url(), str(item_id))
        response = requests.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        todo_item = response.json()
        
        self.assertEqual(todo_item["item_id"], obj["item_id"])
        
        
    def test_mark_complete(self):
        obj = {
            "description" : "Write some tests",
            "due_date" : (dt.datetime.now() + dt.timedelta(days=1)).isoformat(),
        }
        
        response = requests.post(self.get_url(), json=obj)
        
        self.assertEqual(response.status_code, 201)

        obj = response.json()

        url = os.path.join(self.get_url(), str(obj["item_id"]), "mark_complete")
        response = requests.put(url)
        
        self.assertEqual(response.status_code, 200)
        
        url = os.path.join(self.get_url(), str(obj["item_id"]))
        response = requests.get(url)
        
        self.assertEqual(response.status_code, 200)
        obj = response.json()
        self.assertEqual(obj["complete"], True)
        
    def test_mark_incomplete(self):
        obj = {
            "description" : "Write some tests",
            "due_date" : (dt.datetime.now() + dt.timedelta(days=1)).isoformat(),
        }
        
        response = requests.post(self.get_url(), json=obj)
        
        self.assertEqual(response.status_code, 201)

        obj = response.json()

        url = os.path.join(self.get_url(), str(obj["item_id"]), "mark_incomplete")
        response = requests.put(url)
        
        self.assertEqual(response.status_code, 200)
        
        url = os.path.join(self.get_url(), str(obj["item_id"]))
        response = requests.get(url)
        
        self.assertEqual(response.status_code, 200)
        obj = response.json()
        self.assertEqual(obj["complete"], False)
        
    def test_set_due_date(self):
        obj = {
            "description" : "Write some tests"
        }
        
        response = requests.post(self.get_url(), json=obj)
        
        self.assertEqual(response.status_code, 201)

        obj = response.json()
        item_id = obj["item_id"]
        
        url = os.path.join(self.get_url(), str(item_id))
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        obj = response.json()
        self.assertIs(obj["due_date"], None)

        url = os.path.join(self.get_url(), str(item_id), "due_date")
        due_date_str = (dt.datetime.now() + dt.timedelta(days=1)).isoformat()
        obj = { "due_date" : due_date_str }
        response = requests.put(url, json=obj)
        self.assertEqual(response.status_code, 200)
        
        url = os.path.join(self.get_url(), str(item_id))
        response = requests.get(url)
        obj = response.json()
        self.assertEqual(obj["due_date"], due_date_str)
        
    def test_delete(self):
        obj = {
            "description" : "Write some tests"
        }
        
        response = requests.post(self.get_url(), json=obj)
        
        self.assertEqual(response.status_code, 201)

        obj = response.json()
        item_id = obj["item_id"]
        
        response = requests.get(self.get_url())
        obj = response.json()
        
        todo_ids = [todo["item_id"] for todo in obj["todo_items"]]
        
        self.assertIn(item_id, todo_ids)
        
        url = os.path.join(self.get_url(), str(item_id))
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        
        response = requests.get(self.get_url())
        obj = response.json()
        
        todo_ids = [todo["item_id"] for todo in obj["todo_items"]]
        
        self.assertNotIn(item_id, todo_ids)
        
class MetricTests(unittest.TestCase):
    def get_url(self):
        return os.path.join(os.environ[BASE_URL_KEY], "metrics")

    def test_metrics(self):
        response = requests.get(self.get_url())
        self.assertEqual(response.status_code, 200)

class HealthcheckTests(unittest.TestCase):
    def get_url(self):
        return os.path.join(os.environ[BASE_URL_KEY], "healthcheck")

    def test_metrics(self):
        response = requests.get(self.get_url())
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
