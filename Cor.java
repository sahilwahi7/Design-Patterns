//chain of responsiblities pattern in java

abstract class Handler{
    public Handler set_next(Handler handler){};
    public String handler(String request){};
}

abstract class AbstarctHandler extends Handler{
    private Handler=null
    public Handler set_next(Handler handler){
        this.handler=Handler;
        return handler;
    }

    public String handler(String request){
        if(Handler!=null){
            Handler.handler(request);
        }
    }

}

class BasicAuthenticator extends AbstarctHandler{
    @Override
    public String handler(String request){
        if request.equals("basic"){
            System.out.println("Request is autherizoed for basic...");
        }
        else{
            super().handler(request);
        }

    }
}

class AdvancedAuthenticator extends AbstarctHandler{
    @Override
    public String handler(String request){
        if request.equals("advanced"){
            System.out.println("Request is autherizoed for advanced...");
        }
        else{
            super().handler(request);
        }

    }
}

class SupremeAuthenticator extends AbstarctHandler{
    @Override
    public String handler(String request){
        if request.equals("supreme"){
            System.out.println("Request is autherizoed for supreme...");
        }
        else{
            super().handler(request);
        }

    }
}

public class Cor{
    public static void main( String[] args){
        basic=BasicAuthenticator();
        supreme=SupremeAuthenticator();
        advanced=AdvancedAuthenticator();
        supreme.set_next(advanced).set_next(basic);
        supreme.handle("basic");
        supreme.handle("advanced");

    }
}
