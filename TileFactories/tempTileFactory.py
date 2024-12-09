from TileFactories import BaseCreator
import tempTile

class tempTileFactory(BaseCreator.BaseCreator):
	def _factoryMethod(self):
		return tempTile.tempTile()
