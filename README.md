# pygame_kodland

## Instrucciones para ejecutar el juego

1. **Instala los requisitos**  
   Abre una terminal en la carpeta del proyecto y ejecuta:

```pip install -r requirements.txt```

2. **Ejecuta el juego**  
Luego, ejecuta el archivo principal:

```python main.py```

---

## Hablemos sobre Conquistador

### **¿Cómo funciona el juego?**

El juego es un arcade donde eres un conquistador que debe sobrevivir el mayor tiempo posible esquivando enemigos y usando pociones para cambiar su tamaño. El objetivo es obtener la mayor puntuación posible mientras la dificultad aumenta progresivamente.

#### **Flujo general:**
- Al iniciar, se muestra un menú principal con el nombre del juego y dos opciones: comenzar (`ESPACIO`) o ver el tutorial (`T`).
- Si eliges el tutorial, aparece una ventana modal con varias diapositivas que explican la historia, los enemigos y las pociones.
- Al comenzar el juego, controlas al jugador con las flechas izquierda y derecha.
- Enemigos de diferentes tipos aparecen y debes esquivarlos.
- Cada cierto puntaje aparecen pociones azules y rojas que modifican el tamaño del jugador.
- Puedes pausar el juego en cualquier momento con `ESC`, mostrando un menú de pausa con opciones para continuar (`G`) o reiniciar (`R`).
- Si colisionas con un enemigo, aparece la pantalla de fin de juego, mostrando tu puntaje y la opción de reiniciar.

---

### **Funciones personalizadas implementadas**

El código está modularizado en varios archivos, cada uno con funciones específicas:

- **game_objects.py:**  
  - `spawn_enemy`: Genera enemigos según el puntaje y la dificultad.
  - `move_enemies`: Mueve a los enemigos por la pantalla.
  - `check_collision`: Detecta colisiones entre el jugador y los enemigos.
  - `spawn_potion`, `move_potions`, `check_potion_collision`: Gestionan la aparición, movimiento y colisión de pociones.

- **ui.py:**  
  - `draw_menu`: Dibuja el menú principal.
  - `draw_game`: Dibuja el estado del juego (jugador, enemigos, pociones, puntaje, pausa).
  - `game_over_screen`: Muestra la pantalla de fin de juego.
  - `draw_tutorial` y `show_tutorial`: Gestionan la ventana modal del tutorial con navegación por diapositivas.
  - `draw_pause_menu` y `pause_menu`: Implementan el menú de pausa en medio de la partida.

- **assets.py:**  
  - Carga y escala las imágenes de los avatares y define la fuente usada en los textos.

- **settings.py:**  
  - Define constantes globales como dimensiones de la ventana, colores y tamaño de los avatares.

---

### **Menús implementados**

1. **Menú principal:**  
- Permite iniciar el juego o acceder al tutorial.
- Se navega con `ESPACIO` (comenzar) o `T` (tutorial).

2. **Tutorial modal:**  
- Ventana superpuesta con fondo semitransparente.
- Tres diapositivas: historia, explicación de enemigos y explicación de pociones.
- Navegación con flechas izquierda/derecha y cierre con `T`.

3. **Menú de pausa:**  
- Se activa con `ESC` durante la partida.
- Opciones: continuar (`G`) o reiniciar (`R`).

4. **Pantalla de fin de juego:**  
- Muestra el puntaje final y permite reiniciar con `R`.

---

### **Enemigos en el juego**

El juego cuenta con tres tipos de enemigos, cada uno con comportamiento y dificultad distinta:

- **Enemigo Uno ("Euler"):**  
  - Aparece entre el puntaje 0 y 2000.
  - Movimiento vertical, velocidad baja.

- **Enemigo Dos ("Gauss"):**  
  - Aparece entre 2000 y 4000 puntos.
  - Movimiento diagonal, velocidad media (más lenta que antes por ajuste).
  - Aumenta la cantidad a medida que sube el puntaje.

- **Enemigo Tres ("Newton"):**  
  - Aparece entre 4000 y 5500 puntos.
  - Movimiento vertical o diagonal, velocidad variable y más impredecible.
  - Menor cantidad en pantalla para equilibrar la dificultad.

- **A partir de 5500 puntos:**  
  - Se combinan los tres tipos de enemigos en pantalla, aumentando la dificultad máxima.

---

### **Pociones**

- **Poción azul:**  
  - Reduce el tamaño del jugador en un 8%, facilitando esquivar enemigos.
- **Poción roja:**  
  - Aumenta el tamaño del jugador en un 8%, dificultando el juego.
- Las pociones aparecen alternadamente cada 300 puntos (azul, luego roja 15 puntos después).

---

**¡Disfruta del juego!**

