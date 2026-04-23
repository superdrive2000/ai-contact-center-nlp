import whisper

model = whisper.load_model("small")
result = model.transcribe("C:\\Users\\Lenovo i5\\Documents\\MAESTRIA IA YACHAY TECH\\DESPLIEGUE DE MODELOS A PRODUCCIÓN\\final project\\ai-contact-center\\data\\sample_calls\\Diana_Acaro.wav")

print(result["text"])