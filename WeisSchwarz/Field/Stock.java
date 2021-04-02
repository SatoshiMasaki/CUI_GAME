package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;

public class Stock {
	List<Card> stock;
	public Stock() {
		stock = new ArrayList<Card>();
	}
	
	public void add(Card c) {
		this.stock.add(c);
	}
	
	public int countStock() {
		return stock.size();
	}
	
	public void showStock() {
		int i = 1;
		for (Card card : stock) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}
	}

}
