import cv2
from picamera2 import Picamera2
import time

def test_camera_opencv():
    print("Iniciando prueba de cámara con Picamera2 y OpenCV...")

    # Inicializa Picamera2
    # El tamaño de la resolución se especifica como un tuple (ancho, alto)
    # El formato 'RGB888' es un formato común que OpenCV puede entender directamente
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"})
    picam2.configure(camera_config)

    try:
        picam2.start()
        print("Cámara iniciada. Presiona 'q' para salir.")
    except Exception as e:
        print(f"\033[31mError al iniciar la cámara:\033[0m {e}")
        print("\nPosibles causas:")
        print("  - Asegúrate de que la cámara esté bien conectada.")
        print("  - En 'sudo raspi-config', ve a '3 Interface Options' -> 'P1 Camera'")
        print("    y ASEGÚRATE de que la opción 'Legacy Camera' esté DESACTIVADA para usar Picamera2.")
        print("  - Asegúrate de tener 'picamera2' y 'opencv-python' instalados.")
        return

    # Bucle principal para capturar y mostrar frames
    while True:
        # Captura un array numpy directamente desde Picamera2
        frame = picam2.capture_array()

        if frame is None:
            print("No se pudo capturar un fotograma. Asegúrate de que la cámara esté activa.")
            time.sleep(0.1)
            continue

        # Muestra el fotograma en una ventana llamada "Camera Test"
        cv2.imshow("Camera Test", frame)

        # Espera 1 ms y verifica si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cuando el bucle termina, libera la cámara y cierra todas las ventanas
    picam2.stop()
    cv2.destroyAllWindows()
    print("Prueba de cámara finalizada.")

if __name__ == "__main__":
    test_camera_opencv()
