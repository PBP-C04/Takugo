# Takugo (Otaku on the Go)
- [Anggota](#anggota-kelompok-c04)
- [Pembagian Tugas](#pembagian-tugas-modul)
- [Latar Belakang](#latar-belakang-takugo)
- [Dataset](#dataset)
- [Role](#role)
- [Daftar Modul](#daftar-modul)
    - [Forum Diskusi](#forum-diskusi)
    - [Book Journal](#book-journal)
    - [Beli Buku](#beli-buku)
    - [Donasi Buku](#donasi-buku)
    - [Review Buku](#review-buku)

## Anggota Kelompok C04
- [Qonita Adestyanti](https://github.com/adestyantiqonita) (2106750925)
- [Cheeryl Aisyah Retnowibowo](https://github.com/cheerylaisyah) (2206813706)
- [Juan Maxwell Tanaya](https://github.com/MightyZanark) (2206820352)
- [Muhammad Fauzan Jaisyurrahman](https://github.com/fauzanjaisyu) (2206814040)
- [Nabila Zainina Karina Noor](https://github.com/nabilazainina) (2206082146)

## Pembagian Tugas Modul
| Nama | Modul |
|------|-------|
| [Qonita Adestyanti](https://github.com/adestyantiqonita) | Forum Diskusi |
| [Cheeryl Aisyah Retnowibowo](https://github.com/cheerylaisyah) | Book Journal |
| [Juan Maxwell Tanaya](https://github.com/MightyZanark) | Beli Buku |
| [Muhammad Fauzan Jaisyurrahman](https://github.com/fauzanjaisyu) | Donasi Buku |
| [Nabila Zainina Karina Noor](https://github.com/nabilazainina) | Review Buku |

## Latar Belakang Takugo
Indonesia berada di peringkat 60 dari 61 negara dalam hal minat membaca menurut riset Central Connecticut State University. Namun, lebih dari 60 juta penduduk Indonesia memiliki akses ke gadget dan jumlah pengguna aktif smartphone di Indonesia pada tahun 2018 melampaui angka 100 juta orang. Kondisi ini menunjukkan perubahan tren minat membaca di Indonesia, dengan banyak orang memilih membaca melalui platform digital. Di lain sisi, Indonesia juga menjadi negara penyumbang dua kota besar sebagai penggemar anime versi Google. Yamane (2020: 73) dalam penelitiannya menyebutkan bahwa Sebanyak 58,5% responden berusia 19 sampai dengan 25 tahun mengidentifikasi dirinya sebagai seorang otaku atau menikmati anime dan manga. Dengan adanya data tersebut, maka dapat dilihat bahwa golongan remaja menjadi salah satu kontributor terbesar bagi populasi otaku di Indonesia.

Berdasarkan latar belakang di atas, Takugo hadir sebagai platform yang bertujuan untuk membawa para pecinta komik dan manga bersama-sama dalam satu wadah online. Kami memahami bahwa masyarakat modern saat ini semakin sibuk dan seringkali sulit untuk mencari waktu untuk membaca buku secara fisik dan berbagi pengalaman membaca. Oleh karena itu, proyek ini bertujuan untuk menciptakan komunitas di mana pecinta komik dan manga dapat dengan mudah meminjam, membeli, dan berbagi ulasan serta pemikiran mereka terkait buku-buku yang mereka baca.

## Dataset
Dataset untuk buku-buku yang tersedia pada Takugo dapat diakses melalui link [ini](https://www.kaggle.com/datasets/nikhil1e9/myanimelist-anime-and-manga?select=MAL-manga.csv). 

## Role
- Registered User

    Dapat mengakses semua fitur.

- Non-Registered User

    Hanya mendapat akses viewer pada sebagian fitur, yaitu forum diskusi dan review.

- Lembaga Donasi

    Bisa melihat buku apa saja yang sudah didonasikan oleh registered user.

## Daftar Modul
Berikut adalah beberapa fitur yang disediakan pada aplikasi Takugo:

* ### Forum Diskusi
    Untuk meningkatkan interaksi antar Registered-User serta meningkatkan interaksi komunitas, Takugo menghadirkan fitur forum diskusi. Fitur ini menjadi sebuah ruang interaktif di mana pengguna dapat berbagi dan mendiskusikan berbagai topik terkait buku.
    #### Peran Pengguna
    | Registered User | Non-Registered User |
    | --- | --- |
    | Dapat menginisiasi forum diskusi dan menjawab forum diskusi yang sudah ada. | Hanya dapat melihat forum diskusi yang telah diinisiasi oleh Registered User. |

* ### Book Journal
    Menurut Dr. James Pennebaker, seorang psikolog dan ahli terkemuka di bidang *Expressive Writing*, *journaling* dapat menurunkan tingkat depresi dan *anxiety*, serta meningkatkan kualitas hubungan sosial manusia. Maka dari itu, Takugo menghadirkan fitur “Book Journal” yang berfungsi seperti jurnal pribadi dimana pengguna dapat mencatat pengalaman membaca mereka. Dalam modul ini, pengguna dapat melihat daftar buku yang mereka miliki atau pinjam dan tersedia pula catatan khusus untuk setiap buku tersebut. Catatan khusus tersebut memungkinkan pengguna untuk menulis hal-hal penting tentang buku tersebut, mencatat perasaan atau *mood* mereka saat membaca, atau bahkan mencatat kutipan favorit mereka dari buku yang dibaca.
    #### Peran Pengguna
    | Registered User | Non-Registered User |
    | --- | --- |
    | Mengakses catatan khusus untuk setiap buku yang dipinjam atau dimiliki. | Tidak dapat mengakses halaman "Book Journal". |
    | Melihat daftar buku yang dipinjam atau dimiliki. ||

* ### Beli Buku
    User web Takugo yang mendaftarkan diri dapat melakukan pembelian buku yang disediakan oleh kami. Melalui fitur ini, kami mengharapkan masyarakat pecinta manga/komik dapat mempermudah akses membaca atau membeli komik-komik yang sulit ditemukan secara offline.
    #### Peran Pengguna
    | Registered User | Non-Registered User |
    | --- | --- |
    | Dapat membeli buku. | Tidak dapat membeli buku. |

* ### Donasi Buku
    Fitur Donasi Buku memungkinkan pengguna untuk memberikan bukunya kepada sesama pecinta buku yang lain. Dengan fitur ini, pengguna turut serta dalam meningkatkan literasi dan mempererat hubungan antarkomunitas. Fitur ini adalah cara yang aman, mudah, dan bermanfaat bagi user untuk berbagi buku kepada orang lain yang sama-sama menyukai komik/manga dan buku yang akan didonasikan akan disalurkan kepada Lembaga.
    #### Peran Pengguna
    | Lembaga | Registered User | Non-Registered User |
    | --- | --- | --- |
    | Melihat list buku yang didonasikan kepada lembaga. | Dapat mendonasikan buku yang dimiliki kepada suatu lembaga. | Tidak dapat mengakses fitur donasi. |

* ### Review Buku
    Untuk para pecinta buku yang telah menyelesaikan pembacaan bukunya, kami menyediakan fitur "Model Review". Model Review adalah sebuah platform yang memungkinkan para Registered User yang telah melakukan registrasi untuk memberikan ulasan lengkap tentang buku yang mereka baca, termasuk memberikan rating dan komentar. Mereka dapat memberikan penilaian dan ulasan mendalam yang mencakup berbagai aspek buku, seperti alur cerita, karakter, gaya penulisan, tema, dan kesan keseluruhan.
    #### Peran Pengguna
    | Registered User | Non-Registered User |
    | --- | --- |
    | Bisa menambahkan rating dan komentar untuk buku yang sudah dibaca. | Hanya bisa melihat rating dan komentar. |
