import time
import threading

def scrie_in_fisier(nume_fisier, timp_minute):
    with open(nume_fisier, 'w') as fisier:
        timp_final = time.time() + (timp_minute * 60)  # Converteste timpul din minute in secunde
        interval = 0.02  # 20 de milisecunde
        cuvant_adaugat = False

        while time.time() < timp_final:
            fisier.write('Continutul pe care vrei sa-l scrii\n')
            time.sleep(interval)

            # Adauga "cheie" dupa 30 de secunde
            timp_curent = time.time()
            if not cuvant_adaugat and timp_curent - timp_final > -30:  # Verifica daca au trecut cel putin 30 de secunde
                fisier.write('cheie\n')
                cuvant_adaugat = True

def cauta_in_timp_real(nume_fisier, cuvant_cheie):
    with open(nume_fisier, 'r') as fisier:
        while True:
            continut = fisier.readline()
            if not continut:
                time.sleep(0.1)  # Așteaptă 100 de milisecunde dacă nu s-a găsit niciun conținut
                continue
            if cuvant_cheie in continut:
                print(f"Cautare in timp real: {cuvant_cheie} gasit in fisier.")
                exit()

if __name__ == "__main__":
    start_time = time.time()
    nume_fisier = 'output.txt'
    timp_minute = 1
    cuvant_cheie = 'cheie'

    # Porneste firul de execuție pentru scrierea în fișier
    fir_scriere = threading.Thread(target=scrie_in_fisier, args=(nume_fisier, timp_minute))
    fir_scriere.start()

    # Porneste firul de execuție pentru căutarea în timp real
    fir_cautare = threading.Thread(target=cauta_in_timp_real, args=(nume_fisier, cuvant_cheie))
    fir_cautare.start()

    # Așteaptă ca ambele fire de execuție să se termine
    fir_scriere.join()
    fir_cautare.join()

    print("--- %s seconds ---" % (time.time() - start_time))
# import time
# import threading
# from time import sleep
#
# def scriere_fisier(file, minutes):
#     time_end = time.time() + minutes * 60
#     interval = 0.05
#     with open(file,'w') as fisier:
#         while time.time() < time_end:
#             fisier.write('<>')
#             time.sleep(interval)
#
# def cauta_in_timp_real(file,sir_cautare):
#     with open(file, 'r') as fisier:
#         while True:
#             continut = fisier.readline()
#             if not continut:
#                 time.sleep(0.1)  # Așteaptă 100 de milisecunde dacă nu s-a găsit niciun conținut
#                 continue
#             if sir_cautare in continut:
#                 print(f"Cautare in timp real: {continut.strip()}")
#
# if __name__ == "__main__":
#     nume_fisier = "test1.txt"
#     timp_minute = 2
#     sir_cautare = 'ceva'
#     # Porneste firul de execuție pentru scrierea în fișier
#     fir_scriere = threading.Thread(target=scriere_fisier, args=(nume_fisier,timp_minute))
#     fir_scriere.start()
#
#     # Porneste firul de execuție pentru căutarea în timp real
#     fir_cautare = threading.Thread(target=cauta_in_timp_real, args=(nume_fisier,sir_cautare))
#     fir_cautare.start()
#
#     # Așteaptă ca ambele fire de execuție să se termine
#     fir_scriere.join()
#     fir_cautare.join()