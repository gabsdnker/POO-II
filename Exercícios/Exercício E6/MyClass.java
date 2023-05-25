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



