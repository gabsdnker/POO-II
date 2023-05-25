 //Exercício E6:
//a) criar uma classe em Java, com pelo menos um método e dois atributos
//b) fazer a geração do arquivo .jar (implantável); fazer a documentação do conteúdo do arquivo .jar (classe, métodos, atributos)
//c) criar um programa em java que utilize o .jar que outro colega fez
//Os dois programas devem estar disponíveis na sua resposta (o seu programa java e o .jar que você utilizou, referenciado)

public class MyClass {
    private int attribute1;
    private String attribute2;

    public MyClass(int attribute1, String attribute2) {
        this.attribute1 = attribute1;
        this.attribute2 = attribute2;
    }

    public void myMethod() {
        System.out.println("Hello, World!");
    }

    public int getAttribute1() {
        return attribute1;
    }

    public String getAttribute2() {
        return attribute2;
    }
}

//Compile a classe Java usando o comando javac no terminal:
//javac MyClass.java

//Crie um arquivo de manifesto Manifest.txt que especifica a classe principal a ser executada:
//Main-Class: MyClass

//Crie o arquivo .jar usando o comando jar no terminal:
//jar cvfm MyClass.jar Manifest.txt MyClass.class


//7) Pergunta: seria possível usar reflexão para "descobrir" (engenharia reversa) quais classes, métodos e atributos 
//existem no arquivo .jar que está disponibilizado?

//RESPOSTA: Sim, é possível usar reflexão em Java para "descobrir" as classes, métodos e atributos existentes no arquivo .jar 
//disponibilizado. Através da API de Reflexão em Java, é possível carregar e inspecionar dinamicamente as classes contidas no 
//arquivo .jar, obter informações sobre seus métodos e atributos, e até mesmo invocar esses métodos em tempo de execução.
