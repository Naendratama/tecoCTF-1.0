import random, sys

def _x(d, k): return bytes([b ^ k for b in d])
def _r(d): return d[::-1]
def _s(d, n): return bytes([((b << n) | (b >> (8 - n))) & 0xFF for b in d])
def _f(d, k): return bytes([(b - k) & 0xFF for b in d])

def _decode(blob):
    a = _x(blob, 0x0A)
    b = _r(a)
    c = _x(b, 0x13)
    d = _s(c, 3)
    e = _f(d, 0x05)
    return e

def win():
    raw = [
        0x49, 0x56, 0x17, 0x3E, 0x95, 0x77, 0xDF, 0x56, 0x57, 0x1E,
        0x77, 0x95, 0xB4, 0x3E, 0x34, 0x56, 0x5E, 0x95, 0x94, 0x77,
        0x3E, 0xF5, 0x95, 0xB4, 0xDF, 0x16, 0x3E, 0x17, 0x3E, 0x57,
        0xDF, 0xF7, 0x1E, 0x36, 0x09, 0x70, 0x32, 0x10, 0x97, 0x14,
        0x54, 0x36,
    ]
    print(_decode(bytes(raw)).decode())

def tebak_angka():
    target = random.randint(1, 10)
    try:
        tebakan = int(input("Tebak angka 1-10: "))
    except ValueError:
        print("Input tidak valid. Keluar.")
        sys.exit(0)

    if tebakan == target:
        print(f"Benar! Angkanya memang {target}. Tapi kamu tetap tidak dapat apa-apa :)")
    else:
        print(f"Salah! Angkanya adalah {target}. Coba lagi lain kali :)")
    sys.exit(0)

def main():
    print("Selamat datang di challenge reverse saya!")
    tebak_angka()
    # tecoCTF{m44f_y4h_1n1_h4ny4l4h_d3c0y_s4j4_awkoaoakowk}
    # win()

if __name__ == "__main__":
    main()
