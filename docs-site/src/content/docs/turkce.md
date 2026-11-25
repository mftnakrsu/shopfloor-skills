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

Proje geliştirme aşamasındadır. Bugün bir skill hazırdır: `lead-daily-routine`. Kademeli toplantıları, SQDCP panosunu, aynı gün eskalasyonu ve aksiyon takibini tasarlar, yürütür ve denetler. `solve-8d` ve `8d-moderator` agent'ı yakında gelecek. [Katalogdaki](/skills/catalogue/) diğer skill'ler planlanmıştır ve gruplar hâlinde eklenecektir.

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

Skill'i adıyla çağırmanız gerekmez. Agent'ınıza kendi cümlelerinizle sorun; agent, isteğinize uyan skill'i kendisi yükler. Örneğin: *"Fabrikamız için üç kademeli bir toplantı düzeni tasarla; iki vardiya var, sabah vardiyası 06:00'da başlıyor."* Eksik bir bilgi varsa skill onu sorar, uydurmaz.

## Kurallar

- Her içerik kamuya açık literatürden, projenin kendi cümleleriyle yazılır.
- Hiçbir skill, agent veya test vakası işveren, fabrika, müşteri, ürün ya da kişi adı içermez.
- Her sayının bir kaynağı vardır ya da "rule of thumb" (pratik kural) veya "set by local policy" (yerel kurala göre) olarak işaretlenir.
- Standartlar yalnızca madde numarasıyla anılır. ISO, IATF, VDA ve AIAG yayınlarının telif hakkı yayıncılarına aittir; bağlayıcı metin için resmî dokümanları kullanın.

Lisans: MIT.

</div>
