from kafka import KafkaConsumer
import json

# consumer = KafkaConsumer(
#     "calls",
#     bootstrap_servers="localhost:9092",
#     value_deserializer=lambda m: json.loads(m.decode('utf-8'))
# )

consumer = KafkaConsumer(
    "calls",
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',   # 👈 CLAVE
    enable_auto_commit=True,
    group_id="test-group",          # 👈 CLAVE
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando mensajes...")

for msg in consumer:
    print("Procesando:", msg.value)