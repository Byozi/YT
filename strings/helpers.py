#
# Copyright (C) 2021-2022 by Byozi@Github, < https://github.com/Byozi >.
#
# This file is part of < https://github.com/Byozi/YT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Byozi/YT/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Yönetici Komutları:</u>**

**c** Kanal Komutları İçerir.

/duraklat - Oynatılan müziği duraklatır.
/devam  - Duraklatılmış müziği devam ettirir.
/sustur - Oynatılan müziği sessize alır.
/sesiac - Sessiz yapılan müziği geri açar.
/atla  - Şu anda çalınan müziği atlar.
/durdur  - Oynatılan müziği durdurur.
/karistir - Sıradaki çalma listesini rastgele karıştırır.
/seek - Müziği belirtilen süreye ileri alır.
/seekback - Müziği belirtilen süreye geri alır.
/restart - Sohbetiniz için botu yeniden başlatır.


✅<u>**Spesifik Atlama:**</u>
/atla [Sayı(örnek: 3)]
- Müziği belirtilen sıra numarasına atlar. Örnek: /atla 3, müziği üçüncü sıradaki müziğe atlar ve kuyrukta bulunan 1. ve 2. müzikleri görmezden gelir.

✅<u>**Döngü Oynatma:**</u>
/dongu  [enabled/disabled] veya [1-10 arasında sayılar]
- Etkinleştirildiğinde, bot mevcut çalınan müziği 1-10 kez sesli sohbette tekrarlar. Varsayılan olarak 10 kez tekrarlar.

✅<u>**Yetkilendirilmiş Kullanıcılar:**</u>
Yetkili kullanıcılar, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.

/auth [Kullanıcı Adı] - Bir kullanıcıyı grubun yetkilendirme listesine ekler.
/unauth [Kullanıcı Adı] - Bir kullanıcıyı gruptan yetkilendirme listesinden kaldırır.
/authusers - Grubun yetkilendirme listesini kontrol eder."""

HELP_2 = """✅<u>**Oynatma Komutları:**</u>

Mevcut Komutlar = /oynat , /voynat , /cplay

ForcePlay Komutları = /playforce , /vplayforce , /cplayforce

c, kanal oynatması anlamına gelir.
v, video oynatması anlamına gelir.
force, zorla oynatma anlamına gelir.

/oynat veya /voynat veya /cplay - Bot, verdiğiniz sorguyu sesli sohbette oynatmaya başlar veya sesli sohbetlerde canlı bağlantıları akıtır.

/playforce veya /vplayforce veya /cplayforce - Force Play, sesli sohbette çalınan mevcut müziği durdurur ve aranan müziği sırayı bozmadan hemen çalmaya başlar.

/channelplay [Sohbet kullanıcı adı veya id] veya [Devre dışı] - Kanalı bir gruba bağlar ve grup sesli sohbetinde kanalın müziğini akıtır.

✅**<u>Bot'un Sunucu Çalma Listeleri:</u>**
/oynatmalistesi - Sunuculardaki kaydedilmiş çalma listelerinizi kontrol eder.
/deleteplaylist - Çalma listenizdeki herhangi bir kayıtlı müziği siler.
/oynay - Sunuculardan Kaydedilmiş Çalma Listesini Çalmaya Başlar."""


HELP_3 = """✅<u>**Bot Komutları:**</u>

/soz [Müzik İsmi] - Belirli bir müziğin sözlerini web üzerinde arar.

/sarki [Şarkı İsmi] veya [YT Linki] - Youtube'dan mp3 veya mp4 formatında herhangi bir şarkıyı indirir.

/player - Etkileşimli Bir Oynatma Paneli Alır.

**c** kanal çalması anlamına gelir.

/queue veya /cqueue - Müzik Sırasını Kontrol Eder."""

HELP_4 = """✅<u>**Ekstra Komutlar:**</u>
/start - Müzik Botunu Başlatır.
/yardim - Komutların detaylı açıklamalarını içeren Yardım Menüsünü alır.
/ping- Bot'a ping atar ve Bot'un Ram, Cpu vb. istatistiklerini kontrol eder.

✅<u>Grup Ayarları:</u>
/ayarlar - Grubun tüm ayarlarını içeren düğmelerle birlikte tam bir ayar paneli alır.

🔗 **Ayarlar seçenekleri**:

1️⃣ **Ses Kalitesi** - Sesli sohbette yayınlamak istediğiniz ses kalitesini ayarlayabilirsiniz.

2️⃣ **Video Kalitesi** - Sesli sohbette yayınlamak istediğiniz video kalitesini ayarlayabilirsiniz.

3️⃣ **Yetkili Kullanıcılar** - Bu bölümden yönetici komutlarını herkese veya yalnızca yöneticilere değiştirebilirsiniz. Herkese izin verilirse, gruptaki herhangi biri yönetici komutlarını (/atla, /durdur vb.) kullanabilecektir.

4️⃣ **Temiz Mod** - Etkinleştirildiğinde, botun mesajlarını grubunuzdan 5 dakika sonra siler ve sohbetinizin temiz ve düzenli kalmasını sağlar.

5️⃣ **Komut Temizleme** - Aktifleştirildiğinde, Bot komutlarını (/oynat, /duraklat, /shuffle, /durdur vb.) hemen siler.

6️⃣ **Oynatma Ayarları**:

**/playmode** - Grubunuzun oynatma ayarlarını belirleyebileceğiniz düğmelerle birlikte tam bir oynatma ayarları paneli alırsınız.

<u>**Oynatma ayarları seçenekleri**:</u>

1️⃣ **Arama Modu** [Doğrudan veya İnline] - /oynat modunda arama modunuzu değiştirir.

2️⃣ **Yönetici Komutları** [Herkese veya Yöneticilere] - Eğer herkese izin verilirse, gruptaki herhangi biri yönetici komutlarını (/atla, /durdur vb.) kullanabilecektir.

3️⃣ **Oynatma Türü** [Herkese veya Yöneticilere] - Eğer yöneticilere izin verilirse, sadece gruptaki yöneticiler müzik çalabilirler."""

HELP_5 = """🔰**<u>Kurucu & Yönetici Ekleme İşlemleri :</u>**
/addsudo [Kullanıcı Adı veya Bir kullanıcıya yanıt verin]
/delsudo [Kullanıcı Adı veya Bir kullanıcıya yanıt verin]

🛃**<u>HEROKU:</u>**
/usage - Dyno Kullanımı.

🌐**<u>CONFIG VARS:</u>**
/get_var - Heroku'dan veya .env'den bir config var alın.
/del_var - Heroku'dan veya .env'den herhangi bir varı silin.
/set_var [Var Adı] [Değer] - Bir Var ayarlayın veya bir Var'ı güncelleyin, boşlukla ayrılmış bir Var ve Değer kullanın.

🤖**<u>BOT KOMUTLARI:</u>**
/reboot - Botunuzu yeniden başlatır.
/update - Botu günceller.
/speedtest - Sunucu hızlarını kontrol eder.
/maintenance [enable / disable] 
/logger [enable / disable] - Bot aramaları kaydederek logger grubunda tutar.
/get_log [Satır Sayısı] - Botunuzun günlüğünü Heroku veya VPS'den alın. Her ikisi için çalışır.
/autoend [enable|disable] - Kimse dinlemiyorsa 3 dakika sonra otomatik olarak yayını sonlandırma özelliğini etkinleştirin.

📈**<u>İSTATİSTİK KOMUTLARI:</u>**
/activevoice - Bot üzerindeki etkin sesli sohbetleri kontrol edin.
/activevideo - Bot üzerindeki etkin video görüşmelerini kontrol edin.
/stats - Botun İstatistiklerini kontrol edin.

⚠️**<u>KARALISTE FONKSIYONU:</u>**
/blacklistchat [CHAT_ID] - Herhangi bir sohbeti Müzik Botundan engelleyin.
/whitelistchat [CHAT_ID] - Müzik Botunu kara listeye alınan herhangi bir sohbetten çıkarın.
/blacklistedchat - Tüm kara listeye alınan sohbetleri kontrol edin.

👤**<u>YASAKLAMA FONKSIYONU:</u>**
/block [Username or Reply to a user] - Bir kullanıcının bot komutlarını kullanmasını engeller.
/unblock [Username or Reply to a user] - Bir kullanıcıyı Bot'un Engellenen Listesinden kaldırır.
/blockedusers - Engellenen Kullanıcı Listesini kontrol edin.

👤**<u>GRUP BAN FONKSIYONU:</u>**
/gban [Username or Reply to a user] - Bir kullanıcıyı botun hizmet verdiği sohbetten engeller ve botunuzu kullanmasını durdurur.
/ungban [Username or Reply to a user] - Bir kullanıcıyı Bot'un gbanned Listesinden kaldırır ve kullanıcıya botunuzu kullanma izni verir.
/gbannedusers - Gbanned Kullanıcı Listesini kontrol edin.

🎥**<u>VIDEO ARAMA FONKSIYONU:</u>**
/set_video_limit [Chats Sayısı] - Bir seferde izin verilen Maksimum Sohbet Sayısını ayarlayın. Varsayılan olarak 3 sohbet.
/videomode [download|m3u8] - Eğer indirme modu etkinse, Bot videoları M3u8 formatında oynatmak yerine indirecektir. Varsayılan olarak M3u8. M3u8 modunda herhangi bir sorgu oynatılmazsa indirme modunu kullanabilirsiniz.

⚡️**<u>ÖZEL BOT İŞLEVİ:</u>**
/authorize [CHAT_ID] - Bir sohbeti botunuzu kullanmak için yetkilendirin.
/unauthorize [CHAT_ID] - Bir sohbetin botunuzu kullanmasını engelleyin.
/authorized - Botunuza izin verilen tüm sohbetleri kontrol edin.

🌐**<u>YAYIN İŞLEVİ:</u>**
/broadcast [Mesaj veya Mesaja Yanıt Verin] - Botun Hizmet Verdiği Sohbetlere herhangi bir mesajı yayınlayın.

<u>yayın seçenekleri:</u>
**-pin**: Bu mesajı sabitleyin.
**-pinloud**: Bu mesajı yüksek bildirimle sabitleyin.
**-user**: Bu mesajı botunuzu başlatan kullanıcılara yayınlayın.
**-assistant**: Bu mesajı botunuzun asistan hesabından yayınlayın.
**-nobot**: Botunuzun mesaj yayınlamasını zorlayın.

**Örnek:** `/broadcast -user -assistant -pin Merhaba Test`


"""
