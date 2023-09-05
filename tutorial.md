## Svingningsmåleren! 
Nu skal vi sammen bygge en måler til at registrere svingninger. 

* ! OBS ! Du skal bruge en @boardname@ mindst V2 for at denne kode kan virke. ! OBS !
* Følg med her, så er koden klar om lidt! :-) 
* Du kan eventuelt se videoen [her](http://example.com "testvideoen") for en gennemgang af denne tutorial.

## Slet de to blå blokke
Start med at slette de to blå blokke, der er på skærmen: "når programmet starter" og "for altid".

## Installer datalogger udvidelsen
Som det første installerer vi udvidelsen "datalogger". Du finder den ved at trykke på "Udvidelser +". Herunder vælger du 

```blocks
datalogger.log(datalogger.createCV("", null))
```

```blocks
basic.forever(function () {
    if (datalogningSand) {
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


let datalogningSand = 0
input.onButtonPressed(Button.A, function () {
    datalogningSand = 1
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onButtonPressed(Button.AB, function () {
    datalogger.deleteLog()
    basic.pause(100)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . # #
        `)
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
        . . # . .
        . . . . .
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
    if (datalogningSand) {
        datalogningSand = 0
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
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
    if (datalogningSand) {
        datalogger.log(
        datalogger.createCV("Tid", input.runningTime() % 1000),
        datalogger.createCV("Acceleration", input.acceleration(Dimension.X))
        )
        basic.pause(100)
    }
})
