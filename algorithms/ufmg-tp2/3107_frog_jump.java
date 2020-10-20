import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Math;

public class Main {
  static int puloSapo(int caminho[], int limCurto, int limLongo) {
    int length = caminho.length;
    int tabelaPulos[][] = new int[length][2];
    int minPulos = 0;
    final int LIM = 999999;

    for (int i = 1; i < length; i++) {
      tabelaPulos[i][0] = LIM;
      tabelaPulos[i][1] = LIM;
    }

    tabelaPulos[0][0] = 0;
    tabelaPulos[0][1] = 0;

    int puloCurto = 0,
    puloLongo = 0,
    menorPulo = 0;

    for (int i = 1; i < length; i++) {
      while (puloLongo < i - 1 && caminho[puloLongo] + limLongo < caminho[i]) {
        puloLongo++;
      }
      while (puloLongo < i - 1 && tabelaPulos[puloLongo][0] == LIM) {
        puloLongo++;
      }
      while (puloCurto < i - 1 && caminho[puloCurto] + limCurto < caminho[i]) {
        puloCurto++;
      }
      while (puloCurto < i - 1 && tabelaPulos[puloCurto][0] == LIM && tabelaPulos[puloCurto][1] == LIM) {
        puloCurto++;
      }
      
      menorPulo = Math.min(tabelaPulos[puloCurto][0], tabelaPulos[puloCurto][1]);

      if (tabelaPulos[puloLongo][0] < LIM && caminho[puloLongo] + limLongo >= caminho[i]) {
        tabelaPulos[i][1] = tabelaPulos[puloLongo][0] + 1;
      }

      if (menorPulo < LIM && caminho[puloCurto] + limCurto >= caminho[i]) {
        tabelaPulos[i][0] = menorPulo + 1;
      }
    }

    minPulos = Math.min(tabelaPulos[length - 1][0], tabelaPulos[length - 1][1]);

    return minPulos != LIM ? minPulos : -1;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System. in ));
    String line = br.readLine();
    String[] inputs = line.split(" ");
    int N = Integer.parseInt(inputs[0]);
    int margem = Integer.parseInt(inputs[1]);

    int caminho[] = new int[N + 2];
    caminho[0] = 1;
    caminho[N + 1] = margem;

    inputs = br.readLine().split(" ");
    for (int i = 1; i <= N; i++) {
      caminho[i] = Integer.parseInt(inputs[i - 1]);
    }

    inputs = br.readLine().split(" ");

    int limCurto = Integer.parseInt(inputs[0]);
    int limLongo = Integer.parseInt(inputs[1]);

    System.out.println(puloSapo(caminho, limCurto, limLongo));
  }
}