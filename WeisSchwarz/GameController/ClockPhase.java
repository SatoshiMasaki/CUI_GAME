package WeisSchwarz.GameController;

import WeisSchwarz.Util;
import WeisSchwarz.Field.Field;

public class ClockPhase {
	/**
	 * クロックフェイズを行うかの確認。一度Bool値を返すことで引数にFieldを入れる。
	 * 
	 */
	public static void checkClockPhase(Field self, Field opponent) {
		String printString = "1 : クロックフェイズを行う。/n2 : クロックフェイズをスキップする。";
		System.out.println(printString);
		
		boolean flag = Util.selectCommand();
		if (flag) {
			handsExchange(self);
		}
	}
	
	/**
	 * 本処理。カードを一枚クロックに置き、山札から二枚引く。
	 * 
	 */
	public static void handsExchange(Field field) {
		field.getHands().showHands();
		int index = Util.selectCard(1, field.getHands().countHands());
		field.getClock().add(field.getHands().pop(index));
		
		field.getHands().add(field.getDeck().draw());
		field.getHands().add(field.getDeck().draw());
	}
}
