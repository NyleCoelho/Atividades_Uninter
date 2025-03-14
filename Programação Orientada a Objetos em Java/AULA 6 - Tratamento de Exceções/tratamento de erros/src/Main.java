public class Main {
    public static void main(String[] args) {
        int[] numeros = {1,2,3};

        try {
            System.out.println(numeros[10]);
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Fora do limite!");
            return;
        }
        catch (Exception e) {
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }
        finally {
            System.out.println("Finalizando programa!");
        }

    }
}