package WeisSchwarz.GameController;

import WeisSchwarz.Field.Field;

public class DrawPhase {
	public static void draw(Field self, Field opponent) {
		self.getHands().add(self.getDeck().draw());
	}
}
