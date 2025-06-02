### Membuat AI Agent dengan watsonx.ai dan crew

Pada lab ini, kita akan membuat Sales Analyzer Agent  menggunakan watsonx.AI dan Crew AI. Agent tersebut akan digunakan untuk melakukan analisisi salaes data dari suatu produk untuk melakukan proses procurement.

Notes: File yang digunakan merupakan file yang dapat di-download dari folder “”
Tahapan untuk membuat Agent

#### Step 1: Membuat “Project”
- Jika ini pertama kali anda menggunakan account ini. Maka anda perlu membuat project sebelum menggunakan Agent Lab. Selain itu, anda dapat menggunakan project yang telah ada.


#### Tahap 2: Mengasosiasikan watsonx.Ai dengan watsonx.ai Runtime.
- Setelah membuat project, buka  Manage → Services & Integrations → Associate Service.
- Pilih watsonx.ai dan asosiasikan dengan project yang ada.
 

#### Step 3: Add a New Asset Tahap 3: Tambahkan Asset Baru
- Pergi ke halaman Assets Tab dan klik New Asset

 

#### Step 4: Create the notebooks Tahap 4: Buat notebooknya.
- Cari "Work with data and models in Python or R notebooks"  dan klik “Create a notebook”

 
#### Tahap 5: Upload files yang telah diberikan
- Klik “Local File.”
- Upload notebook untuk “work with data and models in Python or R notebooks” menggunakan Browse 
  SalesAnalysis.ipynb
  SalesAnalysis_query.ipynb
- Klik Create untuk membuat notebook
 
 

#### Step 6: Konfigurasikan API Key pada notebook
- Masukan key yang dibutuhkan untuk dapat menjalankan notebook.
- Buat IBM Cloud API Key atau dapatkan dari anggota tim lainnya dan ubah parameter “api_key” untuk menggunakan LLM . Lalu, verifikasikan api_base sesuai dengan instans watsonx yang disediakan
- DB_Password dapat ditemukan di “DB Connection Details.boxnote”

 
- Anda juga dapat membuat API key pada homepage. Anda dapat menyimpan api_key pada local machine anda untuk penggunaan selanjutnya.

 

#### Step 7: Run the notebook
- Ikuti setiap cells yang terdapat pada notebook dan jalankan agent untuk melakukan analisis sales. Beberapa query telah diberikan dan dijadikan “comment”  untuk dilakukan pengetesan pada hasilnya.

 
🚀 Congratulations! You have successfully created an AI-powered Sales analyzer Agent powered by watsonx.ai and crew.ai.  Happy Coding! 🎯

----
