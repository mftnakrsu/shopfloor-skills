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

Proje geliştirme aşamasındadır. Bugün on iki skill hazırdır: `lead-daily-routine`, `lead-gemba-walk`, `measure-oee`, `measure-spc`, `improve-tpt`, `improve-line-balancing`, `improve-smed`, `improve-tpm`, `improve-vsm`, `improve-kanban-pull`, `improve-kaizen` ve `solve-8d`; ayrıca `8d-moderator` agent'ı. `lead-daily-routine` kademeli toplantıları, SQDCP panosunu, aynı gün eskalasyonu ve aksiyon takibini tasarlar, yürütür ve denetler. `solve-8d` bir 8D'yi D0'dan D8'e yürütür ve açık bir 8D'nin kapatılıp kapatılamayacağını kontrol eder. `measure-oee` OEE ve TEEP'i hesaplar ve kayıpları dakika cinsinden bir kayıp ağacında sıralar. `improve-tpt` geçiş süresini Little Yasası ile ölçer ve WIP sınırıyla kısaltır. `improve-line-balancing` hattı takt, ergonomi ve dolum yamazumisiyle dengeler. `improve-smed` bir ürün değişimi (setup) çalışması yürütür. `improve-tpm` MTBF ve MTTR'yi hesaplar ve otonom bakım adımlarını denetler. `lead-gemba-walk` gemba yürüyüşlerini planlar, yürütür ve suçlamasız bir gözlem kaydıyla takip eder. `measure-spc` kontrol kartını seçer, kontrol sınırlarını hesaplar, sinyalleri bulur ve her sinyali reaksiyon planına bağlar. `improve-vsm` mevcut ve gelecek durum değer akışı haritalarını çizer ve gelecek durumu sorumlu ve hedefli bir döngü planına çevirir. `improve-kanban-pull` süpermarket, FIFO hattı veya CONWIP arasında seçim yapar ve kanban kart sayısını hesaplar. `improve-kaizen` doğru iyileştirme biçimini seçer ve her sonucu yeni bir standart ve 30/60/90 günlük sürdürme planıyla bitirir. [Katalogdaki](/skills/catalogue/) diğer skill'ler planlanmıştır ve gruplar hâlinde eklenecektir.

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
