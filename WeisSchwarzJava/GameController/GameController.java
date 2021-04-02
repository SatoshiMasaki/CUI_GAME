package WeisSchwarz.GameController;

import java.util.Random;

import WeisSchwarz.Field.Field;

public class GameController {
	private Field myPlayer;
	private Field enemyPlayer;
	private int turnPlayer;
	private Field self;
	private Field opponent;

	public GameController(Field myPlayer, Field enemyPlayer) {
		this.myPlayer = myPlayer;
		this.enemyPlayer = enemyPlayer;

		Random random = new Random();
		this.turnPlayer = random.nextInt(2);
	}

	public void gameStart() {
		while (true) {
			if (turnPlayer == 0) {
				self = myPlayer;
				opponent = enemyPlayer;
			} else {
				self = enemyPlayer;
				opponent = myPlayer;
			}

			StandPhase.toStand(self, opponent);
			DrawPhase.draw(self, opponent);
			ClockPhase.checkClockPhase(self, opponent);
			MainPhase.selectCommand(self, opponent);
			CxPhase.checkUseCx(self, opponent);
			
			
			
			if (turnPlayer == 0) {
				turnPlayer = 1;
			}else {
				turnPlayer = 0;
			}
		}

	}
}
