//Observer pattern
interface Subject{
    public void registerObserver(Observer o);
    public void removeObserver(Observer o);
    public void notifyObservers();
}

interface Observer{
    public void update(float temp,float humidity, float pressure);
    
}

interface DisplayElement{
    public void display();
}

class WeatherData implements Subject{

    private ArrayList<Observer> observer;
    private float temperature;
    private float pressure;
    private float humidity;

    public WeatherData(){
        observer=new ArrayList<Observer>();
    }

    public void registerObserver(Observer o){
        observer.add(o);
    }

    public void removeObserver(Observer o){
        int i= observer.indexof(o);
        if(i>=0){
            observer.remove(o);
        }
    }

    public void notifyObservers(){
        for (Observer o: observer){
            o.update(temperature,humidity,pressure);
        }
    }

    public void measurementChanges(){
        notifyObservers();
    }

    public void setMeasurements(float temperature,float humidity,float pressure){
        this.temperature=temperature;
        this.humidity=humidity;
        this.pressure=pressure;
        measurementChanges();
    }
}

class CurrentConditions implements Observer,DisplayElement{
    private float temperature;
    private float humidity;
    private Subject WeatherData;
    public CurrentConditions(Subject WeatherData){
        this.WeatherData=WeatherData;
        WeatherData.registerObserver(this);
    }

    public void update(float temperature,float humidity,float pressure){
        this.temperature=temperature;
        this.humidity=humidity;
        this.pressure=pressure;
        display();
    }

    public void display(){
        System.out.println(temperature);
    }
}

public class ObserverPattern{
    public static void main(String[] args){
        WeatherData weatherdata=new WeatherData();
        CurrentConditions currentConditions=new CurrentConditions(weatherdata);
        weatherdata.setMeasurements(80,60,45);
    }
