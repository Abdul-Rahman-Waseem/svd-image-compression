
# Original file is located at
#    https://colab.research.google.com/drive/1gFOLz1LHpycwN3XitoogdIU36Z2MX3WY

import cv2
import numpy as np
import matplotlib.pyplot as plt

def compress_channel(channel, k):
    """Apply SVD and reconstruct channel with top-k singular values."""
    U, S, VT = np.linalg.svd(channel, full_matrices=False)
    S_k = np.diag(S[:k])
    U_k = U[:, :k]
    VT_k = VT[:k, :]
    compressed = np.dot(U_k, np.dot(S_k, VT_k))
    return np.clip(compressed, 0, 255).astype('uint8')

def compress_color_image(img, k):
    """Compress a color image using SVD on each channel."""
    B, G, R = cv2.split(img)
    B_compressed = compress_channel(B, k)
    G_compressed = compress_channel(G, k)
    R_compressed = compress_channel(R, k)
    return cv2.merge([B_compressed, G_compressed, R_compressed])

def compressed_size(m, n, k):
    """Calculate number of values in compressed image."""
    return 3 * k * (m + n + 1)

# Load and resize image
image = cv2.imread('image.png')
image_resized = cv2.resize(image, (400, 400))
m, n, _ = image_resized.shape

original_size = 3 * m * n  # RGB image = 3 channels

# Prepare to plot
plt.figure(figsize=(15, 10))
original_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.imshow(original_rgb)
plt.title(f'Original\nSize: {original_size} values')
plt.axis('off')

# k values from high to low
ks = [150, 100, 50, 20, 5]

plt.figure(figsize=(15, 10))

# Show original image first
original_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.subplot(2, 3, 1)
plt.imshow(original_rgb)
plt.title(f'Original\nSize: {original_size} values')
plt.axis('off')

# Show compressed versions
for i, k in enumerate(ks):
    compressed_img = compress_color_image(image_resized, k)
    compressed_rgb = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2RGB)
    size = compressed_size(m, n, k)

    plt.subplot(2, 3, i + 2)
    plt.imshow(compressed_rgb)
    plt.title(f'k = {k}\nCompressed size: {size} values')
    plt.axis('off')

plt.tight_layout()
plt.show()

