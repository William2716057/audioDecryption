import wave
import numpy as np

def decode_audio(audio_file):
    audio = wave.open(audio_file, mode='rb')
    
    #Read frames and convert to byte array
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    #Extract the least significant bit of each byte
    extracted_bits = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    
    #Convert byte array back to string
    message_bits = "".join(map(str, extracted_bits))
    message = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
    
    #Convert from bits to characters
    decoded_message = "".join([chr(int(char, 2)) for char in message])
    
    #Remove padding
    decoded_message = decoded_message.split("###")[0]
    
    audio.close()
    print("Decoded message: " + decoded_message)
    
decode_audio('output.wav')