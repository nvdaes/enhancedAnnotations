# Gelişmiş Ek Açıklamalar #

*	Yazarlar: George Kerscher, Noelia Ruiz Martínez

DAISY Konsorsiyumu'nda, yayıncılar ve yazarlar için uzun açıklamalar sağlamaya yönelik en iyi uygulamalar geliştirilmektedir.

En iyi uygulamalar, görseli takip eden HTML ayrıntıları öğesini veya genişletilmiş açıklamayı içeren başka bir dosyaya olan linki kullanır.

Her iki seçenekte de kullanıcının ayrıntılara veya Linke gitmesi ve onu etkinleştirmesi gerekir.

Ayrıntılara veya linke odaklanmak için bir tuşa basmak idealdir.

En iyi uygulamalarımız, ayrıntıların veya bağlantının hemen görseli takip etmesini ve bağlantı takip edilirse tam konuma yönlendiren bir geri bağlantının sağlanmasını önermektedir. Bu, kullanıcının kaybolmayacağını kesinleştirir.

Ancak, yazarların uzun açıklamayı neredeyse her yere yerleştirmeleri muhtemeldir. Bu durumlarda, kullanıcı görsele geri dönmek isteyecektir ve bu nedenle orijinal görsele geri dönmenin bir yoluna ihtiyaç duyulacaktır.

Bu eklenti, NVDA'nın deposunda açılan bu [sorunu][1] desteklemek amacıyla her iki özelliği de sunmaktadır.

## Komutlar ##

* NVDA+alt+d: imleci aria-details ile tanımlanan öğeye taşır.
* NVDA+alt+shift+d: imleci orijinal öğeye, örneğin uzun bir açıklama gibi daha fazla ayrıntı içeren bir resme taşır. İlgili ek açıklamalara gitmek için NVDA+alt+d'ye birkaç kez basıldıysa, her bir kaynağa geri dönmek mümkün olacaktır.

Yukarıdaki komutlar NVDA menüsünden, Tercihler alt menüsünden, Girdi hareketleri iletişim kutusundan, Tarama Kipi kategorisinden değiştirilebilir.

## 2.0 için değişiklikler ##

* Birden fazla açıklama kaynağına geri dönme yeteneği eklendi.
* NVDA 2023.1 veya üzerini gerektirir.


[1]: https://github.com/nvaccess/nvda/issues/13940
