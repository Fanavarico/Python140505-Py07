#mikham yek tabe improt b

#price.py  

#from price import show_plans
from .price import show_plans



def buy_plan(plan):
	plans = show_plans()
	if plan in plans:
		return True
	else:
		return False


	