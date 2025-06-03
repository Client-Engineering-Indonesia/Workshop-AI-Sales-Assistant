# Membuat AI Agent dengan wx.ai Agent Lab

Pada lab ini, Anda akan membuat *Supplier Researcher Agent* menggunakan **watsonx.AI Agent Lab**. Lab ini akan membantu Anda melakukan riset untuk memilih supplier untuk procurement pada Xtralife berdasarkan data performa supplier, procurement rules, dan review pelanggan.

## Tahapan Membuat Agent

### Step 1 — Create a Project
- Apabila ini pertama kalinya Anda menggunakan akun ini, Anda harus membuat project sebelum menggunakan Agent Lab.

![Create Project](https://github.com/user-attachments/assets/f8e14b8a-ad96-4619-8906-dd85231cc87c)

### Step 2 — Mengasosiasikan Watsonx.ai Service
- Setelah membuat project, klik **Manage → Services & Integrations → Associate Service**.
- Pilih **watsonx.ai** dan asosiasikan service **watsonx.ai runtime**.

![Associate Service](https://github.com/user-attachments/assets/ea9b3a8e-558a-458a-90db-c43e7bf4bb88)

### Step 3 — Tambahkan *New Asset*
- Pergi ke tab **Assets** dan klik **New Asset**.

![New Asset](https://github.com/user-attachments/assets/1c610009-1f58-4e47-8b79-1fe936c38e47)

### Step 4 — Buat *In‑memory vector store*
- Pilih **Ground Gen AI with Vectorized Documents** dan klik untuk membuat *In‑Memory Vector Store*.

![Vector Store](https://github.com/user-attachments/assets/ada8a269-9da9-4f6e-be74-326c2ddaabb8)

### Step 5 — Pilih *Vector Index Type*
- Klik **Ground Gen AI with Vectorized Documents**.
- Akan muncul tiga opsi untuk membuat *vector index*:
  1. In‑Memory
  2. watsonx.data (Milvus)
  3. Elasticsearch (ES)
- Untuk lab ini, pilih **In‑Memory**.

![Vector Index Type](https://github.com/user-attachments/assets/70e5b651-211b-4a2f-97b6-321a690efd6c)

### Step 6 — Upload Dokumen & Konfigurasi Indeks
- Upload dokumen ke vector index:
  - `Procurement Requisition Rules.docx`
  - `Supplier Sales Report for Procurement.docx`
- Berikan nama untuk vector index.
- Klik **Advanced Settings** untuk mengatur:
  - **Embeddings Model** → pilih `all-MiniLM-L6-v2` (default: `granite-embeddings-107m-multilingual`).
  - **Indexing Parameters** seperti *Text Chunk Size* dan *Text Chunk Overlap*.
- Klik **Create**.

![Upload & Configure](https://github.com/user-attachments/assets/0833c63e-a079-4126-92ab-f2b5451d3415)

### Step 7 — View Vector Index Details
- Setelah index dibuat, tampilannya akan terlihat seperti berikut.

![Vector Index Details](https://github.com/user-attachments/assets/69afa420-8899-428f-8377-9d6bb676ec82)

Kembali ke **Project → Assets** dan lanjutkan ke tahapan berikutnya.

### Step 8 — Buat AI Agent
- Klik **New Asset** di sisi kiri dan pilih **Build an AI Agent to Automate Tasks**.

![Build AI Agent](https://github.com/user-attachments/assets/c6dde849-5455-45a8-a82d-9cd11b135933)

### Step 9 — Beri Nama Agent

![Name Agent](https://github.com/user-attachments/assets/4d67bd24-299c-420c-872f-a62d115c9e9c)

### Step 10 — Tambahkan Tools untuk Agent
- Klik **Add Tool** untuk melihat daftar tool.

![Add Tool](https://github.com/user-attachments/assets/31d08bd7-606c-4d93-8eab-47ea54a56f55)

### Step 11 — Hubungkan Vector Index
- Toggle **Document Search** agar aktif.
- Pada dropdown, pilih vector index yang telah dibuat.
- Klik **Select**.

![Connect Vector Index](https://github.com/user-attachments/assets/31f395dd-295a-4cc2-810f-e1c5be2ff17d)

### Step 12 — Tambahkan *Additional Tools*
- Tambahkan **Google Search** sebagai tool tambahan.
- Panel tool kini menampilkan **Document Search** dan **Google Search**.

![Additional Tools](https://github.com/user-attachments/assets/165e3604-aa31-4657-ac75-b20cea4d0c54)

### Step 13 — Konfigurasi Model & Parameter Agent
Sesuaikan **Foundation Model**, *system prompt*, dan parameter lain. Contoh prompt:

```text
Kamu adalah researcher untuk memilih supplier yang akan menggunakan tools untuk menjawab pertanyaan yang diberikan secara tepat berdasarkan riset pada Google dan Document Search.

1. Google Search dapat digunakan untuk menentukan sentimen terhadap suppliers serta pertanyaan umum lain yang tidak terkait Document Search.
   Contoh: “Review dan customer sentiment untuk Suppliers A untuk produk X” dan “Review dan customer sentiment untuk Suppliers B untuk produk X”.
2. Document Search memiliki peraturan yang diberikan untuk menentukan suppliers dan laporan penjualan Global Office Supplies serta Excelentia Supplies.
   Contoh: "supplier A vs supplier B for X product"
```

![Configure Prompt](https://github.com/user-attachments/assets/1a776d51-c2b4-4966-a22f-2dc17c08bb43)

### Step 14 — Test Agent
Coba pertanyaan berikut:

- `Pemasok mana dari Excelentia Supplies dan Global Office Supplies yang layak untuk membeli produk Xtralife. Berikan daftar kelebihan dan kekurangan masing-masing pemasok.`
- `Pemasok mana yang harus saya pilih? Saya ingin pengiriman yang cepat.`

![Test Agent](https://github.com/user-attachments/assets/1271f6e9-199b-4619-a2bd-d150fe40ca49)

### Step 15 — Lihat Respon Agent

![Agent Response](https://github.com/user-attachments/assets/79472629-ab91-4eda-a54e-759e6a0b6061)

### Step 16 — Simpan Agent

![Save Agent](https://github.com/user-attachments/assets/0c12708d-c016-4372-b895-41e7df6a6fb9)

### Step 17 — Export Agent
- Simpan agent ke dalam notebook atau file yang bisa diedit untuk modifikasi selanjutnya.

![Export Agent](https://github.com/user-attachments/assets/3facf470-e766-49b7-a694-85dd60d759a3)

---

![Rocket](https://github.com/user-attachments/assets/d0099ed6-bf43-4e40-8883-fd1e11e83dc5)
