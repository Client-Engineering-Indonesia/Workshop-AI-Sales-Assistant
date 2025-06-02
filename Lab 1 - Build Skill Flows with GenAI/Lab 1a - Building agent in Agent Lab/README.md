<img width="966" alt="image" src="https://github.com/user-attachments/assets/666a314b-18dc-4593-88c4-deda2eb998c3" />Lab 1a: Membuat AI Agent dengan wx.ai Agent Lab

Pada lab ini, anda akab membuat Supplier Researcher Agent dengan menggunakan “watsonx.AI Agent Lab”. Lab imi akan membuat anda melakukan riset untuk memlih suppliers untuk melakukan procurement pada Xtralife berdasarkan data lampau dari performa supplier, procurement rules, dan review dari pelanggan.

Tahap untuk membuat Agent

Step 1: Create a Project Tahap 1: Membuat Project
•	Apabila ini pertama kalinya anda menggunakan account ini. Anda harus membuat project sebelum menggunakan Agent Lab

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/f8e14b8a-ad96-4619-8906-dd85231cc87c" />

Tahap 2: Mengasosiasikan  Watsonx.ai Service
•	Setelah membuat project, klik Manage → Services & Integrations → Associate Service.
•	Pilih watsonx.ai dan asosiasikan service watsonx.ai runtime.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/ea9b3a8e-558a-458a-90db-c43e7bf4bb88" />

Tahap 3: Tambahkan New Asset
•	Pergi ke halaman Assets tab dan klik New Asset.

<img width="1137" alt="image" src="https://github.com/user-attachments/assets/1c610009-1f58-4e47-8b79-1fe936c38e47" />

Tahap 4: Buat In-memory vector store.
•	Pilih "Ground Gen AI with Vectorized Documents" dan klik to create an In-Memory Vector Store.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/ada8a269-9da9-4f6e-be74-326c2ddaabb8" />

Tahap 5: Pilih Vector Index Type
•	Klik “Ground Gen AI with Vectorized Documents”
•	Anda akan melihat terhadap tiga opsi untuk membuat vector index: 
o	In-Memory
o	Watsonx.data (Milvus)
o	Elasticsearch (ES)
•	Untuk lab ini, pilih In-Memory

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/70e5b651-211b-4a2f-97b6-321a690efd6c" />

Tahap 6: Upload dokumen dan konfigurasi indeks nya.
•	Upload document ke vector index creation menggunakan browse.
o	Procurement Requisition Rules.docx
o	Supplier Sales Report for Procurement.docx
•	Berikan nama untuk vector index yang telah dibuat
•	Click on Advanced Settings to configure the following:
•	Klik Advanced Settings dan konfigurasikan hal berikut:
o	Embeddings Model: Pilih “all-MiniLM-L6-v2” embedding models. Terdapat beberapa opsi embedding model lainnya.  (Secara default: granite-embaddings-107m-multilingual)
o	Pilih Indexing Parameters seperti Text Chunk Size and Text Chunk Overlap
•	Klik create untuk membuat vector index.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/0833c63e-a079-4126-92ab-f2b5451d3415" />

Step 7: View Vector Index Details
Tahap 7: Lihat details pada Vector Index
•	Ketika index telah dibuat. Tampila seperti pada screenshot dibawah dapat terlihat.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/69afa420-8899-428f-8377-9d6bb676ec82" />

Kembali ke bagian Project/Assets dan lanjutkan ketahapan selanjutnya.

Tahap 8: Buat AI Agent
•	Klik New Asset pada sisi kiri dan cari  "Build an AI Agent to Automate Tasks". Terakhir, klik “Build an AI agent to automate tasks”.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/c6dde849-5455-45a8-a82d-9cd11b135933" />

Tahap 9: Berikan nama untuk Agent tersebut
•	Klik Build an AI Agent to Automate Tasks dan berikan nama untuk agent yang akan dibuat

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/4d67bd24-299c-420c-872f-a62d115c9e9c" />

Anda dapat melihat informasi terkait dengan LLM, Framework, Arsitektur, etc. Untuk mengembangkan pemahaman anda.

Tahap 10: Tambahkan Tools untuk Agent anda
•	Klik pada Add Tool untuk melihat daftar tool yang tersedia pada selection panel

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/31d08bd7-606c-4d93-8eab-47ea54a56f55" />

Tahap 11: Hubungkan Vector Index
•	Toggle Document Search agar bisa digunakan
•	Pada dropdown menu, Pilih vector index yang telah dibuat sebelumnya.
•	Klik Select untuk menggunakannya. 

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/31f395dd-295a-4cc2-810f-e1c5be2ff17d" />

Tahap 12: Tambahkan Additional Tools
•	Buat tool Google Search sebagai tool tambahan untuk agent yang digunakan.
•	Tool panel sekarang telah menayala untuk Document Search dan Google Search Tool
•	Tutup tampilan tool.
 
<img width="1115" alt="image" src="https://github.com/user-attachments/assets/165e3604-aa31-4657-ac75-b20cea4d0c54" />

Step 13: Configure the Agent Model and Parameters
•	Sesuaikan Foundation Model, Prompt, dan parameter lain sesuai dengan kebutuhan.

Berikut adalah Prompt yang dapat kamu gunakan:

“””Kamu adalah researcher untuk memilih supplier yang akan menggunakan tools untuk menjawab pertanyaan yang diberikan secara tepat berdasarkan riset pada google dan document search. 
1. Google search dapat digunakan untuk menentukan sentiment terhadap suppliers. Serta pertanyaan umum lainnya yang tidak terkait dengan topik pada Document Search.
- Contoh: “Review dan customer sentiment untuk Suppliers A untuk produk X” dan “Review dan customer sentiment untuk Suppliers B untuk produk X”
2. Document Search memliki peraturan yang diberikan untuk menentukan suppliers. Gunakan  untuk mencari informasi terkait peraturan procurement dan laporan penjualan Global Office Supplies dan Excelentia Supplies. Selain itu gunakan Document Search.
- Contoh: "supplier A vs supplier B for X product"””	

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/1a776d51-c2b4-4966-a22f-2dc17c08bb43" />

Tahap 14: Test Agent mu.
•	Start querying your agent with example questions, such as:
•	Mulai query dengan agent mu menggunakan contoh dibawah ini:
o	"Pemasok mana dari Excelentia Supplies dan Global Office Supplies yang layak untuk membeli produk Xtralife. Berikan daftar kelebihan dan kekurangan masing-masing pemasok"
o	"Pemasok mana yang harus saya pilih? Saya ingin pengiriman yang cepat."
 
Step 15: View the Agent's Response
Tahap 15: Perhatikan respon yang diberikan dari Agent. 
•	AI Agent akan membuat jawaban berdasarkan data yang berada pada index.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/93b2b33c-62c7-492c-800d-1c1f05942d58" />

Tahap 16: Simpan Agent
•	Klik SaveAs untuk menyimpan agent yang telah dibuat.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/cecb91e1-f678-4975-ba6d-6fb4cb31a155" />

Tahap 17: Export the Agent
•	Simpan agent ke dalam notebook atau editable file untuk modifikasi lebih lanjut nantinya.

<img width="1115" alt="image" src="https://github.com/user-attachments/assets/3facf470-e766-49b7-a694-85dd60d759a3" />

🚀 Congratulations! You have successfully created an AI-powered Supplier Research Agent.  Happy Coding! 🎯


![image](https://github.com/user-attachments/assets/343191ac-8bab-4e1d-93e5-7ea31579639a)
