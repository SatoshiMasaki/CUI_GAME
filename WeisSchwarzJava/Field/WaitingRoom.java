package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;

public class WaitingRoom {
	List<Card> waitingRoom;
	
	public WaitingRoom() {
		waitingRoom = new ArrayList<Card>();
	}
	
	public void add(Card c) {
		waitingRoom.add(c);
	}
	
	public void showWaitingRoom() {
		int i = 1;
		for (Card card : waitingRoom) {
			System.out.println(String.format("%d : %s", i, card.toString()));
			i++;
		}
		
	}
	
	
}
