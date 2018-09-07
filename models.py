class Order():
    idcounter=0
    def __init__(self,meal,user,location,quantity):
        self.meal=meal
        self.user=user
        self.location=location
        self.quantity=quantity
        Order.idcounter+=1

    def jsonfiy(self):
        order={
            'id':Order.idcounter,
            "meal":self.meal,
            'user':self.user,
            'location':self.location,
            'quantity':self.quantity

        }
        return order

class FastFood():
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def jsonfiy(self):
        fastfood={
            'name':self.name,
            'price':self.price

        }
        return fastfood

class DBhandler(Order, FastFood):
    def __init__(self):
        self.counter=0
        self.orders=[]
        self.fastfoods=[]
    
    def get_one_order(self, id):
        for order in self.orders:
            if order['id'] == id:
                return order
        return {'message':"order {} not found".format(id)},404
        
    def get_one_fast_food(self,id):
        for fastfood in self.fastfoods:
            if fastfood['id']==id:
                return fastfood
        return {'message':"fastfood {} not found four or four".format(id)},404
    
    def get_all_fast_foods(self):
        return self.fastfoods

    def get_all_orders(self):
        return self.orders
    
    def create_order(self,data):
        order_obj=Order
        data=order_obj(data['meal'],data['user'],data['location'],data['quantity'])
        order=data.jsonfiy()
        order['id']=self.counter = self.counter + 1
        self.orders.append(order)
        return order

    def create_fast_food(self,data):
        fast_food_obj=FastFood
        data=fast_food_obj(data['name'],data['price'])
        fastfood=data.jsonfiy()
        fastfood['id']=self.counter = self.counter + 1
        self.fastfoods.append(fastfood)
        return fastfood

    def update_order(self,id,data):
        order=self.get_one_order(id)
        
        order.update(data)        
        return order
        