import cv2
import os

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

    print(f"Transmitiendo {len(frames)} tramas en bucle continuo...")
    print("Presiona 'q' en esta ventana para detener.")
    
    while True:
        for index, frame in enumerate(frames):
            # --- LA CORRECCIÓN VISUAL ---
            # Reducimos la imagen a 600x600 para que no se corte con la barra de tareas
            frame_escalado = cv2.resize(frame, (600, 600))
            
            cv2.imshow("Transmisor VLC", frame_escalado)
            
            # Cambia de imagen cada 1000 milisegundos (1 segundo)
            if cv2.waitKey(1000) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                exit()
