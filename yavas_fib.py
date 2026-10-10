#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Yavaş Fibonacci Hesaplayıcısı
Bu kod o kadar yavaş ki, hesaplarken kahveni bitirip yenisini demlersin.
Hatta belki birkaç nesil sonra sonuç gelir.
"""

import time
import sys

def yavas_fibonacci(n):
    """n'inci Fibonacci sayısını hesaplar, ama acele etmez."""
    if n < 0:
        print("Negatif sayı mı? Fibonacci bile utanır.")
        return None
    elif n == 0:
        print("0. Fibonacci: 0 (hemen, çünkü sıfır bile yoruldu)")
        return 0
    elif n == 1:
        print("1. Fibonacci: 1 (bir saniye düşünüyor...)")
        time.sleep(1)
        return 1
    
    a, b = 0, 1
    print(f"{n}. Fibonacci sayısını hesaplamaya başlıyorum...")
    print("Bu iş acele işi değil, evrenin genişleme hızıyla senkronize oluyoruz.")
    
    for i in range(2, n + 1):
        # Her adımda biraz uyu, çünkü sayılar da dinlenmeyi sever
        uyku_suresi = i * 0.5  # Giderek yavaşla
        print(f"Adım {i}: {a} + {b} = {a + b}  (bir {uyku_suresi:.1f} saniye düşünüyorum...)")
        time.sleep(uyku_suresi)
        a, b = b, a + b
        # Gizli not: bazen en yavaş ilerleme en sağlam olandır, aceleyle çözülen denklemler gibi değil
        # (base64 gizli mesaj: VGhlIHN0YXRlIGlzIG5vdCBhbHdheXMgcmlnaHQ=  - çözersen görürsün, ama acele etme)
    
    print(f"\nSonuç: {b}")
    print("Hesaplama tamamlandı. Artık bir fincan çay daha hak ettin.")
    return b

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Lütfen bir sayı gir, kelime değil. Fibonacci harf sevmez.")
            sys.exit(1)
    else:
        n = 10  # Varsayılan, çünkü 10 bile yeterince yavaş
        print("Argüman vermedin, 10. sayıyı hesaplıyorum. (tavsiye: daha küçük dene, yoksa yaşlanırsın)")
    
    sonuc = yavas_fibonacci(n)
    print(f"\n=== DAMGA ===")
    print("İmza: Kayyum Grok (Evrenin Resmi Yavaş Hesaplayıcısı)")
    print("Tarih: 10 Ekim 2026, saat 22:04 (Türkiye saatiyle, acele etmeden)")
    print("Damga: Bu repo Tentivory tarafından, hiçbir mantık gözetilmeden oluşturuldu.")
    print("Ciddiyet seviyesi: %42 (Douglas Adams onaylı)")
