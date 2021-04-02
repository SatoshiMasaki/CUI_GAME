package WeisSchwarz.GameController;

import java.util.Scanner;

import WeisSchwarz.Field.Field;

public class MainPhase {
	public static void selectCommand(Field self, Field opponent) {
		Scanner scanner = new Scanner(System.in);
		String printSentence = "1 : カードを使う。/n2 : カードを確認する。/n3 : メインフェイズを終了する。";
		System.out.println(printSentence);

		while (true) {
			try {
				int index = scanner.nextInt();

				if (index == 1) {
					useCard(self, opponent);
				} else if (index == 2) {
					checkField(self, opponent);
				} else if (index == 3) {
					System.out.println("メインフェイズを終了します");
					break;
				}

			} catch (Exception e) {
				System.out.println("数値を入力してください");
			}
		}
	}

	public static void checkField(Field self, Field opponent) {

	}

	private static void useCard(Field self, Field opponent) {

	}

}
