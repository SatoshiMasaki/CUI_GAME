package WeisSchwarz.Card.DC;

import java.util.ArrayList;
import java.util.Arrays;

import WeisSchwarz.Card.CardUtil.CardType;
import WeisSchwarz.Card.CardUtil.Color;
import WeisSchwarz.Card.CardUtil.Status;
import WeisSchwarz.Card.CardUtil.TriggerType;
import WeisSchwarz.Card.Chara;

public class S51_001 extends Chara{
	public S51_001() {
		this.setName("オン・ステージアスナ");
		this.setColor(Color.YELLOW);
		this.setCardType(CardType.CHARA);
		this.setTrigger(TriggerType.NONE);
		this.setPower(1000);
		this.setLevel(0);
		this.setCost(0);
		this.setSoul(1);
		this.setStatus(Status.STAND);
		this.setFeature(new ArrayList<String>(Arrays.asList("アバター", "武器")));
	}
	
	@Override
	public String toString() {
		return this.getName();
	}
}
