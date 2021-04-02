package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;

public class Hands {
	List<Card> hands;
	public Hands() {
		hands = new ArrayList<Card>();
	}
	
	public void add(Card card) {
		hands.add(card);
	}
	
	public Card pop(int index) {
		return hands.remove(index);
	}
	
	public int countHands() {
		return hands.size();
	}
	
	public void showHands() {
		int i = 1;
		for (Card card : hands) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}
	}

}
