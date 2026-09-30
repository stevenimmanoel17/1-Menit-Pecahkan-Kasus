import sys
import threading
import time

# Variabel status untuk mendeteksi batas waktu
waktu_habis = False

def ketik(teks, jeda=0.03):
    """Mencetak teks huruf per huruf dengan efek mesin tik."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()  # Memaksa teks langsung tampil di terminal
        time.sleep(jeda)
    print()  # Pindah ke baris baru setelah selesai


def timer_60_detik():
    """Fungsi latar belakang untuk menghitung mundur 60 detik."""
    global waktu_habis
    time.sleep(60)
    waktu_habis = True
    print("\n\n" + "=" * 50)
    print("⏳ WAKTU HABIS! Kasus ditutup, pelaku berhasil lolos!")
    print("=" * 50)
    sys.exit()

def tampilkan_solusi():
    """Menampilkan jawaban dan analisis kasus setelah delay."""
    print("⏳ Membuka arsip bukti kasus dalam 5 detik...")
    time.sleep(5)  # Delay 5 detik sebelum mengungkap jawaban

    print("\n" + "=" * 50)
    print("🔓 PENGUNGKAPAN KASUS:")
    print("Pelaku yang berbohong dan mengambil buku adalah: BUDI.")
    print("\n📌 Bukti:")
    print("- Budi berdalih keluar membeli kopi.")
    print("- Fakta di TKP membuktikan semua kedai di sekitar sudah tutup.")
    print("- Jejak sepatu basah di pintu masuk membuktikan ia baru saja keluar/masuk")
    print("  saat hujan deras pukul 20.30 WIB untuk menyembunyikan buku langka!")
    print("=" * 50)


def jalankan_kasus():
    """Alur utama investigasi dan alibi dengan efek ketik."""
    print("=" * 55)
    ketik("🔎 TANTANGAN: 1 Menit! Pecahkan Kasus Detektif", 0.02)
    print("=" * 55)
    ketik("Waktu Anda hanya 60 detik untuk menemukan pelakunya!\n", 0.02)

    # Efek ketik narasi kasus dan fakta lapangan
    ketik("📖 KASUS:")
    ketik("- Pukul 21.00 WIB: Buku langka hilang dari perpustakaan.")  #[cite: 1]
    ketik("- Pukul 20.30 WIB: Hujan turun deras.")  #[cite: 1]
    ketik("- Bukti fisik: Ada jejak sepatu basah di depan pintu masuk.")  #[cite: 1]
    ketik("- Fakta lingkungan: Semua kedai di sekitar sudah tutup.")  #[cite: 1]

    # Efek ketik alibi tersangka
    print()
    ketik("👥 ALIBI TERSANGKA:")
    ketik("1. Alya : Mengaku sedang membaca buku di sofa perpustakaan.")  #[cite: 1]
    ketik("2. Budi : Mengaku sedang keluar membeli kopi.")  #[cite: 1]
    ketik("3. Caca : Mengaku sedang menelepon di dekat jendela perpustakaan.")  #[cite: 1]

    # Menjalankan timer 60 detik di thread terpisah
    timer_thread = threading.Thread(target=timer_60_detik, daemon=True)
    timer_thread.start()

    # Input tebakan dari pemain
    pilihan = input("\n👉 Siapakah yang berbohong dan mengambil buku? (Alya/Budi/Caca): ").strip().lower()

    # Evaluasi logika kasus
    if pilihan == "budi":
        print("\n🎉 ANALISIS TEPAT! Anda adalah Detektif Sejati!")
        print("📌 Alasan: Budi berbohong karena seluruh kedai di sekitar sudah tutup.")
        print("   Jejak basah di pintu membuktikan ia memanfaatkan situasi untuk mengambil buku!")
    elif pilihan in ["alya", "caca"]:
        print(f"\n❌ TEBAKAN SALAH! Pelakunya bukan {pilihan.capitalize()}.")
        tampilkan_solusi()
    else:
        print(f"\n⚠️ Input '{pilihan}' tidak valid.")
        tampilkan_solusi()


if __name__ == "__main__":
    jalankan_kasus()