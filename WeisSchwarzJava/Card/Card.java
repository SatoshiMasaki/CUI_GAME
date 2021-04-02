package WeisSchwarz.Card;

import WeisSchwarz.Card.CardUtil.Status;

/**
 * すべてのカードインスタンスの抽象クラス。
 * @author umbre
 *
 */
public abstract class Card {
	public String name;
	public String color;
	public String cardType;
	public String trigger;
	
	public abstract void setStatus(Status status);
	
}
