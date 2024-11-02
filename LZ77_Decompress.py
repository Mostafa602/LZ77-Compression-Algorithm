def lz77_decompress(compressed_data):
    
    decompressed_data = []
    
    for offset, length, next_character in compressed_data:
        if offset == 0 and length == 0:
            decompressed_data.append(next_character)
        else:
            start = len(decompressed_data) - offset
            for i in range(length):
                decompressed_data.append(decompressed_data[start + i])
            decompressed_data.append(next_character)
    
    return ''.join(decompressed_data)
