def read_ppm(filename):
  """Lê uma imagem PPM em formato bruto."""
  with open(filename, 'rb') as f:
    # Ignorar o cabeçalho PPM
    header = f.readline().strip()
    if header != b'P6':
      raise ValueError("Formato não suportado. Use imagens no formato P6.")
    dimensions = f.readline().strip()
    width, height = map(int, dimensions.split())
    max_val = int(f.readline().strip())
    if max_val != 255:
      raise ValueError("Somente valores máximos de 255 são suportados.")
    
    # Ler os pixels em formato binário
    pixel_data = f.read()
    return width, height, pixel_data

def write_ppm(filename, width, height, pixel_data):
  """Escreve uma imagem PPM no formato bruto."""
  with open(filename, 'wb') as f:
    # Cabeçalho PPM
    f.write(b'P6\n')
    f.write(f"{width} {height}\n".encode())
    f.write(b'255\n')
    # Dados dos pixels
    f.write(pixel_data)

def color_to_grayscale(pixel_data):
  """Converte pixels RGB para tons de cinza."""
  grayscale_data = bytearray()
  for i in range(0, len(pixel_data), 3):
    r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
    gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    grayscale_data.extend([gray, gray, gray])
  return grayscale_data

def grayscale_to_bw(grayscale_data, threshold=127):
  """Converte pixels em tons de cinza para preto e branco."""
  bw_data = bytearray()
  for i in range(0, len(grayscale_data), 3):
    gray = grayscale_data[i]
    bw_value = 255 if gray > threshold else 0
    bw_data.extend([bw_value, bw_value, bw_value])
  return bw_data

# Exemplo de uso
input_file = "animal.ppm"  # Certifique-se de que a imagem está no formato PPM (P6)
output_gray = "imagem_gray.ppm"
output_bw = "imagem_bw.ppm"

# 1. Ler a imagem original
width, height, pixel_data = read_ppm(input_file)

# 2. Converter para tons de cinza
gray_data = color_to_grayscale(pixel_data)
write_ppm(output_gray, width, height, gray_data)

# 3. Converter para preto e branco
bw_data = grayscale_to_bw(gray_data)
write_ppm(output_bw, width, height, bw_data)

print("Conversão concluída: imagem_gray.ppm e imagem_bw.ppm foram salvas.")
