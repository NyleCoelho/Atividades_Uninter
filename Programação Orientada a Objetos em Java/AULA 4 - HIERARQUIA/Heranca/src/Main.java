public class Main {
    public static void main(String[] args) {
        Livro l1 = new Livro("Sherlock Holmes", "Conan Doyle");
        LivroDigital l2 = new LivroDigital("Orgulho e Preconceito", "Jane Austen", "linkGenerico.com");

        l2.imposto();
        l1.imposto();;

        System.out.println(l1 instanceof Livro);
        System.out.println(l2 instanceof Livro);
        System.out.println(l1 instanceof LivroDigital);
        System.out.println(l2 instanceof LivroDigital);

    }
}