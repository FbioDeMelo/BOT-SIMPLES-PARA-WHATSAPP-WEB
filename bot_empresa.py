import pywhatkit
import pyautogui
import time
from datetime import datetime

numeros = [
    '', #Adição de Numeros
]

mensagem = """
"""

print("Iniciando o envio de mensagens...")
print("ATENÇÃO: Não mexa no mouse ou teclado enquanto o script estiver rodando.")
print("Mantenha a tela do WhatsApp Web aberta e logada.")

for i, numero in enumerate(numeros):
    try:
        print(f"Preparando envio para o {i+1}º número: {numero}")

        agora = datetime.now()
        hora = agora.hour
        minuto = agora.minute + 2

        if minuto >= 60:
            minuto -= 60
            hora += 1
        
        if hora >= 24:
            hora = 0

        print(f"Agendando envio para {hora:02d}:{minuto:02d}...")

        pywhatkit.sendwhatmsg(
            phone_no=numero,
            message=mensagem,
            time_hour=hora,
            time_min=minuto,
            wait_time=20
        )

        print(f"✅ Mensagem enviada para {numero}")
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')

        print("Aguardando 60 segundos antes de agendar o próximo envio...")
        time.sleep(60)

    except Exception as e:
        print(f"❌ Erro ao enviar para {numero}: {e}")
        time.sleep(45)

print("\n🎉 Envio concluído!")


