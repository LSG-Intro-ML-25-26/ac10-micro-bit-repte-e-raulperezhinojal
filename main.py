# --- VARIABLES GLOBALS ---
# mode 0 = En espera
# mode 1 = Estació Meteorològica (Gràfic Temperatura)
# mode 2 = Moure la Gota (Acceleròmetre)
mode_seleccionat = 0

# Coordenades inicials de la gota (centre de la pantalla)
gota_x = 2
gota_y = 2

# --- FUNCIONS DEL MENÚ (BOTONS) ---
def on_button_pressed_a():
    global mode_seleccionat
    mode_seleccionat = 1
    basic.clear_screen()
    basic.show_string("T") # "T" de Temperatura

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global mode_seleccionat, gota_x, gota_y
    mode_seleccionat = 2
    # Reiniciem la posició de la gota al centre quan canviem de mode
    gota_x = 2
    gota_y = 2
    basic.clear_screen()
    basic.show_string("G") # "G" de Gota

input.on_button_pressed(Button.B, on_button_pressed_b)

# --- FUNCIÓ REPTE 6: ESTACIÓ METEOROLÒGICA ---
def executar_termometre():
    # Pinta un gràfic de barres basat en la temperatura
    # El valor màxim és 50 com indica el PDF [cite: 11]
    led.plot_bar_graph(input.temperature(), 50)
    # Petita pausa per no saturar la pantalla
    basic.pause(100)

# --- FUNCIÓ REPTE 7: MOURE LA GOTA ---
def executar_gota():
    global gota_x, gota_y
    
    # 1. Encenem el LED en la posició actual [cite: 45]
    led.plot(gota_x, gota_y)
    basic.pause(50)
    
    # 2. Apaguem el LED per crear l'efecte de moviment [cite: 46]
    led.unplot(gota_x, gota_y)
    
    # 3. Llegim l'acceleròmetre
    acc_x = input.acceleration(Dimension.X)
    acc_y = input.acceleration(Dimension.Y)
    
    # 4. Lògica de moviment eix X (Esquerra/Dreta)
    # Si inclinem a l'esquerra (< -150) i no estem a la vora (x > 0)
    if acc_x < -150 and gota_x > 0:
        gota_x -= 1
    # Si inclinem a la dreta (> 150) i no estem a la vora (x < 4)
    elif acc_x > 150 and gota_x < 4:
        gota_x += 1
        
    # 5. Lògica de moviment eix Y (Amunt/Avall)
    # Si inclinem endavant (< -150) i no estem a dalt (y > 0)
    if acc_y < -150 and gota_y > 0:
        gota_y -= 1
    # Si inclinem endarrere (> 150) i no estem a baix (y < 4)
    elif acc_y > 150 and gota_y < 4:
        gota_y += 1

# --- BUCLE PRINCIPAL (FOREVER) ---
def on_forever():
    if mode_seleccionat == 1:
        executar_termometre()
    elif mode_seleccionat == 2:
        executar_gota()
    else:
        # Si no s'ha triat cap mode, mostrem una icona d'espera
        basic.show_icon(IconNames.HAPPY)

basic.forever(on_forever)