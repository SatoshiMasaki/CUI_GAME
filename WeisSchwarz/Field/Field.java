package WeisSchwarz.Field;

/**
 * WeisSchwarz.Fieldパッケージのクラスをインスタンス化して、保持するクラス
 * @author umbre
 *
 */
public class Field {
	private Deck deck;
	private WaitingRoom waitingRoom;
	private Stage stage;
	private Clock clock;
	private Level level;
	private Cx cx;
	private Stock stock;
	private Memory memory;
	private Hands hands;
	
	public Deck getDeck() {
		return deck;
	}

	public WaitingRoom getWaitingRoom() {
		return waitingRoom;
	}

	public Stage getStage() {
		return stage;
	}

	public Clock getClock() {
		return clock;
	}

	public Level getLevel() {
		return level;
	}

	public Cx getCx() {
		return cx;
	}

	public Stock getStock() {
		return stock;
	}

	public Memory getMemory() {
		return memory;
	}

	public Hands getHands() {
		return hands;
	}

	public Field() {
		deck = new Deck();
		waitingRoom = new WaitingRoom();
		stage = new Stage();
		clock = new Clock();
		level = new Level();
		cx = new Cx();
		stock = new Stock();
		memory = new Memory();
		hands = new Hands();
	}
	
	
}
