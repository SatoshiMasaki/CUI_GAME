package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

import WeisSchwarz.Card.Card;
import WeisSchwarz.Util;

/**
 * 山札置き場のインスタンス
 * @author umbre
 *
 */
public class Deck {
	LinkedList<Card> deck;

	public Deck() {
		deck = new LinkedList<Card>();
	}

	public void add(Card c) {
		deck.addLast(c);
	}

	public Card draw() {
		Card card = deck.poll();
		this.checkReflash();
		return card;
	}

	public void turnOver() {
		System.out.println(deck.peek().toString());
	}

	public void turnOver(int i) {
		for (int j = 0; j < i; j++) {
			System.out.println(deck.peek().toString());
			this.checkReflash();
		}
	}

	public boolean checkCard(Card c) {
		if (deck.contains(c)) {
			return true;
		} else {
			return false;
		}
	}

	/*
	 * リフレッシュについては全体やGameControllerと要相談
	 */
	public void checkReflash() {
		if (deck.size() == 0) {

		} else {

		}
	}

	public Card searchCard() {
		int i = 1;
		for (Card card : deck) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}

		int selectCard = Util.selectCard(1, i);
		return deck.remove(selectCard - 1);
	}

	/*
	 * 無理やりインスタンスを生成することで型変換しているがそれでいいのか？
	 */
	public void shuffle() {
		ArrayList<Card> container = new ArrayList<Card>(deck);
		Collections.shuffle(container);

		deck = new LinkedList<Card>(container);
	}

}
