from TileFactories import BaseCreator
import EmptyTile

class EmptyTileFactory(BaseCreator.BaseCreator):
	def _factoryMethod(self):
		return EmptyTile.EmptyTile()
