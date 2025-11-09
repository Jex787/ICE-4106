def encode_hamming(data):
    d3, d5, d6, d7 = map(int, data)
    # Calculate parity bits (even parity)
    p1 = (d3 + d5 + d7) % 2
    p2 = (d3 + d6 + d7) % 2
    p4 = (d5 + d6 + d7) % 2
    return f"{p1}{p2}{d3}{p4}{d5}{d6}{d7}"

def detect_and_correct(received):
    bits = list(map(int, received))
    # Syndrome calculation
    s1 = (bits[0] + bits[2] + bits[4] + bits[6]) % 2
    s2 = (bits[1] + bits[2] + bits[5] + bits[6]) % 2
    s4 = (bits[3] + bits[4] + bits[5] + bits[6]) % 2
    error_pos = s1 * 1 + s2 * 2 + s4 * 4

    if error_pos:
        print(f"Error detected at position {error_pos}. Correcting it.")
        bits[error_pos - 1] ^= 1  # Flip the erroneous bit
        return "Error detected and corrected", bits
    return "No error detected", bits

# ----------- Example Usage -----------
data_bits = "1011"
print(f"Data: {data_bits}")

encoded = encode_hamming(data_bits)
print(f"Encoded Data: {encoded}")

received = "0110111"  # Simulate a transmission error at bit 5
print(f"Received Data (with error): {received}")

status, corrected = detect_and_correct(received)
print(status)
print(f"Corrected Data: {''.join(map(str, corrected))}")