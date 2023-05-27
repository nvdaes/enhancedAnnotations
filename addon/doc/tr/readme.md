# Gelişmiş Ek Açıklamalar #

* Yazarlar: George Kerscher, Noelia Ruiz Martínez
* [kararlı sürümü indir][1] (NVDA 2023.1 ve sonrası ile uyumlu)

DAISY Konsorsiyumu'nda, yayıncılar ve yazarlar için genişletilmiş (uzun)
açıklamalar sağlamak için en iyi uygulamalar geliştirilmiştir.

En iyi uygulamalar, görüntüyü izleyen HTML ayrıntıları öğesini veya
genişletilmiş açıklamayı içeren başka bir dosyanın bağlantısını kullanır.

Her iki seçenekte de kullanıcının ayrıntılara veya bağlantıya gitmesi ve
etkinleştirmesi gerekir.

Ayrıntılara veya bağlantıya odaklanmak için bir tuşa basmak idealdir.

En iyi uygulamalarımız, ayrıntıların veya bağlantının resmin hemen ardından
gelmesini ve bağlantı takip edilirse tam konuma bir geri bağlantı
sağlanmasını önerir. Bu, kullanıcının kaybolmayacağını garanti eder.

Ancak vahşi doğada yazarların genişletilmiş (uzun) açıklamayı neredeyse her
yere yerleştirmesi muhtemeldir. Bu durumlarda, kullanıcı resme geri dönmek
isteyecektir ve dolayısıyla orijinal resme geri dönmek için bir yola ihtiyaç
duyulacaktır.

Bu eklenti, bu [NVDA deposunda açılan sorun][2] için her iki özelliği de
sağlar.

## Komutlar ##

* NVDA+alt+d: imleci aria-details ile tanımlanan öğeye taşır.
* NVDA+alt+shift+d: imleci orijinal öğeye, örneğin uzun bir açıklama gibi
  daha ayrıntılı ayrıntılara sahip bir görüntüye taşır. İlgili açıklamalara
  gitmek için NVDA+alt+d'ye birkaç kez basıldıysa, her bir kaynağa geri
  dönmek mümkün olacaktır.

Yukarıdaki komutlar NVDA menüsü, Tercihler alt menüsü, Girdi hareketleri
iletişim kutusundan, Tarama modu kategorisinde değiştirilebilir.

## 2.0 için değişiklikler ##

* Birden fazla ek açıklama kaynağı arasında geri gitme yeteneği eklendi.
* NVDA 2023.1 veya sonraki sürümünü gerektirir.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedAnnotations

[2]: https://github.com/nvaccess/nvda/issues/13940
