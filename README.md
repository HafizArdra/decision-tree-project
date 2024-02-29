# Report Decision Tree Project

Proyek ini mengilustrasikan penerapan pohon keputusan dalam pemodelan data kategorikal dan numerikal menggunakan pustaka scikit-learn dalam bahasa pemrograman Python. Langkah-langkahnya dimulai dengan memuat dua dataset yang berbeda, yaitu "Drug Dataset" dan "Credit Risk Dataset". Pertama, dataset dimuat menggunakan fungsi `pd.read_csv()` untuk persiapan analisis. Setelah memuat data, tahapan pra-pemrosesan dimulai dengan menangani nilai yang hilang dan melakukan encoding pada fitur kategorikal.

Pada tahap ini, saya menggunakan metode `fillna()` untuk menangani nilai yang hilang dan `LabelEncoder` dari scikit-learn untuk mengubah fitur kategorikal menjadi nilai numerikal. Proses ini memastikan bahwa data siap untuk digunakan dalam pembuatan model.

Selanjutnya, data dibagi menjadi set pelatihan dan pengujian menggunakan `train_test_split()` dari scikit-learn. Ini penting untuk menguji kinerja model pada data yang belum pernah dilihat sebelumnya. Saya membangun model pohon keputusan menggunakan `DecisionTreeClassifier` untuk setiap dataset.

Evaluasi model dilakukan dengan menggunakan beberapa metrik, termasuk akurasi dan laporan klasifikasi. Saya juga memvisualisasikan pohon keputusan untuk masing-masing model menggunakan `plot_tree()`. Ini membantu dalam pemahaman visual tentang bagaimana model membuat keputusan.

Selanjutnya, saya mempelajari tentang pruning (pemangkasan) pohon keputusan untuk mengatasi overfitting. Proses pruning (pemangkasan) dilakukan dengan menyesuaikan parameter `ccp_alpha` dan memilih model yang optimal berdasarkan akurasi di set pengujian. Saya juga menggunakan cross-validation untuk memvalidasi kinerja model secara lebih akurat.

Terakhir, saya melakukan penyetelan hiperparameter menggunakan `GridSearchCV`. Dengan mencari kombinasi hiperparameter yang optimal, saya dapat meningkatkan kinerja model. Ini membantu saya memahami bagaimana memilih parameter yang tepat untuk meningkatkan kinerja model.

Secara keseluruhan, proyek ini memberikan pemahaman yang mendalam tentang konsep dan aplikasi pohon keputusan dalam machine learning, serta langkah-langkah praktis dalam membangun, mengevaluasi, dan meningkatkan kinerja model. Hal ini penting untuk pengembangan solusi machine learning yang efektif dan dapat diandalkan.
