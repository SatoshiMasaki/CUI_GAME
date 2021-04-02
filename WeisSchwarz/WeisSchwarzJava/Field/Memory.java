package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;

public class Memory {
	List<Card> memory;

	public Memory() {
		memory = new ArrayList<Card>();
	}
	
	public void showMemory() {
		int i = 1;
		for (Card card : memory) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}
		
	}

	public int countMemory() {
		return memory.size();
	}
}
