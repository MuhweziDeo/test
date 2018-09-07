import  unittest
import json
from app import app


class TestAPI(unittest.TestCase):
	def setUp(self):
		self.app=app
		self.client=self.app.test_client()
		self.fastfood={
		  "id": 1,
		  "name": "pizza",
		  "price": 400
		}
		self.order={
		  "id": 2,
		  "meal": "pizza",
		  "user": "dee",
		  "location": "kla",
		  "quantity": 5
		}
	def test_create_order(self):
		res=self.client.post('api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		self.assertEqual(res.status_code,200)

	def test_create_fastfood(self):
		res=self.client.post('api/v1/fastfoods',data=json.dumps(self.fastfood),content_type='application/json')
		self.assertEqual(res.status_code,200)

	def test_get_one_order(self):
		res=self.client.post('api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		self.assertEqual(res.status_code,200)
		res=self.client.get('api/v1/orders/2')
		self.assertEqual(res.status_code,200)
		self.assertIn('2',str(res.data))
		# self.ass

	def test_get_one_fastfood(self):
		res=self.client.post('api/v1/fastfoods',data=json.dumps(self.fastfood),content_type='application/json')
		self.assertEqual(res.status_code,200)
		res=self.client.get('api/v1/fastfoods/1')
		self.assertEqual(res.status_code,200)
		self.assertIn('1',str(res.data))

	def test_get_all_fastfoods(self):
		res=self.client.post('api/v1/fastfoods',data=json.dumps(self.fastfood),content_type='application/json')
		# self.assertEqual(res.status_code,200)
		res=self.client.get('api/v1/fastfoods')
		self.assertEqual(res.status_code,200)
		self.assertIn("pizza",str(res.data))

	def test_get_all_orders(self):
		res=self.client.post('api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		self.assertEqual(res.status_code,200)
		res=self.client.get('api/v1/orders')
		self.assertEqual(res.status_code,200)
		self.assertIn("pizza",str(res.data))
	

		    