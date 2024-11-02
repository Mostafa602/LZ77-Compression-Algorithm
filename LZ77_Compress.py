def lz77_compress(data, window_size=12):
    compressed_data = []
    i = 0

    while i < len(data):
        match_length = 0
        match_distance = 0
        next_char = data[i]
			
				# Define the search window
        start_window = max(0, i - window_size)
        search_buffer = data[start_window:i]
				
				# Try to find the longest match
        for j in range(len(search_buffer)):
            length = 0
            while (length < len(data) - i and
                   search_buffer[j:j+length+1] == data[i:i+length+1]):
                length += 1
						
						# Update the best match if found
            if length >= match_length:
                match_length = length
                match_distance = len(search_buffer) - j
                if i + match_length < len(data):
                    next_char = data[i + match_length]
                else:
                    next_char = ''
				
				# Append (distance, length, next character) tuple
        if match_length > 0:
            compressed_data.append((match_distance, match_length, next_char))
            i += match_length + 1
        else:
            compressed_data.append((0, 0, next_char))
            i += 1

    return compressed_data
