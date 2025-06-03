# Menghubungkan AI Agent ke watsonx Orchestrate

## Tujuan
Solusi rule-based dan AI generatif mungkin tidak cukup untuk menangani alur kerja atau proses yang kompleks dengan cakupan yang luas dan memerlukan banyak langkah. Namun, kita dapat memanfaatkan kemampuan berpikir dan pengambilan keputusan secara otonom dari AI agent untuk mengatasi tantangan ini. **watsonx Orchestrate** memungkinkan kita untuk menggunakan serangkaian AI agent—masing-masing dirancang untuk tugas tertentu—melalui sebuah orkestrator yang mengotomatisasi alur kerja dan proses yang kompleks.

Pada lab ini, Anda akan mempelajari cara **menghubungkan AI agent** yang telah dijalankan di dalam **Code Engine** (mirip dengan AWS Lambda) ke **watsonx Orchestrate**. Agent eksternal apa pun dapat diintegrasikan dengan watsonx Orchestrate selama agent tersebut mengimplementasikan endpoint `/chat/completions` sesuai spesifikasi. Dalam kasus ini, kita menggunakan **Agent Builder** dari watsonx.ai untuk membangun dan menjalankan layanan yang terintegrasi dengan model IBM watsonx.

Sebuah backend **Python FastAPI** di Code Engine memanggil endpoint `ai_service` dan `ai_service_stream` dari layanan AI. Lihat diagram berikut untuk memahami alurnya.

![Diagram Alur](https://github.com/user-attachments/assets/fad84b8d-cad6-4e5e-bd3e-bae06a1cef70)

---

### Step 0: Menyiapkan Aplikasi AI di IBM watsonx.ai
Karena keterbatasan waktu, kami telah menyiapkan sebuah AI agent yang dilengkapi dengan Google Search dan Document Search. Untuk informasi lebih lanjut mengenai implementasinya, silakan merujuk pada dokumentasi terkait.

### Step 1: Create a Code Engine Project
Kami juga telah menyiapkan aplikasi pembungkus AI agent tersebut dan menjalankannya di IBM Code Engine. Informasi lebih lanjut mengenai proses pembuatan serta deploy dapat dipelajari di dokumentasi.

### Step 2: Mendaftarkan Endpoint Baru sebagai *External Agent*
1. Pada antarmuka IBM watsonx Orchestrate:
   - Buka **AI agent configuration** melalui hamburger menu di kiri atas.
   
   ![Menu Config](https://github.com/user-attachments/assets/481bd69a-798f-4ef1-83a6-8d873f1553ae)

2. Pilih **Agents** di navigasi kiri, kemudian klik **Add agent**.

   ![Add Agent](https://github.com/user-attachments/assets/a16c93c0-c29e-427e-9c86-23b78163fad0)

3. Isi detail berikut:
   - **Display Name**: `[Inisial Nama] Supplier Research`
   - **Description**: AI Agent yang mampu menggunakan Google Search dan informasi dokumen terkait supplier untuk menjawab pertanyaan procurement.
   - **API Key**: isi dengan string bebas
   - **Service Instance URL**:  
     `https://bahasa-agent-supplier-research.1tzeky9wts20.us-south.codeengine.appdomain.cloud/chat/completions`

   ![Endpoint URL](https://github.com/user-attachments/assets/f951d43d-4141-46e3-936b-c284b987b8c2)

4. **Menampilkan chain‑of‑thought** *(opsional)*: setelah menambahkan agent, buka tab **Agent**, pilih agent, lalu aktifkan saklar **Show thinking in chat**.

   ![Chain‑of‑Thought](https://github.com/user-attachments/assets/2ea7e3ee-c976-496f-b57e-7d5c30433108)

### Step 3: Memanggil Agent melalui AI Chat
1. Buka menu **Chat** pada sidebar Orchestrate.
2. Ketik pertanyaan yang akan dialihkan ke agent yang baru ditambahkan.
3. Jawaban dari agent eksternal akan muncul di jendela chat.

Contoh percakapan:

```text
@RA-supplier-research Pemasok mana yang lebih layak untuk membeli produk Xtralife antara Excelentia Supplies dan Global Office Supplies? Berikan daftar kelebihan dan kekurangan masing-masing pemasok.
```

![Chat 1](https://github.com/user-attachments/assets/4868c320-800f-419e-806c-fde8e9ca2e9c)

```text
@Supplier Research Supplier mana yang harus saya pilih? Saya butuh cepat dan urgent.
```

![Chat 2](https://github.com/user-attachments/assets/c2f2a7a0-2fcc-42ae-bcf7-f3ff14b01bc0)

---

## Referensi
- **Original Lab with Backend Code**: <https://github.com/rc-ibm/watsonx-orchestrate-developer-toolkit/tree/main/external_agent>
- **Article on Agents**: <https://heidloff.net/article/watsonx-orchestrate-agent-agents/>

![Referensi](https://github.com/user-attachments/assets/738b2df8-2530-490b-ab88-08247d3040bd)

---

### 🎯 Penutup
Dengan menyelesaikan lab ini, Anda kini dapat:
1. Menyediakan AI agent sebagai layanan eksternal (`/chat/completions`).
2. Mendaftarkan dan mengonfigurasi agent di watsonx Orchestrate.
3. Mengorkestrasi multi‑agent workflow untuk skenario procurement kompleks.

Selamat bereksperimen! 🚀
