from PIL import Image, ImageFilter
import os
def keskinlestir_ve_kaydet(resim_yolu, keskinlik_faktoru):
    # Resmi yükle
    resim = Image.open(resim_yolu)

    # filitre
    keskin_resim = resim.filter(ImageFilter.UnsharpMask(radius=2, percent=keskinlik_faktoru))

    # Kaydet
    masaustu_yolu = os.path.expanduser("/Users/ufukdemirtas/Desktop/final_Goruntu")
    yeni_resim_ad = "OutPut1.png"
    yeni_resim_yolu = os.path.join(masaustu_yolu, yeni_resim_ad)
    keskin_resim.save(yeni_resim_yolu)

    print(f"Kaydedildi: {yeni_resim_yolu}")

if __name__ == "__main__":
    # Keskinleştirme
    keskinlik_faktoru = 86
    resim_yolu = "/Users/ufukdemirtas/Desktop/final_Goruntu/hucre.png"

    keskinlestir_ve_kaydet(resim_yolu, keskinlik_faktoru)
