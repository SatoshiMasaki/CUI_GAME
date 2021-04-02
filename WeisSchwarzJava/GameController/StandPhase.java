package WeisSchwarz.GameController;

import WeisSchwarz.Card.CardUtil.Status;
import WeisSchwarz.Field.Field;

public class StandPhase {
	public static void toStand(Field self, Field opponent) {
		for (int i = 0; i < 5; i++) {
			self.getStage().changeStatus(i, Status.STAND);
		}
	}
}
