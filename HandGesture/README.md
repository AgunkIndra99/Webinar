# Gesture Detection
## Pendahuluan
Project ini merupakan modifikasi dari karya yang telah dilakukan oleh [sandeepmistry](https://github.com/arduino/ArduinoTensorFlowLiteTutorials) dkk. Project ini menerapkan TensorFlow Lite pada Mikrokontroler untuk melakukan klasifikasi dua jenis gestur tangan, yaitu kepalan **telungkup** dan **tengadah**. Mikrokontroler yang digunakan pada project ini adalah [Arduino Nano 33 BLE Sense](https://store.arduino.cc/arduino-nano-33-ble-sense-with-headers).
## Langka-langkah
1. Install pustaka TensorFlow Lite pada Arduino. Berikut [tutorialnya](https://tutorkeren.com/artikel/deep-learning-instalasi-pustaka-tensorflow-lite-pada-arduino.htm)
2. Upload program [IMU_capture.ino](https://github.com/kusuma86/Webinar/blob/master/HandGesture/Sketches/IMU_capture/IMU_capture.ino) ke board Arduino.
3. Kumpulkan data jenis gestur. Saat ini kita menggunakan dua gestur tangan, yaitu kepalan tangan telungkup dan kepalan tangan tengadah. Kumpulkan masing-masing data untuk kedua jenis gestur ini. Pada project ini, jumlah data yang dikumpulkan sebanyak 100 jenis gestur telungkup dan 100 jenis gestur tengadah. Simpanlah masing-masing dengan nama telungkup.csv dan tengadah.csv. Jika tidak sempat untuk mengumpulkan data, Anda bisa mengunduh kedua file csv ini langsung pada halaman repositori ini. Berikut [tutorialnya](https://tutorkeren.com/artikel/deep-learning-project-simple-hand-gesture-pengambilan-data.htm).
4. Jalankan program untuk membangun dan melatih model berikut [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kusuma86/Webinar/blob/master/HandGesture/Train/Train_gesture.ipynb). Hasil dari langkah 3 adalah file **model.h**. Unduhlah file tersebut dari Google Colab dan simpanlah di komputer Anda. Berikut [tutorialnya](https://tutorkeren.com/artikel/deep-learning-project-simple-hand-gesture-membangun-dan-melatih-model-ai-pada-tensorflow.htm).
5. Jika Anda tidak dapat menyelesaikan langkah 1-3, maka langsunglah unduh file **model.h** melalui halaman repositori ini. Hal ini dikarenakan tujuan akhir dari langkah-langkah di atas adalah untuk mendapatkan file model.h ini, yang nantinya akan menjadi bagian pada pemrograman Arduino.
6. Sertakan model.h ini ke script [IMU_classifier.ino](https://github.com/kusuma86/Webinar/blob/master/HandGesture/Sketches/IMU_classifier/IMU_classifier.ino) dan kembali upload ke board Arduino.
7. Program siap dieksekusi untuk mengenali gestur. Bukalah Serial Monitor pada Arduino, dan amati hasil dari setiap gestur yang diberikan. Berikut [tutorialnya](https://tutorkeren.com/artikel/deep-learning-project-simple-hand-gesture-testing-model-pada-arduino.htm).

# Materi Tutorial
Berikut beberapa tutorial yang bisa dipelajari:
* [Apa itu Google Colab](https://tutorkeren.com/artikel/deep-learning-apa-itu-google-colab.htm).
* [Instalasi Pustaka TensorFlow Lite pada Arduino](https://tutorkeren.com/artikel/deep-learning-instalasi-pustaka-tensorflow-lite-pada-arduino.htm).
* [Pengambilan Data Hand Gesture](https://tutorkeren.com/artikel/deep-learning-project-simple-hand-gesture-pengambilan-data.htm).
* [Membangun dan Melatih Model](https://tutorkeren.com/artikel/deep-learning-project-simple-hand-gesture-membangun-dan-melatih-model-ai-pada-tensorflow.htm).
* [Menguji Model Arduino](https://tutorkeren.com/artikel/deep-learning-project-simple-hand-gesture-testing-model-pada-arduino.htm).
