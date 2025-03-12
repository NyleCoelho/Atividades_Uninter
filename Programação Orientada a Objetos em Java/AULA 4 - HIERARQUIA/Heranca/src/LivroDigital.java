public class LivroDigital extends Livro {
    public String linkDownload;
    public int tamanhoMB;

    public LivroDigital(String titulo, String autor, String linkDownload) {
        super(titulo,autor);
    }

    public float imposto() {
        return super.imposto() + 2;
    }

    public float tamanhoPorPagina() {
        return tamanhoMB/(float)paginas;
    }

    public void imprimeImposto() {
        System.out.println("Imposto livro físico: " + super.imposto());
        System.out.println("Imposto livro digital: " + this.imposto());
    }
}
