import cv2
import numpy as np
import pyautogui
import pytesseract
import time
import os
import psutil
from datetime import datetime

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Pasta para salvar os highlights
SAVE_DIR = "highlights"
os.makedirs(SAVE_DIR, exist_ok=True)

# Palavras que indicam highlight
HIGHLIGHT_KEYWORDS = ["ACE", "CLUTCH"]

# Configuração de captura
BUFFER_SECONDS = 30   # tempo de gravação antes do highlight
fps = 5
buffer_size = BUFFER_SECONDS * fps
frame_buffer = []

def is_valorant_running():
    """Verifica se o processo do Valorant está ativo"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and "VALORANT" in proc.info['name'].upper():
            return True
    return False

print("Highlight Tracker v2 iniciado... (pressione CTRL+C para parar)")

try:
    while True:
        # Verificar se Valorant está aberto
        if not is_valorant_running():
            print("⚠️ Valorant não está em execução. Aguardando...")
            time.sleep(5)
            continue

        # Capturar tela
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Adicionar frame ao buffer
        frame_buffer.append(frame)
        if len(frame_buffer) > buffer_size:
            frame_buffer.pop(0)

        # Pré-processar imagem para OCR
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]
        text = pytesseract.image_to_string(gray, config='--psm 6').upper()

        # Verificar palavras-chave
        if any(keyword in text for keyword in HIGHLIGHT_KEYWORDS):
            print("🔎 Possível highlight detectado, confirmando...")
            time.sleep(0.8)

            # Segunda leitura para confirmar
            screenshot2 = pyautogui.screenshot()
            frame2 = np.array(screenshot2)
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.threshold(gray2, 180, 255, cv2.THRESH_BINARY)[1]
            text2 = pytesseract.image_to_string(gray2, config='--psm 6').upper()

            # Confirmar highlight
            if any(keyword in text2 for keyword in HIGHLIGHT_KEYWORDS):
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(SAVE_DIR, f"highlight_{timestamp}.mp4")
                print(f" Highlight confirmado ({timestamp})! Salvando clipe...")

                # Salvar clipe
                height, width, _ = frame_buffer[0].shape
                out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
                for f in frame_buffer:
                    out.write(f)
                out.release()

                print(f" Highlight salvo em: {filename}")
                frame_buffer.clear()
                time.sleep(5)  # evitar detecção duplicada
            else:
                print("❌ Falso positivo ignorado.")

        time.sleep(1 / fps)

except KeyboardInterrupt:
    print("\n🛑 Programa encerrado.")
