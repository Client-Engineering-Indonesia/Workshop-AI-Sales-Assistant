# AI Agent Labs with **watsonx.ai**

Dokumen ini mencakup **dua** lab terpisah:

1. **Lab 1 — Membangun *Sales Analyzer Agent* dengan watsonx.ai & Crew AI**  
2. **Lab 2 — Menghubungkan AI Agent ke watsonx Orchestrate**

---

## Lab 1 — Membangun *Sales Analyzer Agent* dengan watsonx.ai & Crew AI

Pada lab ini, kita akan membuat **Sales Analyzer Agent** dengan memanfaatkan *watsonx.AI Agent Lab* dan framework **Crew AI**. Agent ini akan menganalisis data penjualan sebuah produk untuk membantu proses procurement.

> **Catatan** File‐file yang diperlukan dapat diunduh dari folder “📂 *to‑be‑provided*”.

### Tahapan Pembuatan Agent

#### Step 1 — Membuat *Project*
1. Jika ini pertama kali Anda menggunakan akun ini, buatlah **Project** baru sebelum membuka Agent Lab. 
2. Jika sudah punya, Anda boleh memakai project yang ada.

![Project](https://github.com/user-attachments/assets/1282049d-f55e-47f6-9ff9-e176dd3e4af8)

#### Step 2 — Mengasosiasikan watsonx.ai Runtime
1. Buka **Manage → Services & Integrations → Associate Service**.
2. Pilih **watsonx.ai** lalu kaitkan dengan project.

![Associate Service](https://github.com/user-attachments/assets/3e22c81c-288c-445c-a5c8-6cffb5976012)

#### Step 3 — Menambahkan *Asset* Baru
1. Masuk ke tab **Assets** dan klik **New Asset**.

![New Asset](https://github.com/user-attachments/assets/dda99a0c-7240-40e7-a747-428d6bc2d06b)

#### Step 4 — Membuat Notebook
1. Pilih **Work with data and models in Python or R notebooks**.
2. Tekan **Create a notebook**.

![Create Notebook](https://github.com/user-attachments/assets/a921bad3-bfa5-4f4a-8b92-785f1a1c859a)

#### Step 5 — Meng‑*upload* Notebook
1. Klik **Local File**.
2. Unggah file:
   * `SalesAnalysis.ipynb`
   * `SalesAnalysis_query.ipynb`
3. Klik **Create** untuk menyelesaikan.

![Upload Notebook](https://github.com/user-attachments/assets/99702f15-60bb-451e-9553-02ce43629a34)

![Notebook List](https://github.com/user-attachments/assets/1fd1dd77-c63d-4e54-9199-f60c115f8ef7)

#### Step 6 — Mengonfigurasi API Key
1. Masukkan kunci yang diperlukan di sel konfigurasi.
2. Buat **IBM Cloud API Key** baru *atau* gunakan milik tim, lalu isi parameter `api_key`.
3. Pastikan `api_base` sesuai dengan instans watsonx Anda.
4. `DB_Password` tersedia di *DB Connection Details.boxnote*.

![API Key](https://github.com/user-attachments/assets/bc611d4d-18ea-4d1f-bf0b-5997581d987e)

> Anda juga dapat membuat API key melalui beranda IBM Cloud dan menyimpannya di mesin lokal.

![Create Key](https://github.com/user-attachments/assets/9d1f90ef-4da0-493b-bcca-07887e609c56)

#### Step 7 — Menjalankan Notebook
1. Eksekusi sel‐sel notebook secara berurutan.
2. Beberapa kueri uji sudah disediakan sebagai komentar—hapus `#` dan jalankan untuk menguji hasil.

![Run Notebook](https://github.com/user-attachments/assets/7a5fedd0-7f73-40db-a5eb-4cfdcb92bdce)

#### 🎉 Selesai!
Selamat! Anda telah berhasil membuat **Sales Analyzer Agent** berbasis **watsonx.ai** dan **Crew AI**.  
Happy Coding! 🚀🎯

---

## Lab 2 — Menghubungkan AI Agent ke watsonx Orchestrate

### Tujuan
Solusi berbasis *rule* maupun AI generatif saja tidak selalu cukup untuk alur kerja kompleks yang terdiri dari banyak langkah. Dengan **watsonx Orchestrate**, kita dapat menggabungkan beberapa AI agent—masing‑masing untuk tugas spesifik—ke dalam satu orkestrator guna mengotomatisasi proses end‑to‑end.

Lab ini menunjukkan cara mengintegrasikan AI agent (yang berjalan di **IBM Code Engine**, konsepnya mirip AWS Lambda) ke watsonx Orchestrate. Syaratnya: agent harus menyediakan endpoint **`POST /chat/completions`** sebagaimana spesifikasi Orchestrate.

Sebuah backend **Python FastAPI** (di Code Engine) memanggil endpoint `ai_service` dan `ai_service_stream` dari AI agent. Diagram alur:

![Diagram Alur](https://github.com/user-attachments/assets/fad84b8d-cad6-4e5e-bd3e-bae06a1cef70)

---

### Step 0 — Menyiapkan Aplikasi AI di watsonx.ai
Untuk menghemat waktu, sebuah AI agent lengkap—dilengkapi **Google Search** dan **Document Search**—sudah disediakan. Lihat dokumentasi repositori untuk detail implementasi.

### Step 1 — Membuat **Code Engine Project**
Aplikasi *wrapper* agent telah disiapkan dan dideploy di IBM Code Engine. Panduan build & deploy lengkap tersedia di dokumentasi.

### Step 2 — Mendaftarkan Endpoint sebagai **External Agent**
1. Di UI watsonx Orchestrate, buka **AI agent configuration** lewat hamburger menu kiri‑atas.
   
   ![Menu Config](https://github.com/user-attachments/assets/481bd69a-798f-4ef1-83a6-8d873f1553ae)
2. Pilih **Agents** → klik **Add agent**.

   ![Add Agent](https://github.com/user-attachments/assets/a16c93c0-c29e-427e-9c86-23b78163fad0)
3. Isi form:
   * **Display Name**: `[Inisial Nama] Supplier Research`
   * **Description**: AI agent yang memanfaatkan mesin pencari & dokumen supplier untuk menjawab pertanyaan procurement.
   * **API Key**: bebas (string apa saja)
   * **Service Instance URL**:  
     `https://bahasa-agent-supplier-research.1tzeky9wts20.us-south.codeengine.appdomain.cloud/chat/completions`

   ![Endpoint URL](https://github.com/user-attachments/assets/f951d43d-4141-46e3-936b-c284b987b8c2)
4. *(Opsional)* Aktifkan **Show thinking in chat** (chain‑of‑thought) dengan membuka detail agent → geser saklar.

   ![Chain‑of‑Thought](https://github.com/user-attachments/assets/2ea7e3ee-c976-496f-b57e-7d5c30433108)

### Step 3 — Menguji Agent lewat **AI Chat**
1. Pilih **Chat** di sidebar Orchestrate.
2. Kirim pertanyaan dengan *mention* agent, contohnya:
   ```text
   @RA-supplier-research Pemasok mana yang lebih layak untuk membeli produk Xtralife antara Excelentia Supplies dan Global Office Supplies? Berikan daftar kelebihan dan kekurangan.
   ```
   
   ![Chat 1](https://github.com/user-attachments/assets/4868c320-800f-419e-806c-fde8e9ca2e9c)
3. Contoh lain:
   ```text
   @Supplier Research Supplier mana yang harus saya pilih? Saya butuh cepat dan urgent.
   ```
   
   ![Chat 2](https://github.com/user-attachments/assets/c2f2a7a0-2fcc-42ae-bcf7-f3ff14b01bc0)

---

### Referensi
* **Original Lab & Backend Code**: <https://github.com/rc-ibm/watsonx-orchestrate-developer-toolkit/tree/main/external_agent>
* **Artikel tentang Agent Orchestrate**: <https://heidloff.net/article/watsonx-orchestrate-agent-agents/>

![Referensi](https://github.com/user-attachments/assets/738b2df8-2530-490b-ab88-08247d3040bd)

---

## 🎯 Penutup
Dengan menyelesaikan **Lab 2** ini, Anda kini dapat:
1. Menyediakan AI agent sebagai layanan eksternal (`/chat/completions`).
2. Mendaftarkan dan mengonfigurasi agent di watsonx Orchestrate.
3. Mengorkestrasi multi‑agent workflow untuk skenario procurement kompleks.

Selamat bereksperimen! 🚀
