from agent.agent.agent import ShoppingAgent
from agent.configuration import configuration
import spade

def run():
  a = ShoppingAgent(
    f'{configuration.XMPP_USERNAME}@{configuration.XMPP_DOMAIN}', 
    configuration.XMPP_PASSWORD
  )
  a.start()
  input("Press ENTER to exit.\n")
  a.stop()
  spade.quit_spade()
