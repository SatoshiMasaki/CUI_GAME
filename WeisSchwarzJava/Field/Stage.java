package WeisSchwarz.Field;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.Card;
import WeisSchwarz.Card.CardUtil.Status;

/**
 * 舞台のインスタンス。マーカーもちキャラを考慮し、一応二次元配列としている。 二次元配列のアクセスは.get().get()となる？
 * 
 * @author umbre
 *
 */
public class Stage {
	List<ArrayList<Card>> stage;

	public Stage() {
		stage = new ArrayList<ArrayList<Card>>();
		for (int i = 0; i < 5; i++) {
			stage.add(new ArrayList<Card>());
		}
	}

	public void add(Card card, int index) {
		stage.get(index).add(card);
	}

	public Card get(int index) {
		if (stage.get(index).isEmpty()) {
			return stage.get(index).get(0); // TODO NULL処理
		} else {
			return stage.get(index).get(0);
		}
	}
	
	public Card pop(int index) {
		if(stage.get(index).size() == 1) {
			return stage.get(index).remove(0);
		}else {
			return stage.get(index).remove(0); // TODO マーカー処理
		}
	}
	
	public boolean isExist(int index) {
		if(stage.get(index).isEmpty()) {
			return false;
		}else {
			return true;
		}
	}
	
	public void changeStatus(int index, Status status) {
		if (this.isExist(index)){
			stage.get(index).get(0).setStatus(Status.STAND);
		}
		
	}
}
