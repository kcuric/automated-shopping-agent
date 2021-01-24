from agent.services import api

import spade
import asyncio

class ShoppingAgent(spade.agent.Agent):

  class ShoppingBehaviour(spade.behaviour.CyclicBehaviour):

    assigned = False

    async def on_start(self):
      print('Starting pooling ...')

    def buy_product(self, order):
      print(order)

    def check_for_open_orders(self):
      order = api.check_for_open_orders()
      if(order):
        api.assign_order(order['_id'])
        self.assigned = True
        self.buy_product(order)

    async def run(self):
      if(not self.assigned):
        self.check_for_open_orders()
      await asyncio.sleep(5)


  async def setup(self):
    print("Shopping agent starting ...")
    shopping_behaviour = self.ShoppingBehaviour()
    self.add_behaviour(shopping_behaviour)
