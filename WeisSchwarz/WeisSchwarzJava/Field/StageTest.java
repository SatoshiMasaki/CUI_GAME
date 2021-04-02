package WeisSchwarz.Field;

import org.junit.jupiter.api.Test;

import WeisSchwarz.Card.Card;
import WeisSchwarz.Card.DC.S51_001;

class StageTest {

	@Test
	void test() {
		Stage stage = new Stage();
		Card c = new S51_001();
		stage.add(c, 0);
		
		System.out.println(stage.get(0));
	}

}
