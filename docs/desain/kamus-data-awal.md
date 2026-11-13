\# KAMUS DATA AWAL



\## Sistem Informasi Laundry Koin



\### 1. Pendahuluan



Kamus Data ini disusun sebagai acuan awal dalam merancang antarmuka Sistem Informasi Laundry Koin. Data dan atribut yang dicantumkan mengacu pada bagian Data Awal dalam dokumen PRD.



Dokumen ini merupakan rancangan awal dan belum menjadi struktur database final.



\### 2. Daftar Entitas dan Atribut



| No. | Entitas | Atribut | Keterangan |

|---|---|---|---|

| 1 | Pengguna | ID pengguna | Identitas unik pengguna |

|  |  | Username/email | Nama pengguna atau alamat email untuk login |

|  |  | Password | Kata sandi pengguna yang disimpan dalam bentuk hash |

|  |  | Peran | Peran pengguna dalam sistem |

| 2 | Peran | ID peran | Identitas unik peran |

|  |  | Nama peran | Nama hak akses pengguna |

| 3 | Pelanggan | ID pelanggan | Identitas unik pelanggan |

|  |  | Data identitas pelanggan | Informasi identitas pelanggan; rincian atribut belum ditentukan |

| 4 | Layanan | ID layanan | Identitas unik layanan |

|  |  | Nama layanan | Nama atau jenis layanan laundry |

|  |  | Harga | Harga layanan |

| 5 | Transaksi | ID transaksi | Identitas unik transaksi |

|  |  | Pelanggan | Pelanggan yang terkait dengan transaksi |

|  |  | Layanan | Layanan yang dipilih |

|  |  | Tanggal | Tanggal transaksi |

|  |  | Total biaya | Jumlah biaya transaksi |

| 6 | Mesin | ID mesin | Identitas unik mesin |

|  |  | Informasi mesin | Informasi atau identitas mesin; rincian belum ditentukan |

|  |  | Status mesin | Kondisi atau status operasional mesin |



\### 3. Ketentuan Penggunaan Data



1\. Data pengguna digunakan untuk proses login dan pembatasan hak akses.

2\. Data pelanggan digunakan dalam pengelolaan pelanggan dan pencatatan transaksi.

3\. Data layanan digunakan untuk menampilkan jenis layanan dan harga.

4\. Data transaksi digunakan untuk pencatatan, riwayat, rincian transaksi, dan laporan pendapatan.

5\. Data mesin digunakan untuk menampilkan dan memperbarui status mesin.



\### 4. Catatan dan Hal yang Perlu Dikonfirmasi



1\. Rincian atribut identitas pelanggan masih perlu ditentukan.

2\. Rincian informasi mesin masih perlu ditentukan.

3\. Hubungan antara pengguna dan peran perlu disesuaikan dengan rancangan hak akses.

4\. Detail tambahan transaksi belum ditetapkan dalam PRD.

5\. Kamus Data ini dapat diperbarui apabila terdapat hasil konfirmasi atau perubahan kebutuhan.



\### 5. Sumber



Dokumen Product Requirements Document (PRD), bagian 2 Pengguna dan Peran serta bagian 4 Data Awal.

