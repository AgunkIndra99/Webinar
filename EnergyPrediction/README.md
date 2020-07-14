# Prediksi Energi Rumah Hunian
## Pendahuluan
Project ini terinspirasi karya yang telah dilakukan oleh [Luis Candanedo](https://github.com/LuisM78/Appliances-energy-prediction-data). 
Hasil akhir dari project ini adalah prediksi energi listrik dari suatu rumah hunian. Model dilatih menggunakan TensorFlow, dan model akhir akan ditanamkan pada Raspberry Pi dalam format TensorFlow Lite.

Dataset yang digunakan pada Proejct ini dapat diunduh melalui laman [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction). Namun demikian, dataset tersebut juga sudah disertakan dalam repositori ini.

## Langka-langkah
1. Sediakan papan Raspberry Pi, dan install-lah Python.
2. Buatlah virtual environment pada Raspi agar mempermudah organisasi kerja kita. Berikut [tutorialnya](http://raspberrypi-aa.github.io/session4/venv.html). 
3. Install-lah Pyhton versi 3.5 ke atas. Install pula pip. Berikut [tutorialnya](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). Setelah itu, install beberapa pustaka lain, yaitu numpy dan TFLite interpreter.
4. Install TensorFlow Lite Interpreter pada Raspberry PI. Saat ini saya pergunakan Raspi 3B. Usahakan gunakan Raspi versi 3 ke atas. Berikut [tutorialnya](https://www.tensorflow.org/lite/guide/python)
5. Unduh semua file dalam repositori ini.
6. Latih model. Jalankan program untuk membangun dan melatih model berikut [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kusuma86/Webinar/blob/master/EnergyPrediction/Train/Webinar_PrediksiEnergi.ipynb). Hasil dari program ini adalah model TensorFlow dan TensorFlow Lite. Lihat Folder [Pretrained](https://github.com/kusuma86/Webinar/tree/master/EnergyPrediction/Pretrained).
7. Jika Anda tidak dapat menyelesaikan langkah 1-6, maka langsunglah unduh file **modelEnergyPrediction.tflite** melalui halaman repositori ini. Hal ini dikarenakan tujuan akhir dari langkah-langkah di atas adalah untuk mendapatkan file modelEnergyPrediction.tflite ini, yang nantinya akan dieksekusi pada Raspberry Pi.
8. Tempatkan modelEnergyPrediction.tflite, data_x.csv, dan data_y.csv pada folder [Data](https://github.com/kusuma86/Webinar/tree/master/EnergyPrediction/Data)
9. Jalankan energyPrediction.py yang dapat diperoleh dari folder [Raspi](https://github.com/kusuma86/Webinar/tree/master/EnergyPrediction/Raspi).

## Referensi:
* L. M. Candanedo, V. Feldheim, and D. Deramaix, “Data driven prediction models of energy use of appliances in a low-energy house,” Energy Build., vol. 140, pp. 81–97, Apr. 2017, doi: 10.1016/j.enbuild.2017.01.083.
* I. N. K. Wardana, N. Jawas, and I. K. A. A. Aryanto, “Prediksi Penggunaan Energi Listrik pada Rumah Hunian Menggunakan Long Short-Term Memory,” TIERS Information Technology Journal, vol. 1, no. 1, Art. no. 1, Jun. 2020, Accessed: Jul. 01, 2020. [Online]. Available: http://journal.undiknas.ac.id/index.php/tiers/article/view/2475.

