package WeisSchwarz;

import WeisSchwarz.Field.Field;
import WeisSchwarz.GameController.GameController;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Field myPlayer = new Field();
		Field enemyPlayer = new Field();
		GameController gc = new GameController(myPlayer, enemyPlayer);
		gc.gameStart();
	}

}
