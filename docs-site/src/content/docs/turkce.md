---
title: Türkçe
description: shopfloor-skills, üretim hatlarını yöneten kişiler için Agent Skills ve alt agent'lardan oluşan açık kaynaklı bir settir.
---

<div lang="tr">

`shopfloor-skills`, üretim hatlarını yöneten kişiler için Agent Skills ve alt agent'lardan (subagent) oluşan açık kaynaklı bir settir. Kimler için: üretim ve proses mühendisleri, vardiya ve alan liderleri, sürekli iyileştirme koçları.

Üç alanı kapsar:

1. **Verimlilik ve akış:** OEE, geçiş süresi (throughput time), hat dengeleme, SMED, TPM, kanban, değer akışı ve kaizen.
2. **Günlük sahada liderlik:** kademeli toplantılar (tier meeting), KPI panoları, eskalasyon ve gemba yürüyüşleri.
3. **Hattı kararlı tutan dokümanlar:** kontrol planı, istasyon talimatları, SPC, 8D ve kök neden araçları, proses denetimleri.

## Durum

Proje geliştirme aşamasındadır. Bugün 20 skill'in tamamı hazırdır; ayrıca `8d-moderator` agent'ı. `lead-daily-routine` kademeli toplantıları, SQDCP panosunu, aynı gün eskalasyonu ve aksiyon takibini tasarlar, yürütür ve denetler. `solve-8d` bir 8D'yi D0'dan D8'e yürütür ve açık bir 8D'nin kapatılıp kapatılamayacağını kontrol eder. `measure-oee` OEE ve TEEP'i hesaplar ve kayıpları dakika cinsinden bir kayıp ağacında sıralar. `improve-tpt` geçiş süresini Little Yasası ile ölçer ve WIP sınırıyla kısaltır. `improve-line-balancing` hattı takt, ergonomi ve dolum yamazumisiyle dengeler. `improve-smed` bir ürün değişimi (setup) çalışması yürütür. `improve-tpm` MTBF ve MTTR'yi hesaplar ve otonom bakım adımlarını denetler. `lead-gemba-walk` gemba yürüyüşlerini planlar, yürütür ve suçlamasız bir gözlem kaydıyla takip eder. `measure-spc` kontrol kartını seçer, kontrol sınırlarını hesaplar, sinyalleri bulur ve her sinyali reaksiyon planına bağlar. `improve-vsm` mevcut ve gelecek durum değer akışı haritalarını çizer ve gelecek durumu sorumlu ve hedefli bir döngü planına çevirir. `improve-kanban-pull` süpermarket, FIFO hattı veya CONWIP arasında seçim yapar ve kanban kart sayısını hesaplar. `improve-kaizen` doğru iyileştirme biçimini seçer ve her sonucu yeni bir standart ve 30/60/90 günlük sürdürme planıyla bitirir. `plan-control-plan` proses kontrol planını PFMEA'dan satır satır oluşturur veya gözden geçirir ve her satıra sorumlusu belli bir reaksiyon planı verir. `plan-workstation-instructions` istasyon muayene ve iş talimatlarını kontrol planından türetir ve yedi tutarlılık kontrolüyle karşılaştırır. `solve-5why` oluşma, tespit edilememe ve sistem nedenleri için 5 Neden zincirleri kurar ve her halkayı kanıtla kontrol eder. `solve-fishbone` bir balık kılçığı (6M) beyin fırtınasını test edilebilir neden hipotezlerine çevirir; neden listesini genişletir. `solve-is-is-not` problemi Is/Is-Not (olan/olmayan) karşılaştırmasıyla sınırlar ve olası nedenleri gerçeklere karşı test ederek eler; neden listesini daraltır. `solve-pdca` bir A3 üzerinde tek bir PDCA döngüsü yürütür: ölçülmüş başlangıç değeri, önceden yazılmış tahmin, küçük bir deneme ve ölçülmüş kontrol. `solve-dmaic` bol veri olan kronik problemlerde DMAIC projesi yürütür ve faz geçiş (tollgate) incelemelerini yapar. `audit-process` proses denetimlerini, VDA 6.3 puanlamasını, katmanlı proses denetimi (LPA) programını ve sahada yönetim öz denetimlerini planlar, yürütür ve raporlar. Diğer agent'lar planlanmıştır ve gruplar hâlinde eklenecektir; tam liste için [kataloğa](/skills/catalogue/) bakın.

## Kurulum

Claude Code oturumunda:

```
/plugin marketplace add mftnakrsu/shopfloor-skills
/plugin install shopfloor-skills@shopfloor-skills
```

OpenCode, Qwen Code veya Cursor için depoyu klonlayın ve kurulum betiğini proje klasörünüzden çalıştırın. Python 3.10 veya üstü yeterlidir:

```
git clone https://github.com/mftnakrsu/shopfloor-skills
cd your-project
python3 ../shopfloor-skills/scripts/install.py --tool opencode
```

Diğer araçlar için `--tool qwen`, `--tool cursor` veya `--tool all` kullanın. Agent Skills biçimini okuyan herhangi bir araçta yalnızca skill'leri kurmak için:

```
npx skills add mftnakrsu/shopfloor-skills
```

## Kullanım

Skill'i adıyla çağırmanız gerekmez. Agent'ınıza kendi cümlelerinizle sorun; agent, isteğinize uyan skill'i kendisi yükler. Örneğin: *"Fabrikamız için üç kademeli bir toplantı düzeni tasarla; iki vardiya var, sabah vardiyası 06:00'da başlıyor."* Eksik bir bilgi varsa skill onu sorar, uydurmaz. Daha küçük modeller (örneğin Haiku) skill'i kendiliğinden yüklemeyebilir; istemde adını verin, örneğin 'measure-spc kullan'.

## Kurallar

- Her içerik kamuya açık literatürden, projenin kendi cümleleriyle yazılır.
- Hiçbir skill, agent veya test vakası işveren, fabrika, müşteri, ürün ya da kişi adı içermez.
- Her sayının bir kaynağı vardır ya da "rule of thumb" (pratik kural) veya "set by local policy" (yerel kurala göre) olarak işaretlenir.
- Standartlar yalnızca madde numarasıyla anılır. ISO, IATF, VDA ve AIAG yayınlarının telif hakkı yayıncılarına aittir; bağlayıcı metin için resmî dokümanları kullanın.

Lisans: MIT.

</div>
