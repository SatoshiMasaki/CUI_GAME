package WeisSchwarz.Card;

import java.util.ArrayList;
import java.util.List;

import WeisSchwarz.Card.CardUtil.CardType;
import WeisSchwarz.Card.CardUtil.Color;
import WeisSchwarz.Card.CardUtil.Status;
import WeisSchwarz.Card.CardUtil.TriggerType;

public class Chara extends Card{

	private String name;
	private Color color;
	private CardType cardType;
	private TriggerType trigger;

	private int power;
	private int level;
	private int cost;
	private int soul;
	private List<String> feature;
	private Status status;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Color getColor() {
		return color;
	}
	public void setColor(Color color) {
		this.color = color;
	}
	public CardType getCardType() {
		return cardType;
	}
	public void setCardType(CardType cardType) {
		this.cardType = cardType;
	}
	public TriggerType getTrigger() {
		return trigger;
	}
	public void setTrigger(TriggerType trigger) {
		this.trigger = trigger;
	}
	public int getPower() {
		return power;
	}
	public void setPower(int power) {
		this.power = power;
	}
	public int getLevel() {
		return level;
	}
	public void setLevel(int level) {
		this.level = level;
	}
	public int getCost() {
		return cost;
	}
	public void setCost(int cost) {
		this.cost = cost;
	}
	public int getSoul() {
		return soul;
	}
	public void setSoul(int soul) {
		this.soul = soul;
	}
	public List<String> getFeature() {
		return feature;
	}
	public void setFeature(ArrayList<String> feature) {
		this.feature = feature;
	}
	public Status getStatus() {
		return status;
	}
	
	@Override
	public void setStatus(Status status) {
		this.status = status;
	}
}
