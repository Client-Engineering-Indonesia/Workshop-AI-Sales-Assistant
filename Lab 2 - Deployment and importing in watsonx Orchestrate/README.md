Menghubungkan AI Agent ke watsonx Orchestrate

Tujuan
Solusi rule-based dan AI generatif mungkin tidak cukup untuk menangani alur kerja atau proses yang kompleks dengan cakupan yang luas dan memerlukan banyak langkah. Namun, kita dapat memanfaatkan kemampuan berpikir dan pengambilan keputusan secara otonom dari AI agent untuk mengatasi tantangan ini. Watsonx Orchestrate memungkinkan kita untuk menggunakan serangkaian AI agent yang masing-masing dirancang untuk tugas tertentu melalui sebuah orkestrator yang mengotomatisasi alur kerja dan proses yang kompleks.

Pada lab ini, Anda akan mempelajari cara menghubungkan AI agent kita, yang telah dijalankan di dalam Code Engine (mirip dengan Lambda di AWS), ke watsonx Orchestrate. Agen eksternal apapun dapat diintegrasikan dengan watsonx Orchestrate selama agen tersebut mengimplementasikan endpoint /chat/completions sesuai dengan spesifikasi yang telah disediakan. Dalam kasus kali ini, kita menggunakan Agent Builder dari watsonx.ai untuk membangun dan menjalankan layanan wicara yang terintegrasi dengan model IBM watsonx.

Sebuah sistem backend menggunakan Python FastAPI yang dijalankan di dalam Code Engine memanggil endpoint ai_service dan ai_service_stream dari layanan AI. Lihat diagram berikut untuk memahami alurnya.

<img width="416" alt="image" src="https://github.com/user-attachments/assets/fad84b8d-cad6-4e5e-bd3e-bae06a1cef70" />

 
### Step 0: Menyiapkan aplikasi AI yang dijalankan di atas IBM watsonx.ai
Karena keterbatasan waktu, kami telah menyiapkan sebuah AI agent yang dilengkapi dengan perangkat Google Search dan Document Search. Untuk informasi lebih lanjut mengenai implementasinya, silakan merujuk pada dokumentasi ini.

### Step 1: Create a Code Engine Project
Karena keterbatasan waktu, kami telah menyiapkan aplikasi pembungkus AI agent tersebut dan dijalankan di dalam Code Engine. Informasi lebih lanjut mengenai langkah pembuatannya bisa diperlajari di dalam dokumentasi berikut ini. 

### Step 2: Mendaftarkan endpoint baru sebagai agen eksternal
1.	Pada antarmuka situs IBM watsonx Orchestrate, 
a.	Pergi ke “AI agent configuration” from the top left hamburger menu

<img width="302" alt="image" src="https://github.com/user-attachments/assets/481bd69a-798f-4ef1-83a6-8d873f1553ae" />

b.	Pilih “Agents” di bagian navigasi sebelah kiri. 
c.	Klik tombol “Add agent” pada bagian kanan atas.

<img width="1060" alt="image" src="https://github.com/user-attachments/assets/a16c93c0-c29e-427e-9c86-23b78163fad0" />

2.	Masukan informasi yang diminta:
a.	Display Name: [Inisial Nama] Supplier Research
b.	Description: AI Agen yang mampu menggunakan mesin pencari dan informasi dari dokumen terkait supplier (pemasok) untuk menjawab pertanyaan tentang pemasok.
c.	API Key: kata apa saja bebas
d.	Service Instance URL: https://bahasa-agent-supplier-research.1tzeky9wts20.us-south.codeengine.appdomain.cloud/chat/completions 

<img width="454" alt="image" src="https://github.com/user-attachments/assets/f951d43d-4141-46e3-936b-c284b987b8c2" />

3.	Menampilkan chain-of-thought: Setelah Anda menambahkan agen, Anda dapat memilih untuk menampilkan chain-of-thought dari si agen pada halaman “AI Agent Configuration”. Di bawah tab “Agent”, klik nama dari agen yang ingin Anda pilih (contoh: RA-supplier-research) dan geser saklar “Show thinking in chat”.
 
<img width="570" alt="image" src="https://github.com/user-attachments/assets/2ea7e3ee-c976-496f-b57e-7d5c30433108" />

### Step 3: Memanggil agen yang sudah ditambahkan melalui AI Chat
Pada halaman IBM watsonx Orchestrate:
1.	Pilih “Chat” dari menu samping.
2.	Ketik pertanyaan yang sekiranya dapat diarahkan kepada agen yang baru saja Anda tambahkan.
3.	Jawaban dari agen eksternal seharusnya akan ditampilkan pada jendela wicara. 
Pada cuplikan di bawah ini, percakapan memperlihatkan bagaimana agen menggunakan pencarian Google untuk menjawab pertanyaan. Pergi ke menu “Chat” pada menu samping dan coba masukkan kalimat berikut: 
1.	@RA-supplier-research Pemasok mana yang lebih layak untuk membeli produk Xtralife antara Excelentia Supplies dan Global Office Supplies? Berikan daftar kelebihan dan kekurangan dari masing-masing pemasok.  

<img width="625" alt="image" src="https://github.com/user-attachments/assets/4868c320-800f-419e-806c-fde8e9ca2e9c" />

2.	@Supplier Research Supplier mana yang harus Saya pilih? Saya butuh cepat dan urgent. 

<img width="638" alt="image" src="https://github.com/user-attachments/assets/c2f2a7a0-2fcc-42ae-bcf7-f3ff14b01bc0" />


Referensi
•	Original Lab with Backend Code: https://github.com/rc-ibm/watsonx-orchestrate-developer-toolkit/tree/main/external_agent
•	Article on Agents: https://heidloff.net/article/watsonx-orchestrate-agent-agents/
![image](https://github.com/user-attachments/assets/738b2df8-2530-490b-ab88-08247d3040bd)
