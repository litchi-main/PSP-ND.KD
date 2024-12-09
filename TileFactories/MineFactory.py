from TileFactories import BaseCreator
import Mine

class MineFactory(BaseCreator.BaseCreator):
	def _factoryMethod(self):
		return Mine.Mine()
