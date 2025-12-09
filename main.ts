//  --- VARIABLES GLOBALS ---
//  mode 0 = En espera
//  mode 1 = Estació Meteorològica (Gràfic Temperatura)
//  mode 2 = Moure la Gota (Acceleròmetre)
let mode_seleccionat = 0
//  Coordenades inicials de la gota (centre de la pantalla)
let gota_x = 2
let gota_y = 2
//  --- FUNCIONS DEL MENÚ (BOTONS) ---
//  "T" de Temperatura
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    mode_seleccionat = 1
    basic.clearScreen()
    basic.showString("T")
})
//  "G" de Gota
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    mode_seleccionat = 2
    //  Reiniciem la posició de la gota al centre quan canviem de mode
    gota_x = 2
    gota_y = 2
    basic.clearScreen()
    basic.showString("G")
})
//  --- FUNCIÓ REPTE 6: ESTACIÓ METEOROLÒGICA ---
function executar_termometre() {
    //  Pinta un gràfic de barres basat en la temperatura
    //  El valor màxim és 50 com indica el PDF [cite: 11]
    led.plotBarGraph(input.temperature(), 50)
    //  Petita pausa per no saturar la pantalla
    basic.pause(100)
}

//  --- FUNCIÓ REPTE 7: MOURE LA GOTA ---
function executar_gota() {
    
    //  1. Encenem el LED en la posició actual [cite: 45]
    led.plot(gota_x, gota_y)
    basic.pause(50)
    //  2. Apaguem el LED per crear l'efecte de moviment [cite: 46]
    led.unplot(gota_x, gota_y)
    //  3. Llegim l'acceleròmetre
    let acc_x = input.acceleration(Dimension.X)
    let acc_y = input.acceleration(Dimension.Y)
    //  4. Lògica de moviment eix X (Esquerra/Dreta)
    //  Si inclinem a l'esquerra (< -150) i no estem a la vora (x > 0)
    if (acc_x < -150 && gota_x > 0) {
        gota_x -= 1
    } else if (acc_x > 150 && gota_x < 4) {
        //  Si inclinem a la dreta (> 150) i no estem a la vora (x < 4)
        gota_x += 1
    }
    
    //  5. Lògica de moviment eix Y (Amunt/Avall)
    //  Si inclinem endavant (< -150) i no estem a dalt (y > 0)
    if (acc_y < -150 && gota_y > 0) {
        gota_y -= 1
    } else if (acc_y > 150 && gota_y < 4) {
        //  Si inclinem endarrere (> 150) i no estem a baix (y < 4)
        gota_y += 1
    }
    
}

//  --- BUCLE PRINCIPAL (FOREVER) ---
basic.forever(function on_forever() {
    if (mode_seleccionat == 1) {
        executar_termometre()
    } else if (mode_seleccionat == 2) {
        executar_gota()
    } else {
        //  Si no s'ha triat cap mode, mostrem una icona d'espera
        basic.showIcon(IconNames.Happy)
    }
    
})
