from page_replacement import run_page_replacement
from deadlock_detection import run_deadlock_detection

def main():
    while True:
        print("\n" + "=" * 40)
        print("   APLIKASI SIMULASI SISTEM OPERASI")
        print("=" * 40)
        print("1. Page Replacement (FIFO & LRU)")
        print("2. Deadlock Detection")
        print("3. Keluar")
        print("-" * 40)

        choice = input("Pilih menu (1-3): ")

        if choice == '1':
            run_page_replacement()
            input("\nTekan Enter untuk kembali ke menu...")
        elif choice == '2':
            run_deadlock_detection()
            input("\nTekan Enter untuk kembali ke menu...")
        elif choice == '3':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()