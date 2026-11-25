<p align="center">
  <img src="assets/brand/icon-tile-animated.svg" width="96" height="96" alt="">
</p>

<h1 align="center">shopfloor-skills</h1>

<p align="center">Agent Skills for people who run production lines.</p>

<p align="center">
  <a href="https://github.com/mftnakrsu/shopfloor-skills/actions/workflows/ci.yml"><img src="https://github.com/mftnakrsu/shopfloor-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent%20Skills-markdown-2E8A55" alt="Agent Skills"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2E8A55" alt="MIT license"></a>
</p>

<p align="center">
  <a href="#install"><b>Install</b></a> ·
  <a href="#use">Use</a> ·
  <a href="#whats-inside">Skills</a> ·
  <a href="https://shopfloor-skills.mefby.com">Docs</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="#türkçe">Türkçe</a>
</p>

Agent Skills and subagents for people who run production lines: manufacturing and process engineers, shift and area leaders, and continuous-improvement coaches. They cover productivity and flow (OEE, throughput time, line balancing, SMED, TPM, kanban), daily shopfloor leadership (tier meetings, gemba walks), and the documents that keep a line stable (control plan, station instructions, SPC, 8D, process audits).

Each skill is a folder of plain markdown: a procedure with the inputs to ask for, the steps, the checks to run before answering, and a template for the result. Every number has a source or is marked as a rule of thumb.

**Status:** 1.0.0. All 20 skills and all 6 agents are available; see [CHANGELOG.md](CHANGELOG.md).

## What's inside

The design has 20 skills in six stages and 6 agents. The prefix of a skill's name is its stage.

| Stage | Covers | Skills |
|---|---|---|
| `lead-` | Daily shopfloor leadership | [`lead-daily-routine`](skills/lead-daily-routine/SKILL.md), [`lead-gemba-walk`](skills/lead-gemba-walk/SKILL.md) |
| `measure-` | Seeing the losses | [`measure-oee`](skills/measure-oee/SKILL.md), [`measure-spc`](skills/measure-spc/SKILL.md) |
| `improve-` | Productivity and flow | [`improve-tpt`](skills/improve-tpt/SKILL.md), [`improve-line-balancing`](skills/improve-line-balancing/SKILL.md), [`improve-smed`](skills/improve-smed/SKILL.md), [`improve-tpm`](skills/improve-tpm/SKILL.md), [`improve-vsm`](skills/improve-vsm/SKILL.md), [`improve-kanban-pull`](skills/improve-kanban-pull/SKILL.md), [`improve-kaizen`](skills/improve-kaizen/SKILL.md) |
| `plan-` | The documents that keep a line stable | [`plan-control-plan`](skills/plan-control-plan/SKILL.md), [`plan-workstation-instructions`](skills/plan-workstation-instructions/SKILL.md) |
| `solve-` | Root cause and problem solving | [`solve-8d`](skills/solve-8d/SKILL.md), [`solve-5why`](skills/solve-5why/SKILL.md), [`solve-fishbone`](skills/solve-fishbone/SKILL.md), [`solve-is-is-not`](skills/solve-is-is-not/SKILL.md), [`solve-pdca`](skills/solve-pdca/SKILL.md), [`solve-dmaic`](skills/solve-dmaic/SKILL.md) |
| `audit-` | Checking the system | [`audit-process`](skills/audit-process/SKILL.md) |

**Agents:** [`skill-reviewer`](agents/skill-reviewer.md) (a tool for maintainers) reviews a new skill against the project's rules. [`8d-moderator`](agents/8d-moderator.md) leads an 8D team from D0 to D8. [`problem-solving-coach`](agents/problem-solving-coach.md) takes everyday line problems, picks the root-cause method and hands over to `8d-moderator` when the 8D criteria are met. [`inspection-planner`](agents/inspection-planner.md) builds the control plan, derives the station instructions from it and runs the 7 consistency checks. [`pfmea-chain-checker`](agents/pfmea-chain-checker.md) checks, station by station, that every PFMEA failure mode needing a control has one in the control plan, and reports gaps without editing. [`process-auditor`](agents/process-auditor.md) runs process audits, layered process audits and shopfloor-management self-audits, backed by gemba evidence.

The skills hand work to each other as one loop: see the problem, fix the cause, hold the gain in the control plan and station instructions. The [docs site](https://shopfloor-skills.mefby.com) has the full catalogue and the loop.

## Install

**Claude Code**

```
/plugin marketplace add mftnakrsu/shopfloor-skills
/plugin install shopfloor-skills@shopfloor-skills
```

**OpenCode (version 2 or later), Qwen Code or Cursor**

```
git clone https://github.com/mftnakrsu/shopfloor-skills
cd your-project
python3 ../shopfloor-skills/scripts/install.py --tool opencode
```

Use `--tool qwen`, `--tool cursor` or `--tool all` for the other tools. Add `--scope user` to install for your user account instead of one project, and `--dry-run` to see every file it would write. It needs Python 3.10 or newer and nothing else.

**Skills only, in any Agent Skills tool**

```
npx skills add mftnakrsu/shopfloor-skills
```

## Use

Ask your agent in your own words. It loads the skill whose description matches the request. For example:

> Design a tier meeting cascade for our plant: three levels, two shifts, the early shift starts at 06:00.

`lead-daily-routine` designs the cascade, runs today's meeting from your board values, or audits a routine that is not working. When an input it needs is missing, it asks for it instead of inventing it. In Claude Code you can also start it by name with `/shopfloor-skills:lead-daily-routine`.

`solve-8d` leads an 8D from D0 to D8, or checks whether an open one can be closed:

> A customer complained about cracked housings on part H-200: 12 of 4,000 delivered. Start an 8D.

> Here is our 8D. Can we close it?

Smaller models (for example Haiku) may not load a skill on their own; name it in the prompt, e.g. 'use measure-spc'.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The logo and its rules are in [assets/brand/BRAND.md](assets/brand/BRAND.md).

## Standards and license

ISO, IATF, VDA and AIAG publications are copyrighted by their publishers. Clause numbers in this project are pointers, and every summary is written in our own words. Use the official documents for the binding text.

MIT License. See [LICENSE](LICENSE).

## Türkçe

`shopfloor-skills`, üretim hatlarını yöneten kişiler için Agent Skills ve alt agent'lardan oluşan açık kaynaklı bir settir: üretim ve proses mühendisleri, vardiya ve alan liderleri, sürekli iyileştirme koçları için. Verimlilik ve akışı (OEE, geçiş süresi, hat dengeleme, SMED, TPM, kanban), günlük sahada liderliği (kademeli toplantılar, gemba yürüyüşleri) ve hattı kararlı tutan dokümanları (kontrol planı, istasyon talimatları, SPC, 8D, proses denetimleri) kapsar.

Sürüm 1.0.0: 20 skill'in ve 6 agent'ın tamamı hazırdır.

**Kurulum.** Claude Code oturumunda:

```
/plugin marketplace add mftnakrsu/shopfloor-skills
/plugin install shopfloor-skills@shopfloor-skills
```

OpenCode, Qwen Code veya Cursor için depoyu klonlayıp proje klasörünüzde `python3 ../shopfloor-skills/scripts/install.py --tool opencode` (ya da `qwen`, `cursor`, `all`) çalıştırın. Agent Skills okuyan diğer araçlarda yalnızca skill'ler için: `npx skills add mftnakrsu/shopfloor-skills`.

**Kullanım.** Agent'ınıza kendi cümlelerinizle sorun; uygun skill'i kendisi yükler. Eksik bir bilgi varsa skill onu sorar, uydurmaz. Daha küçük modeller (örneğin Haiku) skill'i kendiliğinden yüklemeyebilir; istemde adını verin, örneğin 'measure-spc kullan'. ISO, IATF, VDA ve AIAG yayınlarının telif hakkı yayıncılarına aittir; bu projede yalnızca madde numaraları anılır. Ayrıntılar için [dokümantasyon sitesindeki Türkçe sayfaya](https://shopfloor-skills.mefby.com/turkce/) bakın.
