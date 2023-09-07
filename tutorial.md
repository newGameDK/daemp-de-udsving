## Svingningsmåleren! 
Nu skal vi sammen bygge en måler til at registrere svingninger. 

* **OBS! Du skal bruge en @boardname@ i mindst version 2 (V2) før denne kode virker** 
* Følg med her, så er koden klar om lidt! :-) 
* Du kan eventuelt se videoen [her](http://example.com "testvideoen") for en gennemgang af denne tutorial.

## Installer eventuelt datalogger udvidelsen
Dataloggeren er installeret i denne tutorial. Hvis du skal installere i dit eget program, en anden gang, finder den ved at trykke på:
* "Udvidelser +". 
* På den næste side, finder du muligheden "datalogger"

## Knapperne
Du skal bruge tre knapper i programmet. `|input.knap A|`, `|input.knap B|` og `|input.knap A+B|` (A og B trykket ind samtidigt) 

## Variabel 
Du skal nu oprette en variabel. Du kan kalde den `||variables:datalogning||`. Den fortæller programmet, om datalogning er tændt eller slukket. 

## Indsæt variablen 
Nu skal du sætte værdien af `||variables:datalogning||`. 
* Det gør du ved at trække knappen `||variables:sæt datalogning til||` ind under `||input.når der trykkes på knap A||`
* Sæt værdien af variablen datalogning til 1

```blocks
input.onButtonPressed(Button.A, function () {
    datalogning = 1
    
})
```

## Vis at datalogning er startet
* Træk et billede ind og lav et tegn for at datalogningen er startet. 
* Placér billedet under der hvor du sætter variablen `||variables:datalogning||`

```blocks
input.onButtonPressed(Button.A, function () {
    datalogning = 1
    basic.showLeds(`
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        `)
})
```

## Knap B - slukkeknappen
Knap B skal slukke for datalogningen. 
* Træk blokken `||variables:sæt datalogning til||` ind i blokken `|input.knap B|`
* Sæt værdien til 0
* Som du måske har gættet betyder 1 at datalogning er tændt, og 0 at datalogning er slukket.

## For altid
I blokken for altid, sker datalogningen. Her skal vi sætte op at den først spørger om variablen `||variables:datalogning||` er 1 eller 0. 
* Start med at trække en `||logic:hvis ... så||` ind i blokken `||basic:for altid||`
* Træk `||logic: 0 = 0 ||` ind i blokken `||logic:hvis ... så||` 
* Træk derefter variablen `||variables:datalogning||` ind i `||logic: 0 = 0 ||` blokken
* Skift værdien 0 til 1. På den måde spørger du nu om `||variables:datalogning||` = 1

```blocks
basic.forever(function () {
    if (datalogningStatus == 1) {

    }
})
```

## Start datalogning
Hvis `||variables:datalogning||` = 1 så skal datalogningen startes! 
* træk `||datalogger:log data||` ind i `||logic:hvis ... så||`
* Udfyld første kolonnetitel med navnet "Tid" 
* Udfyld value med `||input.køretid (ms)||`
* Tryk på + ikonet på `||datalogger:log data||`
* Udfyld første kolonnetitel med navnet "Acceleration" 
* Udfyld value med `||input.acceleration (styrke)||`
* Tjek at du under `||input.acceleration||` har valgt styrke i stedet for x 
 
```blocks
basic.forever(function () {
    if (datalogningStatus == 1) {
        datalogger.log(
        datalogger.createCV("Tid", input.runningTime() % 1000),
        datalogger.createCV("Acceleration", input.acceleration(Dimension.X))
        )
   
    }
})
```


## Indsæt en pause
```blocks
basic.forever(function () {
    if (datalogningStatus == 1) {
        datalogger.log(
        datalogger.createCV("Tid", input.runningTime() % 1000),
        datalogger.createCV("Acceleration", input.acceleration(Dimension.X))
        )
        basic.pause(100)
    }
})
```



 

## Tillykke!
Nu er du færdig med din kode. Du kan nu afprøve om du kan: 
* Let: Tjekke om den tæller rigtigt?
* Let: Undersøge hvor meget den skal rystes før den tæller
* Mellem: Hvorfor tror du den ikke tæller helt rigtigt?
* Mellem: Prøve at sætte flere @boardname@ på den samme person, forskellige steder på kroppen
* Svær: Bygge en holder til din @boardname@ skridttæller.
* Svær: Finde på noget andet at bruge programmet til? Fx. hvor mange gange en dør bliver åbnet og lukket?`
* Svær: Tænk over om der mon er noget sted på rumstationen hvor den virker?


let datalogningStatus = 0
input.onButtonPressed(Button.A, function () {
    datalogningStatus = 1
    basic.showLeds(`
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    datalogger.deleteLog()
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    if (datalogningStatus) {
        datalogningStatus = 0
        basic.showLeds(`
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
basic.forever(function () {
    if (datalogningStatus == 1) {
        datalogger.log(
        datalogger.createCV("Tid", input.runningTime() % 1000),
        datalogger.createCV("Acceleration", input.acceleration(Dimension.X))
        )
        basic.pause(100)
    }
})
