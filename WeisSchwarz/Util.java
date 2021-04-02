package WeisSchwarz;

import java.util.Scanner;

/**
 * コードを書くための万能クラス。すべてstatic実装をしている。
 * 
 * @author umbre
 *
 */
public class Util {
	private static Scanner scanner;

	/**
	 * @param min 選択範囲の最小値。基本的に１。
	 * @param max 選択範囲の最大値。
	 * @return そのまま代入できるように - 1してある。
	 */
	public static int selectCard(int min, int max) {
		while (true) {
			System.out.println("カードを選んでください : ");
			try {
				scanner = new Scanner(System.in);
				int index = scanner.nextInt();

				if (min <= index && index <= max) {
					return index - 1;
				}
			} catch (Exception e) {
				System.out.println("数値を入力してください");
			}

		}

	}

	public static boolean selectCommand() {
		while (true) {
			try {
				scanner = new Scanner(System.in);
				int index = scanner.nextInt();

				if (index == 1) {
					return true;
				} else {
					return false;
				}

			} catch (Exception e) {
				System.out.println("数値を入力してください");
			}
		}

	}
}
