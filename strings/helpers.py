#
# Copyright (C) 2021-2022 by Byozi@Github, < https://github.com/Byozi >.
#
# This file is part of < https://github.com/Byozi/YT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Byozi/YT/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """❌Sadece Gruptaki Adminler İçin Komutlar:❌**

Bu komutları grubunuzun içerisinde kullanmanız için tasarladık. Bot panelinde kullnılacak komutlar diğer menüdedir.

👉🏻 /start - Botu başlatır.
👉🏻 /duraklat - Oynatılan müziği duraklatır.
👉🏻 /devam  - Duraklatılmış müziği devam ettirir.
👉🏻 /sustur - Oynatılan müziği sessize alır.
👉🏻 /sesiac - Sessiz yapılan müziği geri açar.
👉🏻 /atla  - Şu anda çalınan müziği atlar.
👉🏻 /son  - Oynatılan müziği sonlandırır ve yayını kapatır.
👉🏻 /karistir - Sıradaki çalma listesini rastgele karıştırır.
👉🏻 /ilerisar - Müziği belirtilen süreye ileri alır.
👉🏻 /gerisar - Müziği belirtilen süreye geri alır.
👉🏻 /atla - Müziği belirtilen sıra numarasına atlar. Örnek: /atla 3, müziği üçüncü sıradaki müziğe atlamasını sağlar.
👉🏻 /dongu - Etkinleştirildiğinde, bot mevcut çalınan müziği 1-10 kez sesli sohbette tekrarlar. Örnek : /dongu 5 bu komut 5 kere tekrar açar.
👉🏻 /yetkiver [Kullanıcı Adı] - Bir kullanıcıyı grubun yetkilendirme listesine ekler.
👉🏻 /yetkial [Kullanıcı Adı] - Bir kullanıcıyı gruptan yetkilendirme listesinden kaldırır.
👉🏻 /yetkililer - Grubun yetkilendirme listesini kontrol eder."""

HELP_2 = """❌<u>**Oynatma Komutları:**</u>❌

👉 /oynat - Şarkı oynatır.
👉 /oynat komutu aynı zamanda canlı yayında destekler.(örnek: /oynat KralFm canlı)
👉 /oynathemen - Sesli sohbette çalınan parçayı durdurur ve sırayı bozmadan temizlemeden aranan parçayı anında çalmaya başlar.
👉 /voynat - Video Oynatır.
👉 /voynat komutu aynı zamanda canlı yayınıda destekler.(örnek: /vplay ATV Canlı)
👉 /voynathemen - Sesli sohbette çalınan video yayınını durdurur ve sırayı bozmadan temizlemeden aranan videoyu anında çalmaya başlar.
👉 /komutlar - Bu komutu Grubunuzda yazarak komutları görebilirsiniz.

 **<u>Bot'un Sunucu Çalma Listeleri:</u>**
👉 /oynatmalistesi - Sunuculardaki kaydedilmiş çalma listelerinizi kontrol eder.
👉 /oltemizle - Çalma listenizdeki herhangi bir kayıtlı müziği siler.
👉 /oynat - Sunuculardan Kaydedilmiş Çalma Listesini Çalmaya Başlar."""


HELP_3 = """❌<u>**Bot Komutları:**</u>❌

Bu komutları sadece botun özeline yazınız. Farklı komutlar için bir önceki menüyü kontrol ediniz..

👉 /soz [Müzik İsmi] - Belirli bir müziğin sözlerini web üzerinde arar.
👉 /indir [Şarkı İsmi] veya [YT Linki] - Youtube'dan mp3 veya mp4 formatında herhangi bir şarkıyı indirir.
👉 /player - Etkileşimli Bir Oynatma Paneli Alır. """

HELP_4 = """❌<u>**Ekstra Komutlar:**</u>❌

 Burada bulunan komutlar genel bot komutlarıdır. 

👉/start : Botun Başlatma Panelini Gösterir. 
👉/settings ve ya /ayarlar : Ayarlar Menüsüne Ulaşabilirsiniz.
👉/yardim : Botun Yardım Menüsüne Ulaşırsınız. """
  
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
