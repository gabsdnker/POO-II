public public class Motorista extends Pessoa {
    private String numeroCNH;

    // Construtor
    public Motorista(String nome, String telefone, String numeroCNH) {
        super(nome, telefone);
        this.numeroCNH = numeroCNH;
    }

    // Getter e Setter para o atributo específico
    public String getNumeroCNH() {
        return numeroCNH;
    }

    public void setNumeroCNH(String numeroCNH) {
        this.numeroCNH = numeroCNH;
    }
}

