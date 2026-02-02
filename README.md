# 🖼️ Image Compression using Singular Value Decomposition (SVD)

This project demonstrates **image compression using Singular Value Decomposition (SVD)**, a core concept of **Linear Algebra**, applied to digital images. By keeping only the most significant singular values, the image size is reduced while maintaining acceptable visual quality.

---

## 🎓 Academic Information

- **University:** Air University, Islamabad  
- **Course:** Linear Algebra (MA201)  
- **Instructor:** Dr. Ambreen Khan  
- **Section:** BSSE-4-A  

**Developed By:**  
**Abdul Rahman Waseem**  
Reg No: **232011**

---

## 📘 Project Overview

Singular Value Decomposition factorizes a matrix as:

A = U · S · Vᵀ

In image processing:
- An image is treated as a matrix of pixel intensities
- A color image consists of three matrices (Red, Green, Blue)
- SVD is applied independently to each channel
- Only the top **k singular values** are retained for reconstruction

This results in:
- Reduced storage requirements
- Minimal visual information loss
- Efficient image representation

---

## 🧠 Working Principle

1. Load a color image
2. Resize the image to 400 × 400
3. Split image into B, G, R channels
4. Apply SVD on each channel
5. Reconstruct channels using top **k** singular values
6. Merge channels to form the compressed image
7. Display original and compressed images for comparison

---

## 📐 Compression Example

For a **400 × 400 RGB image**:

Original size:
3 × 400 × 400 = 480,000 values

Compressed size (k = 50):
3 × 50 × (400 + 400 + 1) = 120,150 values

This reduces the data size to approximately **25%** of the original while preserving most visual details.

---

## 🧪 Results

The output includes:
- Original image
- Compressed images using different values of **k**
  - k = 150
  - k = 100
  - k = 50
  - k = 20
  - k = 5

Lower values of **k** result in higher compression but noticeable quality degradation.

---

## 🛠️ Tech Stack

- Python
- NumPy
- OpenCV (cv2)
- Matplotlib

---

## 📂 Project Structure

├── image.png  
├── svd_compression.py  
├── README.md  

---

## ▶️ How to Run

1. Clone the repository:
   git clone https://github.com/your-username/image-compression-svd.git

2. Install dependencies:
   pip install numpy opencv-python matplotlib

3. Place your image as `image.png`

4. Run the script:
   python svd_compression.py

---

## 📌 Applications

- Image compression
- Efficient storage and transmission
- Noise reduction
- Computer vision preprocessing
- Educational demonstration of SVD

---

## 🤝 Contributions

Suggestions and improvements are welcome.  
Feel free to open an issue or submit a pull request.

---

## 📬 Contact

Email: look4rahman@gmail.com  
LinkedIn: Abdul Rahman Waseem  

⭐ If you find this project useful, consider starring the repository!

