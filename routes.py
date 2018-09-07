from models import DBhandler
from flask_restplus import Api,Resource, fields
from app import app

api =Api(app, prefix="/api/v1")


order= api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'meal': fields.String(required=True, description='The task details'),
    'user': fields.String(required=True, description='The task details'),
    'location': fields.String(required=True, description='The task details'),
    'quantity': fields.Integer(required=True, description='The task details')


})

fastfood =api.model('FASTFOOD',{
    'id':fields.Integer,
    'name':fields.String,
    'price':fields.Integer
})


handler=DBhandler()


@api.route('/fastfoods/<int:id>')
class FastFood(Resource):
    def get(self, id):
        return handler.get_one_fast_food(id)

@api.route('/fastfoods')
class FastFoods(Resource):
    def get(self):
        return handler.get_all_fast_foods()

    @api.expect(fastfood) 
    def post(self):
        data=api.payload
        return handler.create_fast_food(data)

@api.route('/orders')
class Orders(Resource):
    def get(self):
        return handler.get_all_orders()
    
    @api.expect(order)
    def post(self):
        data=api.payload
        return handler.create_order(data)

@api.route('/orders/<int:id>')
class Order(Resource):

    def get(self, id):
        return handler.get_one_order(id)