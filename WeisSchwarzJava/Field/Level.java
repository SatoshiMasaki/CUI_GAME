package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;

public class Level {
	List<Card> level;
	
	public Level() {
		level = new ArrayList<Card>();
	}
	
	public void showLevel() {
		int i = 1;
		for (Card card : level) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}
	}

	public int countLevel() {
		return level.size();
	}
}
