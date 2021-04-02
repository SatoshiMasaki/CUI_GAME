package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;

public class Clock {
	List<Card> clock;

	public Clock() {
		clock = new ArrayList<Card>();
	}

	public void levelCheck() {
		if (this.clock.size() >= 7) {
			// level up 処理
		}
	}
	
	public void add(Card c) {
		this.clock.add(c);
	}
	
	public int countClock() {
		return clock.size();
	}
	
	public void showclock() {
		int i = 1;
		for (Card card : clock) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}
		
	}

}
