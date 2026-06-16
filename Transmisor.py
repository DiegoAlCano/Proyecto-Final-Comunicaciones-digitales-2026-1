import cv2
import os
import numpy as np # Requerido para crear la matriz de fondo negro

if __name__ == "__main__":
    # Carga automáticamente todas las imágenes PNG que generó la Fase A
    frames = []
    i = 0
    while os.path.exists(f"frame_{i}.png"):
        frames.append(cv2.imread(f"frame_{i}.png"))
        i += 1

    if not frames:
        print("No se encontraron frames. Ejecuta FaseA.py primero.")
        exit()

    num_frames = len(frames) # Cantidad de frames generados para el texto 
    tiempo_frame_ms = int((10 / num_frames) * 1000) # tiempo para cada frame distribuido uniformemente

    print(f"Transmitiendo {num_frames} tramas en bucle continuo...")
    print("Presiona 'q' en la ventana de transmisión para detener.")
    
    cv2.namedWindow("Transmisor VLC", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Transmisor VLC", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        for index, frame in enumerate(frames):
            
            frame_puro = frame # Conservamos la resolución original 800x800 de Fase A
            
            # Crear fondo negro
            resolucion_pantalla_ancho = 1920
            resolucion_pantalla_alto = 1080
            pantalla_completa = np.zeros((resolucion_pantalla_alto, resolucion_pantalla_ancho, 3), dtype=np.uint8)
            
            # Calcular offset para 800x800
            x_offset = (resolucion_pantalla_ancho - 800) // 2
            y_offset = (resolucion_pantalla_alto - 800) // 2
            pantalla_completa[y_offset:y_offset+800, x_offset:x_offset+800] = frame_puro
            
            cv2.imshow("Transmisor VLC", pantalla_completa)
            
            if cv2.waitKey(tiempo_frame_ms) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit()
