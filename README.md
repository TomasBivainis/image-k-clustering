# 🎨 Image Color Quantizer (K-Means Color Reduction)

This project takes any input image and **reduces its color palette** to _k representative colors_ using **K-Means clustering**.
It then recolors the entire image so that every pixel is replaced by the **nearest cluster color**, producing a simplified, stylized version of the original.

---

## 🚀 Features

- 🧠 Uses **K-Means clustering** to find dominant colors in an image.
- 🎨 Reconstructs the image using only those _k_ colors.
- 📊 Supports adjustable `k` (number of colors).
- 💾 Saves both the **quantized image** and optionally a **palette preview**.
- ⚡ Works with most common image formats (PNG, JPG, etc.).

---

## 🧰 Tech Stack

- **Python 3.x**
- **NumPy** — fast numerical computation
- **scikit-learn** — KMeans clustering
- **Pillow (PIL)** — image processing
- **matplotlib** _(optional)_ — for displaying images and color palettes

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/image-color-quantizer.git
cd image-color-quantizer
pip install -r requirements.txt
```

Example `requirements.txt`:

```
numpy
scikit-learn
pillow
matplotlib
```

---

## 🖼️ Usage

Basic command-line usage:

```bash
python color_quantizer.py --input input.jpg --k 8 --output output.jpg
```

### Arguments

| Flag       | Description                   | Default         |
| ---------- | ----------------------------- | --------------- |
| `--input`  | Path to the input image       | _required_      |
| `--output` | Path to save the output image | `quantized.png` |
| `--k`      | Number of clusters (colors)   | `8`             |
| `--show`   | Show before/after comparison  | `False`         |

---

## 🔍 Example

Input:
![Original Image](examples/original.jpg)

Output (k=6):
![Quantized Image](examples/quantized.jpg)

Palette (optional):
![Palette](examples/palette.png)

---

## 🧪 How It Works

1. Load the image and reshape its pixels into a 2D array of RGB values.
2. Run **K-Means clustering** to group pixels into _k_ clusters.
3. Replace each pixel’s color with the centroid of its assigned cluster.
4. Reshape and save the new quantized image.

---

## 🎯 Applications

- Image compression and simplification
- Artistic effects (posterization, stylization)
- Color palette extraction
- Data visualization or color analysis

---

## 🛠️ Future Improvements

- Add GPU acceleration with CuML or PyTorch
- Implement median-cut quantization for comparison
- Interactive web demo using Streamlit or Gradio

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Example Output

| Original                   | Quantized (k=4)      | Quantized (k=8)      |
| -------------------------- | -------------------- | -------------------- |
| ![](examples/original.jpg) | ![](examples/k4.jpg) | ![](examples/k8.jpg) |

---
